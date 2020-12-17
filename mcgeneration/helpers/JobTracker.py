import os
import datetime
import math
from helper_tools import run_process,regex_match

# Utility class for keeping track of gridpack production jobs
# NOTE: This assumes that all the relevant log files are in the same directory
class JobTracker(object):
    RUNNING = 'running'
    CODEGEN = 'codegen'
    INTEGRATE = 'intg_all'
    INTEGRATE_FILTER = 'intg_filter'
    STUCK = 'stuck'
    FINISHED = 'finished'

    @classmethod
    def getJobTypes(cls):
        return [cls.RUNNING,cls.CODEGEN,cls.INTEGRATE,cls.FINISHED]

    @classmethod
    def formatTime(cls,t):
        h = max(math.floor(t/3600.0),0)
        m = max(math.floor((t - h*3600)/60.0),0)
        s = max(t - h*3600 - m*60,0)

        h = "%d" % (h)
        m = "%d" % (m)
        s = "%d" % (s)
        return (h,m,s)
        #return (h.rjust(2,"0"),m.rjust(2,"0"),s.rjust(2,"0"))

    def __init__(self,fdir='.'):
        self.fdir = fdir        # Where to look for output files
        self.intg_cutoff = -1
        self.stuck_cutoff = -1
        self.tarball_cutoff = -1    # Large value requires the tarball to go longer periods without being modified
        self.proc_filter = []       # A list of strings to compare against in order to filter out jobs from other batch runs
        self.tags_filter = []
        self.runs_filter = []

        self.resubmitted = {}

        self.use_cached_update = False     # If true, then getRunningJobs() should return

        self.scram_arch = 'slc6_amd64_gcc630'
        self.cmssw_release = 'CMSSW_9_3_0'

        self.update()

    def update(self):
        self.last_update = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.all = self.getJobs(no_cache=True)               # A job is a string of the form: p_c_r
        self.finished = self.getFinishedJobs(no_cache=True)
        self.running = self.getRunningJobs(no_cache=True)
        self.codegen = self.getCodeGenJobs()
        self.intg_full = self.getIntegrateJobs()
        self.intg_filter = self.getIntegrateJobs(self.intg_cutoff)
        self.stuck = self.getStuckJobs(self.stuck_cutoff)

    def addResubmit(self,job):
        if not self.resubmitted.has_key(job):
            self.resubmitted[job] = 0
        self.resubmitted[job] += 1

    def setDirectory(self,fdir):
        self.fdir = fdr

    def setIntegrateCutoff(self,v):
        self.intg_cutoff = v

    def setStuckCutoff(self,v):
        self.stuck_cutoff = v

    def setTarballCutoff(self,v):
        self.tarball_cutoff = v

    def setJobFilters(self,procs=[],tags=[],runs=[]):
        # The if statements ensure we don't accidentally erase one of the filters
        if procs: self.proc_filter = list(procs)
        if tags:  self.tags_filter = list(tags)
        if runs:  self.runs_filter = list(runs)

    # Explicitly clear all job filters
    def clearJobFilters(self):
        self.proc_filter = []
        self.tags_filter = []
        self.runs_filter = []

    # Return a list of scanpoint files in the target directory
    def getScanpointFiles(self,fdir='.'):
        fnames = []
        for fn in os.listdir(fdir):
            fpath = os.path.join(fdir,fn)
            if os.path.isdir(fpath):
                continue
            if fn.find("_scanpoints.txt") < 0:
                continue
            fnames.append(fn)
        return fnames

    # Check if the job has produced a tarball
    def hasTarball(self,chk_file,fdir='.'):
        arr = chk_file.split('_')
        p,c,r = arr[:3]
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        fpath = os.path.join(fdir,"{tag}_{scram_arch}_{release}_tarball.tar.xz".format(tag=tag_str,scram_arch=self.scram_arch,release=self.cmssw_release))
        return os.path.exists(fpath)

    # Check if the job's .log file contains an error line
    def logHasError(self,job,fdir='.'):
        # NOTE: Make sure to check that the job exists before calling this fcn
        if not self.isJob(job):
            return False
        fn = os.path.join(fdir,job + '.log')
        rgx = 'Error when reading.*'
        ret = run_process(['grep','-l','-e',rgx,fn],verbose=False)
        return bool(ret)

    # Check if the job's .log file contains a xsec line
    def logHasXsec(self,job,fdir='.'):
        # NOTE: Make sure to check that the job exists before calling this fcn
        fn = os.path.join(fdir,job + '.log')
        rgx = 'Cross-section : '
        ret = run_process(['grep','-l','-e',rgx,fn],verbose=False)
        return bool(ret)

    # Check if the job's .log file indicates that the codegen step failed
    def failedCodegen(self,job,fdir='.'):
        if not self.isJob(job):
            return False
        fn = os.path.join(fdir,job + '.log')
        if not os.path.exists(fn):
            return False
        rgx = '^Process output directory %s not found\.' % (job)
        ret = run_process(['grep','-l','-e',rgx,fn],verbose=False)
        return bool(ret)

    # The job produced a tarball, that stopped being modified sufficiently long ago
    def finishedTarball(self,fn):
        #b = self.hasTarball(fn,self.fdir) and (self.tarball_cutoff == -1 or self.getTarballTime(fn) > self.tarball_cutoff)
        b = self.hasTarball(fn,self.fdir) and self.getTarballTime(fn) > self.tarball_cutoff
        return b

    # Check if the job is still in the code gen phase
    def isCodeGen(self,chk_file,fdir='.'):
        arr = chk_file.split('_')
        p,c,r = arr[:3]
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        log_fpath = os.path.join(fdir,"{tag}.log".format(tag=tag_str))
        input_fpath = os.path.join(fdir,"input_{tag}.tar.gz".format(tag=tag_str))
        codegen1_fpath = os.path.join(fdir,"codegen_{tag}.sh".format(tag=tag_str))
        codegen2_fpath = os.path.join(fdir,"codegen_{tag}.jdl".format(tag=tag_str))
        if not os.path.exists(log_fpath):
            return True
        elif os.path.exists(input_fpath):
            return True
        elif os.path.exists(codegen1_fpath):
            return True
        elif os.path.exists(codegen2_fpath):
            return True
        else:
            return False

    def isStuck(self,fn):
        return (fn in self.stuck)

    def isJob(self,fn):
        return (fn in self.all)

    def isFinished(self,fn):
        b = self.finishedTarball(fn) or self.failedCodegen(fn,self.fdir)
        return b

    # Returns a list of all jobs (based on scanpoints.txt file)
    def getJobs(self,no_cache=False):
        if no_cache or not self.use_cached_update:
            sp_files = self.getScanpointFiles(self.fdir)
            jobs = set()
            for fn in sp_files:
                arr = fn.split('_')
                p,t,r = arr[:3]
                # Skip jobs which don't match the job filters
                if self.proc_filter and len(regex_match([p],self.proc_filter)) == 0: continue
                if self.tags_filter and len(regex_match([t],self.tags_filter)) == 0: continue
                if self.runs_filter and len(regex_match([r],self.runs_filter)) == 0: continue
                jobs.add('_'.join(arr[:3]))
            return jobs
        else:
            return self.all

    # Returns a list of all jobs which have produced a tarball
    # NOTE: Should be mutually exclusive with getRunningJobs()
    def getFinishedJobs(self,no_cache=False):
        if no_cache or not self.use_cached_update:
            jobs = self.getJobs(no_cache=True)
            finished = set()
            for fn in jobs:
                if self.isFinished(fn):
                    finished.add(fn)
            return finished
        else:
            return self.finished

    # Returns a list of all jobs which have not yet produced a tarball
    def getRunningJobs(self,no_cache=False):
        if no_cache or not self.use_cached_update:
            # Calculate the running jobs
            jobs = self.getJobs(no_cache=True)
            finished = self.getFinishedJobs()
            running = jobs - finished   # returns all elements in jobs, but not in finished
            return running
        else:
            # Just return number running from last update()
            return self.running

    # Returns the subset of running jobs which are in the codegen phase
    def getCodeGenJobs(self):
        running = self.getRunningJobs()
        subset  = set()
        for fn in running:
            if self.isCodeGen(fn,self.fdir):
                subset.add(fn)
        return subset

    # Returns the subset of running jobs which are in the integrate phase
    def getIntegrateJobs(self,cutoff=-1):
        running = self.getRunningJobs()
        subset = set()
        for fn in running:
            if self.isCodeGen(fn,self.fdir):
                continue
            t = self.getIntegrateTime(fn)
            if cutoff > -1 and t > cutoff:
                continue
            subset.add(fn)
        return subset

    # Checks for stuck jobs (Note: This only checks the .log file so won't catch jobs stuck in the CODEGEN phase)
    def getStuckJobs(self,cutoff):
        subset = set()
        if cutoff < 0:
            return subset
        running = self.getRunningJobs()
        for fn in running:
            t = self.getStuckTime(fn)
            if t > cutoff:
                subset.add(fn)
        return subset

    # Returns how long the job has been in the integrate phase
    def getIntegrateTime(self,fn):
        if not self.isJob(fn):
            return 0
        p,c,r = fn.split('_')
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        fpath1 = os.path.join(self.fdir,"{tag}_codegen.log".format(tag=tag_str))
        fpath2 = os.path.join(self.fdir,"{tag}.log".format(tag=tag_str))
        return self.getModifiedTimeDifference(fpath2,fpath1)

    # Returns time since the log file was last updated (relative to now)
    def getStuckTime(self,fn):
        if not self.isJob(fn):
            return 0
        p,c,r = fn.split('_')
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        fpath = os.path.join(self.fdir,"{tag}.log".format(tag=tag_str))
        return self.getLastModifiedTime(fpath)

    # Returns the time since the tarball file was last updated (relative to now)
    def getTarballTime(self,fn):
        if not self.isJob(fn):
            return 0
        p,c,r = fn.split('_')
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        fpath = os.path.join(self.fdir,"{tag}_{scram_arch}_{release}_tarball.tar.xz".format(tag=tag_str,scram_arch=self.scram_arch,release=self.cmssw_release))
        return self.getLastModifiedTime(fpath)

    # Returns the time the job spent in the codegen phase
    def getCodegenTime(self,fn):
        dt = 0
        if not self.isJob(fn):
            return dt
        p,c,r = fn.split('_')
        tag_str = "{proc}_{coeff}_{run}".format(proc=p,coeff=c,run=r)
        if fn in self.codegen:
            # The Job is still in the codegen phase --> use scanpoints file to determine time
            fpath = os.path.join(self.fdir,"{tag}_scanpoints.txt".format(tag=tag_str))
            dt = self.getLastModifiedTime(fpath)
        else:
            # The job is out of the codegen phase
            fpath1 = os.path.join(self.fdir,"{tag}_scanpoints.txt".format(tag=tag_str))
            fpath2 = os.path.join(self.fdir,"{tag}_codegen.log".format(tag=tag_str))
            dt = self.getModifiedTimeDifference(fpath2,fpath1)
        return dt

    # Returns the absolute time difference (in seconds) since last modification between two files
    def getModifiedTimeDifference(self,fpath1,fpath2):
        if not os.path.exists(fpath1) or not os.path.exists(fpath2):
            return 0
        fstats1 = os.stat(fpath1)
        fstats2 = os.stat(fpath2)
        return int(abs(fstats2.st_mtime - fstats1.st_mtime))

    # Returns the time (relative to now) since the file was last modified
    # NOTE: Should always return > 0
    def getLastModifiedTime(self,fpath):
        if not os.path.exists(fpath):
            return 0
        fstat = os.stat(fpath)
        tstamp = datetime.datetime.fromtimestamp(fstat.st_mtime)
        dt = datetime.datetime.now() - tstamp
        return (dt.days*3600*24 + dt.seconds)

    # Reads the last n lines from each of the jobs still in the integrate phase
    def checkProgress(self,lines=5):
        for fn in sorted(self.intg_full,key=self.getIntegrateTime):
            log_file = os.path.join(self.fdir,"%s.log" % (fn))
            if not os.path.exists(log_file):
                continue
            t = self.getLastModifiedTime("%s_scanpoints.txt" % (fn))
            h,m,s = self.formatTime(t)
            tot_tstr = "[%s:%s:%s]" % (h.rjust(2,"0"),m.rjust(2,"0"),s.rjust(2,"0"))
            t = self.getIntegrateTime(fn)
            h,m,s = self.formatTime(t)
            int_tstr = "[%s:%s:%s]" % (h.rjust(2,"0"),m.rjust(2,"0"),s.rjust(2,"0"))
            t = self.getLastModifiedTime(log_file)
            h,m,s = self.formatTime(t)
            mod_tstr = "[%s:%s:%s]" % (h.rjust(2,"0"),m.rjust(2,"0"),s.rjust(2,"0"))
            #print "\nChecking: %s - %s - %s" % (fn,int_tstr,mod_tstr)
            #print "\nChecking: %s - Total %s - Intg %s - LogMod %s" % (fn,tot_tstr,int_tstr,mod_tstr)
            print "\nChecking: %s - %s - %s - %s" % (fn,tot_tstr,int_tstr,mod_tstr)
            run_process(['tail','-n%d' % (lines),log_file])

    def displayJobList(self,s,arr):
        print "%s Jobs: %d" % (s,len(arr))
        for f in sorted(arr):
            print "\t%s" % (f)

    def showJobs(self,wl=[]):
        print "Last Update: %s" % (self.last_update)
        if len(wl) == 0:
            wl = self.getJobTypes()

        if len(self.resubmitted):
            print "Resubmitted Jobs:"
            for k,v in self.resubmitted.iteritems():
                print "\t%s: %d" % (k,v)

        if self.RUNNING in wl:
            self.displayJobList("Running",  self.running)
        if self.CODEGEN in wl:
            self.displayJobList("CodeGen",  self.codegen)
        if self.INTEGRATE in wl:
            self.displayJobList("Integrate",self.intg_full)
        if self.INTEGRATE_FILTER in wl:
            self.displayJobList("Integrate(f)",self.intg_filter)
        if self.STUCK in wl:
            self.displayJobList("Stuck",self.stuck)
        if self.FINISHED in wl:
            self.displayJobList("Finished", self.finished)

if __name__ == "__main__":
    curr_dir = os.getcwd()
    tracker = JobTracker(fdir=curr_dir)
    int_cutoff = 30*60
    stk_cutoff = 30*60
    tar_cutoff = 5*60
    tracker.setIntegrateCutoff(int_cutoff)
    tracker.setStuckCutoff(stk_cutoff)
    tracker.setTarballCutoff(tar_cutoff)
    tracker.update()
    job_list = [JobTracker.RUNNING,JobTracker.CODEGEN,JobTracker.INTEGRATE,JobTracker.INTEGRATE_FILTER,JobTracker.STUCK]
    tracker.showJobs(wl=job_list)
    tracker.checkProgress(lines=5)
    print "\nChecking finished jobs for failures:"
    for job in tracker.finished:
        if tracker.logHasError(job=job,fdir=curr_dir):
            print "\tFinished Job %s has error!" % (job)
        if not tracker.logHasXsec(job=job,fdir=curr_dir):
            print "\tFinished Job %s is missing xsec!" % (job)