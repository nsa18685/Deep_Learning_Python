class MyStats:

    def __init__(self):
        pass

    def mean(self, args):
        return sum(args) / len(args)

    def variance(self, args):
        re = 0
        m = self.mean(args)
        n = len(args)

        for i in args:
            re += (i - m) ** 2

        return re / (n - 1)

    def stddev(self, args):
        import math
        return math.sqrt(self.variance(args))

    def median(self, args):
        import numpy as np
        return np.median(args)

    def mode(self, args):
        from collections import Counter
        cnt = Counter(args)
        return cnt.most_common()

    def my_range(self, args):
        return max(args) - min(args)

    def box_range(args):
        import numpy as np
        return np.percentile(args, 75) - np.percentile(args, 25)