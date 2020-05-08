# iterated determinstic multiple affine transformation based random processing 
# currently #affine=1


# rule 
import numpy as np 
import random 
import matplotlib.pyplot as plt

# rule
def rule1(A1, A2, A3, A0): 
	[x_1, y_1] = A1
	[x_2, y_2] = A2
	[x_3, y_3] = A3
	[x_0, y_0] = A0
	p = 1/3
	# k=1 output 
	random.choices(population=[1,2,3],weights=[p, p, p], k=1)
	if i==1: 
		x_i = x_1
		y_i = y_1
	if i==2:
		x_i = x_2
		y_i = y_2
	if i==3: 
		x_i = x_3
		y_i = y_3 

	x = (x_0 + x_i)/2
	y = (y_0 + y_i)/2
	return x, y



# initial 3 points
# --------------------------------------------------
result = np.empty()
# randomly pick up a point
A0 = [x_0, y_0] = np.random.rand((1,2))
# Triange frame
A1 = [x_1, y_1] = [0,0]
A2 = [x_2, y_2] = [3,0]
A3 = [x_3, y_3] = [3/2, 3]

# record all new location of (x,y)
# --------------------------------------------------
x,y = rule1(A1, A2, A3, A0)
np.concatenate((result, [x,y]))


# plot
# --------------------------------------------------
x_new = result[:,[0]]
y_new = result[:,[1]]
plt.title("Siepinski Triangle") 
plt.xlabel("x axis ") 
plt.ylabel("y axis p") 
plt.plot(x_new,y_new) 
plt.show()



# i = np.random.randint(1,3,)
# from numpy.random import choice
# draw = choice([1,2,3]], 1,p=probability_distribution)



