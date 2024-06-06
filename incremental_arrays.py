import numpy as np

# creating incremental arrays

a_range = np.arange(0,10,1) # parameters: x (start), y (end), z (increment (optional), default is zero)
print(a_range) # np.arange doesn't include the 10

a_linspace = np.linspace(0,10,11) # parameters: x (start), y (end), z (number of points)
print(a_linspace) # includes the 10

a_logspace = np.logspace(0,2,5) # generate an array with logarithmically distributed values between 1 and 100
print(a_logspace) # 5 data points between 10**0=1 to 10**2=100
