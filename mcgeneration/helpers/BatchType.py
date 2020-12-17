class BatchType(object):
    LOCAL      = 'local'
    LSF        = 'lsf'
    CMSCONNECT = 'cmsconnect'
    CONDOR     = 'condor'
    NONE       = 'none'

    @classmethod
    def getTypes(cls):
        return [cls.LOCAL,cls.LSF,cls.CMSCONNECT,cls.CONDOR,cls.NONE]

    @classmethod
    def isValid(cls,btype):
        if not btype in cls.getTypes():
            raise ValueError("%s is not a valid batch type!" % (btype))
        return btype in cls.getTypes()  #TODO: Won't be needed once Gridpack class is implemented