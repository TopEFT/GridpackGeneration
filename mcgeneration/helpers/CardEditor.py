import os
import shutil
import re

from helper_tools import run_process

class BaseCard(object):
    def __init__(self,card_dir,card_name):
        """
            card_dir: The path to the directory that the original card is located in
            card_name: The name of the original card as it appears in the directory
        """
        self.name = card_name   # Name of the card (e.g. run_card.dat)
        self.cdir = card_dir    # Location of the original card (e.g. the specific template dir)

        self.key_width = 0
        self.val_width = 0

        self.__ops = {}     # Dictionary of options related to the card
        self.__ord = []     # Order in which the options are added

    def exists(self):
        fpath = self.getFilePath()
        return os.path.exists(fpath)

    def list(self):
        return self.__ord

    def size(self):
        return len(self.__ord)

    def clear(self):
        self.key_width = 0
        self.val_width = 0
        self.__ops = {}
        self.__ord = []

    def copy(self,dst,force=False):
        """
            Copy the original card to a new location
                dst: The full path, including the new file name
                force: If true will overwrite the file in the copy directory (default: False)
        """
        src = self.getFilePath()
        if os.path.exists(dst):
            if os.path.samefile(src,dst):
                s = "{src} and {dst} refer to the same file!".format(src=src,dst=dst)
                raise RuntimeError(s)
            if force:
                print "Removing existing file {dst}...".format(dst=dst)
                os.remove(dst)
            else:
                s = "{file} already exists!".format(file=dst)
                raise RuntimeError(s)
        print "Copying to {dst}...".format(dst=dst)
        shutil.copyfile(src,dst)

    def getFilePath(self):
        """
            Returns the path to the original template card
        """
        return os.path.join(self.cdir,self.name)

    def hasOption(self,k):
        """
            Checks if the option exists or not
                k: The name of the option as it appears in the card
        """
        return self.__ops.has_key(k)

    def setOption(self,k,v):
        """
            Set the value of a card option, if the option doesn't already exist adds it to the list
                k: The name of the option as it should appear in the card
                v: The value for the option. NOTE: will be typecast to a string
        """
        if not self.hasOption(k):
            self.key_width = max(self.key_width,len(k))
            self.__ord.append(k)
        self.val_width = max(self.val_width,len(str(v)))
        self.__ops[k] = str(v)

    def getOption(self,k):
        """
            Try to return the value of a particular option
                k: The name of the option as it appears in the card
        """
        try:
            r = self.__ops[k]
        except KeyError as e:
            raise e
        return r

    def dump(self):
        """
            Basic method for printing all of the options of the card. Can be reimplemented in the
            derived classes
        """
        for k in self.list():
            v = self.__ops[k]
            print "{0:>{w1}} = {1:<{w2}}".format(k,v,w1=self.key_width,w2=self.val_width)

    def parse(self):
        """
            Abstract method for parsing a card in order to extract setting names and values. Should
            be implemented in the derived classes
        """
        raise NotImplementedError

    def save(self):
        """
            Abstract method for saving the current internal state of the card's options. Should be
            implemented in the derived classes
        """
        raise NotImplementedError

class MGRunCard(BaseCard):
    LINE_COMMENT = "#"
    EOL_COMMENT  = "!"

    def __init__(self,*args,**kwargs):
        super(MGRunCard,self).__init__(*args,**kwargs)

        self.line_width = 0
        self.__line_map = {}    # A record of the original unmodified line

        self.parse()

    def parse(self):
        """ Parser for a MadGraph run card """
        fpath = self.getFilePath()
        with open(fpath,'r') as f:
            for l in f:
                orig_line = l
                idx = l.find(self.LINE_COMMENT)
                if idx != -1:
                    l = l[:idx]
                idx = l.find(self.EOL_COMMENT)
                if idx != -1:
                    l = l[:idx]
                l = l.strip()
                if len(l) == 0: continue
                lst = l.split('=')
                if len(lst) != 2:
                    continue
                v,k = [x.strip() for x in lst]
                self.setOption(k,v)
                self.__line_map[k] = orig_line.strip('\n')
                self.line_width = max(self.line_width,len(orig_line.strip('\n')))
                
    def dump(self):
        h = "{0:>{w1}} = {1:<{w2}} -- {2:<{w3}}".format("KEY","VALUE","ORIGINAL",
            w1=self.key_width,
            w2=self.val_width,
            w3=self.line_width
        )
        print h
        print "-"*(len(h))
        for k in self.list():
            v = self.getOption(k)
            l = self.__line_map[k]
            print "{0:>{w1}} = {1:<{w2}} -- {2}".format(k,v,l,w1=self.key_width,w2=self.val_width)

    def save(self,dst,force=False):
        self.copy(dst,force=force)

        for k in self.list():
            v = self.getOption(k)
            old = self.__line_map[k]
            repl = " {0:>{w1}} = {1:<{w2}} {eol}".format(v,k,
                w1=self.val_width,
                w2=self.key_width,
                eol=self.EOL_COMMENT
            )
            pat = r".*=\s*%s\s*[!#]?" % (k)
            new = re.sub(pat,repl,old)

            # Need to escape any special chars otherwise sed won't match the line
            old = old.replace('\\','\\\\').replace('*','\\*')
            new = new.replace('\\','\\\\').replace('*','\\*')
            
            #print "{old:<{w}} --> {new}".format(old=old,new=new,w=self.line_width)

            sed_cmd = "s|{old}|{new}|g".format(old=old,new=new)
            run_process(['sed','-i','-e',sed_cmd,dst])

class MGCustomizeCard(BaseCard):
    LINE_COMMENT = "#"

    def __init__(self,*args,**kwargs):
        super(MGCustomizeCard,self).__init__(*args,**kwargs)
        self.parse()

    def parse(self):
        fpath = self.getFilePath()
        with open(fpath,'r') as f:
            for l in f:
                idx = l.find(self.LINE_COMMENT)
                if idx != -1:
                    l = l[:idx]
                l = l.strip()
                if len(l) == 0: continue
                self.setOption(l)

    def setOption(self,l):
        idx = self.size()   # Note: array size and array index are always offset by 1 from each other
        super(MGCustomizeCard,self).setOption(str(idx),l)

    def dump(self):
        for k in self.list():
            v = self.getOption(k)
            print "[{0:>{w1}}] {1:<{w2}}".format(k,v,w1=self.key_width,w2=self.val_width)

    def save(self,dst,force=False,indent=0):
        indent_str = " "*4*indent
        if os.path.exists(dst):
            if not os.path.isfile(dst):
                s = "{ind}{dst} is not a file!".format(dst=dst,ind=indent_str)
                raise RuntimeError(s)
            if force:
                print "{ind}Removing {dst}...".format(dst=dst,ind=indent_str)
                os.remove(dst)
            else:
                s = "{ind}{file} already exists!".format(file=dst,ind=indent_str)
                raise RuntimeError(s)
        print "{ind}Saving to {dst}...".format(dst=dst,ind=indent_str)
        with open(dst,'w') as f:
            for k in self.list():
                v = self.getOption(k)
                f.write(v+'\n')


def test_run_card():
    home_dir = "/home/issa/Documents/Research/lannon/CERN/EFT_Research/MG_Studies/TopEFT/mcgeneration"
    card_dir = "addons/cards/example_testing"
    ex_dir = os.path.join(home_dir,card_dir)

    rc = MGRunCard(card_name='run_card.dat',card_dir=ex_dir)
    #for k in rc.list():
    #    rc.setOption(k,'42.0')
    rc.setOption('bwcutoff','9999')
    rc.setOption('xn','42')
    rc.dump()

    #fpath = os.path.join(ex_dir,'mod_run_card.dat')
    #rc.save(fpath,force=True)

def test_customize_card():
    home_dir = "/home/issa/Documents/Research/lannon/CERN/EFT_Research/MG_Studies/TopEFT/mcgeneration"
    card_dir = "addons/cards/example_testing"
    ex_dir = os.path.join(home_dir,card_dir)

    cc = MGCustomizeCard(card_name='customizecards.dat',card_dir=ex_dir)

    cc.setOption('set param_card MB 0')
    cc.dump()

    #fpath = os.path.join(ex_dir,'mod_customize_card.dat')
    #cc.save(fpath,force=True)
    

if __name__ == "__main__":
    test_run_card()
    test_customize_card()