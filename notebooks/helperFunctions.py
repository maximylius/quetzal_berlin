# Notebook to store and load in helper functions
import sys
from shapely.geometry import LineString, Point


class helpers:

    # print progress to know where slow function is at 
    def printProgress(i, imax, t, t0, threshold = 0.01, flush=True):
        # round only once for each threshold*100% progress
        if((i+1) in list(map(lambda x: max(1,round(x * threshold * imax)), range(0, round(1 / threshold)+1)))):
            if(flush):
                sys.stdout.flush()
            p = 100 * + (i+1) / imax
            pr = round(p)
            s = '\r'
            s += ((pr if(pr>0) else 0) *"|") + ((100-pr if(100-pr>0) else 0)*"-")
            s += " " + str(round(pr)) + "%. "
            if(t):
                minElap = (t - t0)
                minRem = (100 - p) / p * (t - t0)
                s += "Minutes elapsed: " + str("%02d" % (minElap // 60)) + ":" + str("%02d" % round(minElap % 60)) + ". "
                s += "Minutes remaining: " +str("%02d" % (minRem // 60)) + ":" + str("%02d" % round(minRem % 60)) + ". "
            print(s, end='')

    # helper function to divide a line into segments from start to end point
    def segmentLine(l=LineString([(0,0),(1,1)]), i=0, nSteps=10):
        startPoint = Point(
            i/nSteps*l.coords[0][0] + (1-(i/nSteps)) * l.coords[-1][0],
            i/nSteps*l.coords[0][1] + (1-(i/nSteps)) * l.coords[-1][1]
        )
        i += 1
        endPoint = Point(
            i/nSteps*l.coords[0][0] + (1-(i/nSteps)) * l.coords[-1][0],
            i/nSteps*l.coords[0][1] + (1-(i/nSteps)) * l.coords[-1][1]
        )
        return LineString([startPoint, endPoint])

