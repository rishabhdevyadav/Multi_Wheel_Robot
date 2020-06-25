
import matplotlib.pyplot as plt
import itertools 
import numpy as np
import random

def findsubsets(s, n): 
	return list(itertools.combinations(s, n)) 


def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 

# Driver Code 
# s = [-2,-1,1, 2]
# enc = [120,130,140,100]


# Wheel Configuration is here
s = [-4,-3,-2,-1,0,1, 2, 3,4]

#encoder list
enc = random.sample(range(1000, 2500), len(s))

n = 4  # number of active agents
l1,x1,index2 =[],[],[]

a = (findsubsets(s, n)) 

if (len(s) % 2) != 0: 
	if (n%2) == 0:
		targetsum1,targetsum2 = 0,0
	else:
		targetsum1,targetsum2 = -1,1

	for i in range(0, len(a)):
		if sum(a[i]) == targetsum1 or sum(a[i]) == targetsum2 or sum(a[i]) == 0:
			l1.append(a[i])
			x = np.array(a[i])
			x1 = (np.absolute(x))
			
			if (n % 2) == 0:
				if len(Repeat(x1)) == (n)/2:
					print(a[i])
					l2 = a[i]
					index1 = []
					for j in range (0, len(l2)):
						index = s.index(l2[j])
						index1.append(index)

			else:
				if len(Repeat(x1)) == (n-1)/2:
					print(a[i])
					l2 = a[i]
					index1 = []
					for j in range (0, len(l2)):
						index = s.index(l2[j])
						index1.append(index)
					
			index2.append(index1) 

	l3 =[]
	for i in range (0, len(index2)):
		res_list = [enc[i] for i in index2[i]] 
		l3.append(sum(res_list))
	print(l3)
	print(min(l3))
	index = l3.index(min(l3)) 





if (len(s) % 2) == 0:  #if number of wheel are even

	if (n%2) == 0:
		targetsum1,targetsum2 = 0,0
	else:
		targetsum1,targetsum2 = -1,1

	for i in range(0, len(a)):
		if sum(a[i]) == targetsum1 or sum(a[i]) == targetsum2 or sum(a[i]) == 0:
			l1.append(a[i])
			x = np.array(a[i])
			x1 = (np.absolute(x))
			
			if (n % 2) == 0:
				if len(Repeat(x1)) == (n)/2 :
					print(a[i])
					l2 = a[i]
					index1 = []
					for j in range (0, len(l2)):
						index = s.index(l2[j])
						index1.append(index)

			else:
				if len(Repeat(x1)) == (n-1)/2 :  #for odd n
					print(a[i])
					l2 = a[i]
					index1 = []
					for j in range (0, len(l2)):
						index = s.index(l2[j])
						index1.append(index)
					#print(index1)
			index2.append(index1) 

	l3 =[]
	for i in range (0, len(index2)):
		res_list = [enc[i] for i in index2[i]] 
		l3.append(sum(res_list))
	
	index = l3.index(min(l3)) 

   
print(index2[index])
print(l1[index])


# xaxis = l1[index]
# yaxis = [1]*len(xaxis)
# plt.ylim(0,2)
# # plot the index for the x-values
# plt.plot(xaxis, yaxis, marker='s', linestyle='--', color='r', label='Active_wheel_position') 
# plt.xlabel('wheel number')
# plt.ylabel('y') 
# plt.title(enc)
# plt.legend() 
# plt.show()
 
xaxis = l1[index]
plt.ylim(0,1)
# plot the index for the x-values
plt.plot(xaxis, [0.6]*len(xaxis), marker='s', linestyle='--', color='r', label='Active_wheel_position')
plt.plot(s , [0.4]*len(s), marker='o', linestyle='--', color='g', label='Wheel_position')
plt.xlabel('wheel number')
plt.ylabel('y') 
plt.title('Encoder Count '+ str(enc))
plt.grid(True)
plt.legend() 
plt.show()