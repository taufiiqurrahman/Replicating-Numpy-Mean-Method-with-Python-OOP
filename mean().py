import numpy as np 
data_uji = [20, 63, 87, 35, 84, 19, 45, 31, 64, 95]  
data_uji_numpy_clone = numpy_clone(data_uji) 
data_uji_numpy = np.array(data_uji) 
print("Banyak data :", len(data_uji)) 
print("Mean numpy_clone :", data_uji_numpy_clone.array_1d_mean()) 
print("Mean numpy library :", data uji_numpy.mean())