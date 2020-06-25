class Matrix:
    def __init__(self, rws = 0, cols = 0):
        self.rws = rws
        self.cols = cols
        self.matrix = []
        self.columns = []
    def ini_matrix(self):
        if self.cols != 0:
            for i in range(0, self.rws):
                for i in range(0, self.cols):
                    self.columns.append(0)
                self.matrix.append(self.columns)
                self.columns = []
            return self.matrix
        else:
            for i in range(0, self.rws):
                self.matrix.append(0)
            return self.matrix
