def findSolution(self, customfunction, z):
        res = []
        y = 1000
        for x in xrange(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res