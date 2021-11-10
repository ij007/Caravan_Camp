'''
By: Anushka Singh
'''

from math import sqrt
from numpy import array 
from matplotlib.pyplot import plot, show, axis

# We can think of each point as a point in the co-ordinate plane. 
# for n = 1, the figure will have 4^1 points. i.e. 4 points
# for n = 2, the figure will have 4^2 = 16 points
# for n = 3, the figure will have 4^3 = 64 points
# ...
# for n = n, the figure will have 4^n points

# We can divide the answer figure into 4 portions (quadrants). For example
# If n = 3, we will have 4^3 = 64 points => sqrt(64) = 8 rows,  sqrt(64) = 8 columns
# Each quadrant will have sqrt(64)//2 = 4 rows and 4 columns
# . . . . | . . . . 
# . . . . | . . . . 
#  quad I | quad II
# . . . . | . . . .
# . . . . | . . . .
# _________________
# . . . . | . . . .
# . . . . | . . . .
# quad III| quad IV 
# . . . . | . . . .
# . . . . | . . . .


# Take value of some positive integer n as user input
n = int(input("Enter value of n: "))

def f(n):
	# Trivial Case (n = 1)
	if n == 1:
		answer = [(1,1), (2,1), (2,2), (1,2)]

	else:
		n_rows = int(sqrt(4**n)) #number of rows = sqrt of total number of points 
		L = f(n-1)

		# We can divide the answer figure into 4 portions(quadrants).
		# Quadrant 1 is the image of f(n-1) rotated by -90 degrees i.e. elements of f(n-1) with points interchanged (if (1,2) is in f(n-1), => (2,1) will be in quad1) 
		quad1 = [] 
		for x in range(len(L)):
			quad1.append(tuple([L[x][1], L[x][0]])) 

		# Quadrant 2 is the mirror image of quad1 about the vertical, => row number of each point corresponding to a pt in quad1 will remain the same.
		quad2 = [0 for x in range(len(quad1))]
		for x in range(1, len(quad2)+1):
			quad2[-1*x] = tuple([quad1[x-1][0], n_rows + 1 - quad1[x-1][1] ])

		# Quadrant 3 is the image of f(n-1) shifted towards the bottom => row number of each point corresponding to a pt in quad1 will be incremented. 
		quad3 = []
		for x in range(0, len(L)):
			quad3.append(tuple([L[x][0] + n_rows//2, L[x][1]]))


		# Quadrant 4 is the image of f(n-1) shited towards the bottom and then to the right by as many units as there are rows in each quadrant. 
		quad4 = []
		for x in range(len(L)):
			quad4.append(tuple([L[x][0] + n_rows//2, L[x][1] + n_rows//2]))

		# The final image of f(n) is drawn in the order: quadrant 1 -> quadrant 3 -> quadrant 4 -> quadrant 2
		# So the final order of elements for the image of f(n) becomes:
		answer = quad1 + quad3 + quad4 + quad2
	return answer

pattern = f(n)
print(pattern)

# Code to illustrate the pattern
data = [(-1*pattern[x][0], pattern[x][1]) for x in range(len(pattern))] # adjusting axis acc to data
data = array(data)
plot(data[:, 1], data[:, 0], c="violet", linewidth=2.1)
axis("off")
show()