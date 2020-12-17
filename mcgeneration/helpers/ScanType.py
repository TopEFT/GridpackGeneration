import random

from helper_tools import linspace, check_point

class ScanType(object):
    FRANDOM   = 'full_random'
    SRANDOM   = 'axis_random'
    FLINSPACE = 'full_linspace'
    SLINSPACE = 'axis_linspace'
    FROMFILE  = 'from_file'
    NONE      = 'none'

    @classmethod
    def getTypes(cls):
        return [cls.FRANDOM,cls.SRANDOM,cls.FLINSPACE,cls.SLINSPACE,cls.FROMFILE,cls.NONE]

    @classmethod
    def isValid(cls,stype):
        if not stype in cls.getTypes():
            raise ValueError("%s is not a valid scan type!" % (stype))
        return stype in cls.getTypes() #TODO: Won't be needed once Gridpack class is implemented

    @classmethod
    def getPoints(cls,dofs,num_pts,stype):
        pts = []
        if stype == cls.FLINSPACE:
            # Full scan of phase space using a linear grid spacing
            pts = cls.fullScanLinear(dofs,num_pts)
        elif stype == cls.FRANDOM:
            # Full scan of phase space using random sampling of the entire phase space
            pts = cls.fullScanRandom(dofs,num_pts)
        elif stype == cls.SLINSPACE:
            # Axis scan (no xterms) with linear spacing along the axis
            pts = cls.axisScanLinear(dofs,num_pts)
        elif stype == cls.SRANDOM:
            # Axis scan (no xterms) with random sampling along the axis
            cls.axisScanRandom(dofs,num_pts)
        elif stype == cls.FROMFILE or stype == cls.NONE:
            pts = []
        return pts

    @classmethod
    def fullScanLinear(cls,dofs,npts):
        """ Generate a list of n-D points for all DoFs using a grid scan. Will generate npts^N total
            reweight points. This list of points is suitable for fitting an n-D quadratic.
        """
        pts_arr = []
        if npts == 0:
            return pts_arr
        sm_pt = {}
        start_pt = {}
        coeffs = dofs.keys()
        arr = []
        for c in coeffs:
            sm_pt[c] = 0.0
            start_pt[c] = dofs[c].getStart()
            arr += [linspace(dofs[c].getLow(),dofs[c].getHigh(),npts)]
        has_sm_pt = check_point(sm_pt,start_pt)
        mesh_pts = [a for a in itertools.product(*arr)]
        for rwgt_pt in mesh_pts:
            pt = {}
            for idx,c in enumerate(coeffs):
                pt[c] = round(rwgt_pt[idx],6)
            if check_point(pt,sm_pt):
                # Skip SM point
                has_sm_pt = True
            if check_point(pt,start_pt):
                # Skip starting point
                continue
            pts_arr.append(pt)
        if not has_sm_pt:
            pts_arr.append(sm_pt)
        return pts_arr

    @classmethod
    def fullScanRandom(cls,dofs,npts):
        """ Generate a list of n-D points for all DoFs sampled uniformly from the n-D space.
            Will generate exactly npts reweight points. This list of points is suitable for fitting
            an n-D quadratic
        """
        pts_arr = []
        if npts == 0:
            return pts_arr
        sm_pt = {}
        start_pt = {}
        coeffs = dofs.keys()
        for c in coeffs:
            sm_pt[c] = 0.0
            start_pt[c] = dofs[c].getStart()
        has_sm_pt = check_point(sm_pt,start_pt)
        for idx in range(npts):
            pt = {}
            for c in coeffs:
                pt[c] = round(random.uniform(dofs[c].getLow(),dofs[c].getHigh()),6)
            if check_point(pt,sm_pt):
                has_sm_pt = True
            if check_point(pt,start_pt):
                continue
            pts_arr.append(pt)
        if not has_sm_pt:
            pts_arr.append(sm_pt)
        return pts_arr

    @classmethod
    def axisScanLinear(cls,dofs,npts):
        """ Generate a list of 1-D points with linear spacing. Will generate N*npts reweight points.
            This list of point is only suitable for fitting 1-D quadratics as it will not include
            any points involving cross terms.
        """
        pts_arr = []
        if npts == 0:
            return pts_arr
        sm_pt = {}
        start_pt = {}
        coeffs = dofs.keys()
        for c in coeffs:
            sm_pt[c] = 0.0
            start_pt[c] = dofs[c].getStart()
        has_sm_pt = check_point(sm_pt,start_pt)
        for c1 in coeffs:
            arr = linspace(dofs[c1].getLow(),dofs[c1].getHigh(),npts)
            for v in arr:
                pt = {}
                for c2 in coeffs:
                    if c1 == c2:
                        pt[c2] = round(v,6)
                    else:
                        pt[c2] = 0.0
                if check_point(pt,sm_pt):
                    has_sm_pt = True
                if check_point(pt,start_pt):
                    continue
                pts_arr.append(pt)
        if not has_sm_pt:
            pts_arr.append(sm_pt)
        return pts_arr

    @classmethod
    def axisScanRandom(cls,dofs,npts):
        """ Generate a list of 1-D points sampled uniformly. Will generate N*npts reweight points.
            This list of point is only suitable for fitting 1-D quadratics as it will not include
            any points involving cross terms.
        """
        pts_arr = []
        if npts == 0:
            return pts_arr
        sm_pt = {}
        start_pt = {}
        coeffs = dofs.keys()
        for c in coeffs:
            sm_pt[c] = 0.0
            start_pt[c] = dofs[c].getStart()
        has_sm_pt = check_point(sm_pt,start_pt)
        for c1 in coeffs:
            for idx in range(npts):
                pt = {}
                v = random.uniform(dofs[c1].getLow(),dofs[c1].getHigh())
                for c2 in coeffs:
                    if c1 == c2:
                        pt[c2] = round(v,6)
                    else:
                        pt[c2] = 0.0
                if check_point(pt,sm_pt):
                    has_sm_pt = True
                if check_point(pt,start_pt):
                    continue
                pts_arr.append(pt)
        if not has_sm_pt:
            pts_arr.append(sm_pt)
        return pts_arr
