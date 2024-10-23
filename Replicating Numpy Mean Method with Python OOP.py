class numpy_clone:
    def init(self, data):
        self.data = data
    def array_ld_mean(self):
        return sum(self.data)/len(self.data)
    def array_2d_mean(self, axis=None):
        if axis == None:
            sum_data = 0
            num_of_data = len(self.data)*len(self.data[6])
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    sum_data += self.data[i][j]
            return sum_data/num_of_data
        elif axis == 0:
            mean = []
            for j in range(len(self.data[0])):
                sum_data = 0
                for i in range(len(self.data)):
                    sum_data += self.data[i][j]
                mean.append(sum_data/len(self.data))
            return mean
        elif axis == 1:
            mean = []
            for i in range(len(self,data)):
                sum_data sum(self.data[i])
                mean_of_each_row = sum_data / len(self.data[i])
                mean.append(mean_of_each_row)
            return mean
        else:
            raise ValueError("Axis has to be None, 0, or 1")