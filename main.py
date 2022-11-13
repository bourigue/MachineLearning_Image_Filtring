from scipy import misc
import matplotlib.pyplot as plt
import numpy
face=misc.face()
arr=numpy.array(face)
arr[::2,::2]+=100
plt.imshow(arr)