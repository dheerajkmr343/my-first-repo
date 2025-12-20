# import numpy
# a = [11, 55, 87, 61, 46, 44, 52, 98]
# aa = numpy.array(a)
# print(aa)
# print(type(aa))


import numpy as np
# z = np.array([1,2,3,4,5,6])
# print(z)

# zerodim = np.array(1)
# print(zerodim.ndim)
onedim = np.array([11,22,33,445,789])
# print(onedim.ndim)
# twodim = np.array([[78,65,44,96,36],[78,69,36,11,69]])
# print(twodim.ndim)
# print(twodim[0][1])


array = np.array([44,98,15,69,78,36,71,98,14])
print(np.array_split(array,3))


d = np.array([44,98,15,69,78,36,71,98,14])
print(np.array_split(d,3))



a = np.array([44,98,15,69,78,36,71,98,14])
print(np.array_split(a,2))