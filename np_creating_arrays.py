import numpy as np

print('='*(130-17))
print('--> using np.array\n')

a = np.array([1,2,3],dtype=np.int32) # can be initialized with a generic list
b = np.array((1,2,3),dtype=np.int32) # can be initialized with a generic tuple
c = np.array([i for i in range(10)],dtype=np.int32) # can be initialized with a list comprehension
d = np.array(tuple(i for i in range(10)),dtype=np.int32) # can be initialized with a tuple comprehension
e = np.array(list(dict(a=1,b=2,c=3).values()),dtype=np.int32) # can be initialized with the values of a dictionary
f = np.array(list({'a':1,'b':2,'c':3}.values()),dtype=np.int32) # same as the above
g = np.array('hello,world,python,spam'.split(','),dtype='<U5') # with strings using split
h = np.array(['hello','world','python','spam'],dtype='<U5') # normal list of strings
j = np.array('hello world') # normal string
k = np.linspace(0,10,num=100) # linspace creates an array of some type staring with a start and ending with an end, num specifies the total amount of elements
l = np.array(k) # or using other ndarray objects

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(h)
print(g)
print(j)
print(k)
print(l)

m = np.array([1,2,3,4])
print(m)
print(m.ndim, np.ndim(m))
print(m.shape, np.shape(m))
print(m.size, np.size(m))

n = np.array([[1,2],[3,4]]) # create a two dimensional array 2 x 2
print(n)
print(n.ndim, np.ndim(n))
print(n.shape, np.shape(n))
print(n.size, np.size(n))

print('='*(130-17))
print('--> arrays filled with constant values 1s and 0s\n')

o = np.zeros(10) # create a flat array of 0 elements the size of 10
print(o)
p = np.zeros((5,2),dtype=np.int32) # create a 5 x 2 array of 0 elements the size of 10, type specified by dtype
print(p)

q = np.zeros((5,3,5),dtype=np.int32) # likewise, but a three dimensional array (5,3,5)
print(q)

# same operations apply to np.ones()
r = np.ones(10)
print(r)

s = np.ones((5,2),dtype=np.int32)
print(s)

t = np.ones((5,3,5),dtype=np.int32) 
print(t)

u = np.ones(10)
print(u * 5.4, 5.4 * u) # order doesn't matter

#or 

v = np.full(10,5.4)
print(v)

w = np.full((5,2,2),10.67) # same but 2 dimensional or 3 dimensional
print(w)

x1 = np.empty(5) # np.empty creates an array of size 5 filled with random arbitrary values
# or np.empty((5,)) or np.empty((2,3))
x1.fill(9.5) # fill() replaces all the values in the array with the specified value 9.5
print(x1)

x2 = np.array([[1,2,3],[2,3,4],[3,4,5]])
x2.fill(1.1)

print(x2)