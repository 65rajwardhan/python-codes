#numpy
#array in numpy
#create numarray
import numpy as np
arr=np.array([10,20,30])
print(arr)

#####################
#creating multi-dimenstion array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

#represent minimum dimensions
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

#change data type
arr=np.array([10,20,30],dtype=complex)
print(arr)

#get dimension of array
arr=np.array([[1,2,3,4],[5,6,7,8],[55,34,23,45]])
print(arr.ndim)
print(arr)

######################
#finding size of each item in the array
arr=np.array([10,20,30])
print("each item contain in bytes:",arr.itemsize)

#array datatype
arr=np.array([10,20,30])
print("each item is of type:",arr.dtype)

#get shape and size of array
arr=np.array([[10,20,30,45],[55,40,50,60]])
print("array size",arr.size)
print("array shape",arr.shape)

#create array for list with type float
arr=np.array([[10,20,30],[40,50,60]],dtype='float')
print('array created by using list',arr)

#############################
#create sequence of int using array
arr=np.arange(0,20,3)
print("a sequential array with steps of 3 \n",arr)

###############################
#array indexing in numpy
arr=np.arange(11)
print(arr)

print(arr[2])

print(arr[2])

print(arr[-2])

#####################3
#multiple dimension array indexing
arr=np.array([[10,20,30,40,50],[60,70,80,30,40]])
print(arr)

print(arr.shape)

print(arr[1,1])

print(arr[0,4])

print(arr[1,-1])

#########################
#accessing array element using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)

x=arr[-2:3:-1]
print(x)

x=arr[-2:10]
print(x)

########################
#indexing in numpy
import numpy as np
multi_arr=np.array([[10,20,30,40,50],[60,70,80,30,40],[44,66,77,88,89],[11,23,43,54,45]])
multi_arr

multi_arr [1,2]

multi_arr [1,:]

multi_arr [:,1]

x=multi_arr[:3,::2]
print(x)

#############################
#integer array indexing
arr=np.arange(35).reshape(5,7)
print(arr)

##########################3
#boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True])
rows
wanted_rows=arr[rows,:]
print(wanted_rows)

rows=np.array([True,False,True])
rows
wanted_rows=arr[rows,:]
print(wanted_rows)

################################
list=[20,40,60,80]
array=np.asarray(list)
print("array:",array)
print(type(array))

##########################

#properties of ndarray
#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

################
#resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)

#######################
#numpy reshape
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)

###############################
#apply arithmatic oeration on numpy array
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,3,2,4])

#add
add_arr=np.add(arr1,arr2)
print(f"adding two arrays:\n{add_arr}")

#sub
sub_arr=np.subtract(arr1,arr2)
print(f"subtracting two arrays:\n{sub_arr}")

#multiplication
mul_arr=np.multiply(arr1,arr2)
print(f"multiplying two arrays:\n{mul_arr}")
 
#divide
div_arr=np.divide(arr1,arr2)
print(f"dividing two arrays:\n{div_arr}")

#reciprocal
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"after applying reciprocal function:\n{rep_arr1}")

###############################
#numpy power operation
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"after applying power function:\n{pow_arr1}")

###########################
arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("my second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"after applying power function:\n{pow_arr2}")

###################################3
#to perform mod function
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr=np.mod(arr1,arr2)
print(f"after applying mod function:\n{mod_arr}")

#############################3
#create empty array
from numpy import empty
a=empty([3,3])
print(a)

################################
#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)

##############################
#create one array
from numpy import ones
a=ones([5])
print(a)

##############################
#create array with vstack
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
print(a1)
#create seond array
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)

########################3
#create array with hstack
from numpy import array
from numpy import hstack
#create first array
a1=array([1,2,3])
print(a1)
#create seond array
a2=array([4,5,6])
print(a2)
#create horizontal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)

###########################
###############
#######
##
#
from numpy import array
data=array([
[11,22],
[33,44],
[55,66]])
print(data[0,])

#slicing one dimensional array
from numpy import array
data=array([11,22,44,55,66])
print(data[1:4])

#negative slicing
data=array([11,22,33,44,55])
print(data[-2:])

#########################
#split input and output data
from numpy import array
data=array([
[11,22,77],
[33,44,88],
[55,66,99]])
#seperate data
X,y=data[:,:-1],data[:,-1]
X
y

###########################
#broadcast scalar to one dimensional array
from numpy import array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b
print(c)

###############################
#l1 norm is calculated as the sum of the  asolute vector values
from numpy import array
from numpy.linalg import norm
a=array([1,2,3])
print(a)
l1=norm(a,1)
print(l1)

#l2 norm is used to calculate square root 
#of sum of the squared vector values
#also used to calculate errors in machine learning module
from numpy import array
from numpy.linalg import norm
a=array([1,2,3])
print(a)
l2=norm(a)
print(l2)

#########################
#triangular matrix
from numpy import array
from numpy import tril
from numpy import triu
#definr square matrix
M=array([
    [11,22,77],
    [33,44,88],
    [55,66,99]])
print(M)
#lower triangular matrix
lower=tril(M)
print(lower)
#upper triangular matrix
upper=triu(M)
print(upper)

#####################
#digonal matrix
from numpy import array
from numpy import diag
M=array([
    [11,22,77],
    [33,44,88],
    [55,66,99]])
print(M)

d=diag(M)
print(d)

D=diag(d)
print(D)

#identity matrix
from numpy import identity
I=identity(3)
print(I)

#orthogonal matrix
from numpy import array
from numpy.linalg import inv
Q=array([
    [1,0],
    [0,-1]])
print(Q)
#inverse equivalence
V=inv(Q)
print(Q.T)
print(V)
#identity equivalence
I=Q.dot(Q.T)
print(I)

####################################
#transpose of matrix
from numpy import array
A=array([
    [1,0],
    [3,4],
    [5,6]])
print(A)

C=A.T 
print(C)

#inverse matrix
from numpy import array
from numpy.linalg import inv
A=array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)

B=inv(A)
print(B)

#multiply a and b
I=A.dot(B)
print(I)

#################
#sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
A=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)

S=csr_matrix(A)
print(S)

B=S.todense()
print(B)

###################################
