import os

class MGProcess(object):
    TDIR = "template_cards"
    TEMPLATE_RUN_CARD = 'run_card.dat'
    TEMPLATE_CUSTOM_CARD = 'customizecards.dat'

    def __init__(self,name,process,pcard,tdir):
        self.setName(name)
        self.setProcess(process)
        self.setProcessCard(pcard)
        self.setTemplateDir(tdir)

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getProcess(self):
        return self.p

    def setProcess(self,p):
        self.p = p

    def getProcessCard(self):
        return self.pcard

    def setProcessCard(self,card):
        self.pcard = card

    def getTemplateDir(self):
        return self.template_dir

    def setTemplateDir(self,tdir):
        self.template_dir = os.path.join(self.TDIR,tdir)

    def getFlavorScheme(self,card_dir):
        fpath = os.path.join(card_dir,self.getTemplateDir(),self.TEMPLATE_RUN_CARD)
        flvr_str = "maxjetflavor"
        comment_char = "#"
        flvr_scheme = -1
        with open(fpath,'r') as f:
            for l in f:
                l = l.strip()
                if len(l) == 0 or l[0] == comment_char:
                    continue
                elif not flvr_str in l:
                    continue
                lst = l.split('=')
                if len(lst) != 2:
                    continue
                s1,s2 = lst
                flvr_scheme = int(s1)   # Doesn't care about whitespace
                break
        return flvr_scheme



if __name__ == "__main__":
    ttH      = MGProcess(name='ttH'     ,process='ttH'  ,pcard='ttH.dat'     ,tdir='defaultPDFs_template')
    ttHJet   = MGProcess(name='ttHJet'  ,process='ttH'  ,pcard='ttHJet.dat'  ,tdir='jets_template')
    ttHDecay = MGProcess(name='ttHDecay',process='ttH'  ,pcard='ttHDecay.dat',tdir='defaultPDFs_template')
    ttll     = MGProcess(name='ttll'    ,process='ttll' ,pcard='ttll.dat'    ,tdir='defaultPDFs_template')
    ttlnu    = MGProcess(name='ttlnu'   ,process='ttlnu',pcard='ttlnu.dat'   ,tdir='defaultPDFs_template')
    tllq     = MGProcess(name='tllq'    ,process='tllq' ,pcard='tllq.dat'    ,tdir='defaultPDFs_template')
    tHq      = MGProcess(name='tHq'     ,process='tHq'  ,pcard='tHq.dat'     ,tdir='tHq_template')
