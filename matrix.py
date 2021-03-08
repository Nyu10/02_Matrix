"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(float(matrix[j][i]),end =" ")
        print()
    print()

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                matrix[i][j]=1.0
            else:
                matrix[i][j]=0.0


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2

def matrix_mult( m1, m2 ):
    m1_invert=invert_matrix(m1)
    m2_invert=invert_matrix(m2)
    p = len(m1_invert)#rows of m1
    n=len(m2_invert)#column of m1 and rows of m2 are the same
    q=len(m2_invert[0])# columns of m2
    result=new_matrix(rows=p,cols=q)
    #actual matrix multiplication
    for i in range(p):
        for j in range(n):
            for k in range(q):
                result[i][k]+=m1_invert[i][j]*m2_invert[j][k]
    #re-inverts result
    final_result=invert_matrix(result)
    #copy finla_results to m2
    for i in range(len(m2)):
        for j in range(len(m2[i])):
            m2[i][j]=final_result[i][j]

#inverts matrix to match 
#x0  x1      xn
#y0  y1      yn
#z0  z1  ... zn
#1   1        1

def invert_matrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    temp =new_matrix(rows=col,cols=row)
    for i in range(col):
        for j in range(row):
            temp[i][j]=matrix[j][i]

    return temp

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( rows):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m

