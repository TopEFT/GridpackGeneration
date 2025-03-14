class DegreeOfFreedom(object):
    def __init__(self,name,relations=[]):
        self.name = name
        self.relations = {}
        self.limits = [0,None,None]

        if len(relations) == 2:
            self.setCoefficient(relations[0],relations[1])

    def getName(self):
        return self.name

    def getCoefficients(self):
        return self.relations.keys()

    def getStart(self):
        return self.limits[0]

    def getLow(self):
        return self.limits[1]

    def getHigh(self):
        return self.limits[2]

    def setCoefficient(self,wc_names,scale):
        for wc in wc_names:
            self.relations[wc] = scale

    def setLimits(self,start,low,high):
        self.limits = [start,low,high]

    def hasLimits(self):
        return not (self.getLow() is None or self.getHigh() is None)

    def popCoefficient(self,wc_name):
        return self.relations.pop(wc_name,None)

    def eval(self,x):
        output = {}
        for wc,scale in self.relations.items():
            if x*scale == 0.0:
                output[wc] = 0.0
            else:
                output[wc] = x*scale
        return output

    def getCouplingString(self):
        s = "FCNC=0 DIM6^2==1"
        for k in self.relations.keys():
            s += " DIM6_%s^2==1" % (k)
        return s


# cQDW = 1.0*cQj13 = 1.0*cQl3(l)
# cQDB = 6.0*cQj11 = 1.5*cQu1 = -3.0*cQd1 = -3.0*cQb1 = -2.0*cQlM(l) = -1.0*cQe(l)
# ctDB = 6.0*ctj1  = 1.5*ctu1 = -3.0*ctd1 = -3.0*ctb1 = -2.0*ctl(l)  = -1.0*cte(l)
# cQDG = 1.0*cQj18 = 1.0*cQu8 =  1.0*cQd8 =  1.0*cQb8  **NOT SURE ABOUT cQj18**
# ctDG = 1.0*ctj8  = 1.0*ctu8 =  1.0*ctd8 =  1.0*ctb8

#ANALYSIS_COEFFS = [ # As suggested by Adam
#    'ctH','cpQM','cpQ3','cHtb','cHtbRe','ctWRe', 'ctBRe', 'cbWRe','ctG',
#    'cQl31','cQlM1','cQe1','ctl1','cte1','ctlS1','ctlT1',
#    'cQl32','cQlM2','cQe2','ctl2','cte2','ctlS2','ctlT2',
#    'cQl33','cQlM3','cQe3','ctl3','cte3','ctlS3','ctlT3',
#]

#TOP_PHILIC_COEFFS = [
#    'ctH','cpQM','cpQ3','cHtb','cHtbRe','ctWRe', 'ctBRe', 'cbWRe','ctG', # 9 two-heavy quark + bosons
#    'cQQ1','cQQ8','cQt1','cQt8','ctt1',                         # 5 four heavy quarks
#]

if __name__ == "__main__":
    ctHRe    = DegreeOfFreedom(name='ctHRe'  ,relations=[['ctHRe'] ,1.0])
    cHQ1     = DegreeOfFreedom(name='cHQ1' ,relations=[['cHQ1'],1.0])
    cHQ3     = DegreeOfFreedom(name='cHQ3' ,relations=[['cHQ3'],1.0])
    cHt      = DegreeOfFreedom(name='cHt'  ,relations=[['cHt'] ,1.0])
    cHtbRe   = DegreeOfFreedom(name='cHtbRe' ,relations=[['cHtbRe'],1.0])
    ctWRe    = DegreeOfFreedom(name='ctWRe',relations=[['ctWRe'] ,1.0])
    ctBRe    = DegreeOfFreedom(name='ctBRe',relations=[['ctBRe'] ,1.0])
    cbWRe    = DegreeOfFreedom(name='cbWRe'  ,relations=[['cbWRe'] ,1.0])
    ctGRe    = DegreeOfFreedom(name='ctGRe',relations=[['ctGRe'] ,1.0])
    cQe      = DegreeOfFreedom(name='cQe' ,relations=[['cQe'],1.0])
    ctl      = DegreeOfFreedom(name='ctl' ,relations=[['ctl'],1.0])
    cte      = DegreeOfFreedom(name='cte' ,relations=[['cte'],1.0])
    cQl3     = DegreeOfFreedom(name='cQl3',relations=[['cQl3'],1.0])
    cQl1     = DegreeOfFreedom(name='cQl1',relations=[['cQl1'],1.0])
    cleQt1Re = DegreeOfFreedom(name='cleQt1Re',relations=[['cleQt1Re'],1.0])
    cleQt3Re = DegreeOfFreedom(name='cleQt3Re',relations=[['cleQt3Re'],1.0])
    ctp   = DegreeOfFreedom(name='ctp'  ,relations=[['ctp'] ,1.0])
    cpQM  = DegreeOfFreedom(name='cpQM' ,relations=[['cpQM'],1.0])
    cHQ1  = DegreeOfFreedom(name='cHQ1' ,relations=[['cHQ1'],1.0])
    cpQ3  = DegreeOfFreedom(name='cpQ3' ,relations=[['cpQ3'],1.0])
    cHQ3  = DegreeOfFreedom(name='cHj3' ,relations=[['cHj3'],1.0])
    cpt   = DegreeOfFreedom(name='cpt'  ,relations=[['cpt'] ,1.0])
    cHt   = DegreeOfFreedom(name='cHt'  ,relations=[['cHt'] ,1.0])
    cptb  = DegreeOfFreedom(name='cptb' ,relations=[['cptb'],1.0])
    ctW   = DegreeOfFreedom(name='ctW'  ,relations=[['ctW'] ,1.0])
    ctWRe = DegreeOfFreedom(name='ctWRe',relations=[['ctWRe'] ,1.0])
    ctZ   = DegreeOfFreedom(name='ctZ'  ,relations=[['ctZ'] ,1.0])
    ctBRe = DegreeOfFreedom(name='ctBRe',relations=[['ctBRe'] ,1.0])
    cbW   = DegreeOfFreedom(name='cbW'  ,relations=[['cbW'] ,1.0])
    ctG   = DegreeOfFreedom(name='ctG'  ,relations=[['ctG'] ,1.0])
    ctGRe = DegreeOfFreedom(name='ctGRe',relations=[['ctGRe'] ,1.0])
    cQei  = DegreeOfFreedom(name='cQei' ,relations=[['cQe1','cQe2','cQe3'],1.0])
    ctli  = DegreeOfFreedom(name='ctli' ,relations=[['ctl1','ctl2','ctl3'],1.0])
    ctei  = DegreeOfFreedom(name='ctei' ,relations=[['cte1','cte2','cte3'],1.0])
    cQl3i = DegreeOfFreedom(name='cQl3i',relations=[['cQl31','cQl32','cQl33'],1.0])
    cQlMi = DegreeOfFreedom(name='cQlMi',relations=[['cQlM1','cQlM2','cQlM3'],1.0])
    ctlSi = DegreeOfFreedom(name='ctlSi',relations=[['ctlS1','ctlS2','ctlS3'],1.0])
    ctlTi = DegreeOfFreedom(name='ctlTi',relations=[['ctlT1','ctlT2','ctlT3'],1.0])
    
    # Four heavy quarks
    cQQ1   = DegreeOfFreedom(name='cQQ1'   ,relations=[['cQQ1'],1.0])
    cQQ8   = DegreeOfFreedom(name='cQQ8'   ,relations=[['cQQ8'],1.0])
    cQt1   = DegreeOfFreedom(name='cQt1'   ,relations=[['cQt1'],1.0])
    cQt8   = DegreeOfFreedom(name='cQt8'   ,relations=[['cQt8'],1.0])
    cQb1   = DegreeOfFreedom(name='cQb1'   ,relations=[['cQb1'],1.0])
    cQb8   = DegreeOfFreedom(name='cQb8'   ,relations=[['cQb8'],1.0])
    ctt    = DegreeOfFreedom(name='ctt'    ,relations=[['ctt'],1.0])
    ctt1   = DegreeOfFreedom(name='ctt1'   ,relations=[['ctt1'],1.0])
    ctb1   = DegreeOfFreedom(name='ctb1'   ,relations=[['ctb1'],1.0])
    cQtQb1 = DegreeOfFreedom(name='cQtQb1' ,relations=[['cQtQb1'],1.0])

    ################################################################################################

    cQDW = DegreeOfFreedom(name='cQDW')
    cQDW.setCoefficient(['cQj31','cQl31','cQl32','cQl33'],1.0)

    cQDB = DegreeOfFreedom(name='cQDB')
    cQDB.setCoefficient(['cQj11'],6.0)
    cQDB.setCoefficient(['cQu1'],1.5)
    cQDB.setCoefficient(['cQd1','cQb1'],-3.0)
    cQDB.setCoefficient(['cQlM1','cQlM2','cQlM3'],-2.0)
    cQDB.setCoefficient(['cQe1','cQe2','cQe3'],-1.0)

    ctDB = DegreeOfFreedom(name='ctDB')
    ctDB.setCoefficient(['ctj1'],6.0)
    ctDB.setCoefficient(['ctu1'],1.5)
    ctDB.setCoefficient(['ctd1','ctb1'],-3.0)
    ctDB.setCoefficient(['ctl1','ctl2','ctl3'],-2.0)
    ctDB.setCoefficient(['cte1','cte2','cte3'],-1.0)

    cQDG = DegreeOfFreedom(name='cQDG')
    cQDG.setCoefficient(['cQj18','cQu8','cQd8','cQb8'],1.0)

    ctDG = DegreeOfFreedom(name='ctDG')
    ctDG.setCoefficient(['ctj8','ctu8','ctd8','ctb8'],1.0)

    ctp   = DegreeOfFreedom(name='ctp',relations=[['ctp'],1.0])
    cpQM  = DegreeOfFreedom(name='cpQM',relations=[['cpQM'],1.0])
    cHQ1  = DegreeOfFreedom(name='cHQ1',relations=[['cHQ1'],1.0])
    cpQ3  = DegreeOfFreedom(name='cpQ3',relations=[['cpQ3'],1.0])
    cHQ3  = DegreeOfFreedom(name='cHQ3',relations=[['cHQ3'],1.0])
    cpt   = DegreeOfFreedom(name='cpt',relations=[['cpt'],1.0])
    cHt   = DegreeOfFreedom(name='cHt',relations=[['cHt'],1.0])
    cptb  = DegreeOfFreedom(name='cptb',relations=[['cptb'],1.0])
    ctW   = DegreeOfFreedom(name='ctW',relations=[['ctW'],1.0])
    ctWRe = DegreeOfFreedom(name='ctWRe',relations=[['ctWRe'],1.0])
    ctZ   = DegreeOfFreedom(name='ctZ',relations=[['ctZ'],1.0])
    ctBRe = DegreeOfFreedom(name='ctBRe',relations=[['ctBRe'],1.0])
    cbW   = DegreeOfFreedom(name='cbW',relations=[['cbW'],1.0])
    ctG   = DegreeOfFreedom(name='ctG',relations=[['ctG'],1.0])
    ctGRe = DegreeOfFreedom(name='ctGRe',relations=[['ctGRe'],1.0])
    cQQ1  = DegreeOfFreedom(name='cQQ1',relations=[['cQQ1'],1.0])
    cQQ8  = DegreeOfFreedom(name='cQQ8',relations=[['cQQ8'],1.0])
    cQt1  = DegreeOfFreedom(name='cQt1',relations=[['cQt1'],1.0])
    cQt8  = DegreeOfFreedom(name='cQt8',relations=[['cQt8'],1.0])
    ctt1  = DegreeOfFreedom(name='ctt1',relations=[['ctt1'],1.0])

    cQl3i = DegreeOfFreedom(name='cQl3i',relations=[['cQl31','cQl32','cQl33'],1.0])
    cQlMi = DegreeOfFreedom(name='cQlMi',relations=[['cQlM1','cQlM2','cQlM3'],1.0])
    cQei  = DegreeOfFreedom(name='cQei',relations=[['cQe1','cQe2','cQe3'],1.0])
    ctli  = DegreeOfFreedom(name='ctli',relations=[['ctl1','ctl2','ctl3'],1.0])
    ctei  = DegreeOfFreedom(name='ctei',relations=[['cte1','cte2','cte3'],1.0])
    ctlSi = DegreeOfFreedom(name='ctlSi',relations=[['ctlS1','ctlS2','ctlS3'],1.0])
    ctlTi = DegreeOfFreedom(name='ctlTi',relations=[['ctlT1','ctlTi','ctlTi'],1.0])

    ################################################################################################

    cQDW = DegreeOfFreedom(name='cQDW')
    cQDW.setCoefficient(['cQq13','cQl31','cQl32','cQl33'],1.0)

    cQDB = DegreeOfFreedom(name='cQDB')
    cQDB.setCoefficient(['cQq11'],6.0)
    cQDB.setCoefficient(['cQu1'],1.5)
    cQDB.setCoefficient(['cQd1','cQb1'],-3.0)
    cQDB.setCoefficient(['cQlM1','cQlM2','cQlM3'],-2.0)
    cQDB.setCoefficient(['cQe1','cQe2','cQe3'],-1.0)

    ctDB = DegreeOfFreedom(name='ctDB')
    ctDB.setCoefficient(['ctq1'],6.0)
    ctDB.setCoefficient(['ctu1'],1.5)
    ctDB.setCoefficient(['ctd1','ctb1'],-3.0)
    ctDB.setCoefficient(['ctl1','ctl2','ctl3'],-2.0)
    ctDB.setCoefficient(['cte1','cte2','cte3'],-1.0)

    cQDG = DegreeOfFreedom(name='cQDG')
    cQDG.setCoefficient(['cQq81','cQu8','cQd8','cQb8'],1.0)

    ctDG = DegreeOfFreedom(name='ctDG')
    ctDG.setCoefficient(['ctq8','ctu8','ctd8','ctb8'],1.0)
