import numpy as np

# meshgrid arrays
# given two 1d arrays, meshgrid will produce two 2D arrays representing all combinations of these coordinates

x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X,Y = np.meshgrid(x,y) # returns a tuple of two 2d arrays, each one captured by X and Y
print(X) # [[-1,0,1],[-1,0,1],[-1,0,1]]
print(Y) #[[-2,-2,-2],[0,0,0],[2,2,2]]

Z = (X + Y) ** 2 # adding both arrays and raising each sum to 2
print(Z)
