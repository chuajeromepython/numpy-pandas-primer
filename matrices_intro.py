import numpy as np

# creating matrices

x = 3
identity_mat = np.identity(x) # parameter x specifies the number of 1s on the diagonal
print(identity_mat)

eye = np.eye(x,k=1) # similar to np.identity: paremeter x specifies the dimension of the array (3 x 3) and k specifies the offset of the diagonal (0 is default)
# negative k makes a reversed diagonal
print(eye)

a_linspace = np.linspace(1,10,10)
diag = np.diag(a_linspace) # np.diag works the same way, but it puts a 1d array on the diagonal
print(diag)
