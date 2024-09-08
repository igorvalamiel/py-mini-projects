import numpy as np

a = np.array([[0,0,0,0], [1,1,1,1], [2,2,2,2]])

a[0, :] = a[0,:] - (a[1,:] + a[2,:])
print(a)

a = np.delete(a, 1,0)
print(a)