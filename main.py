from display import *
from draw import *
from matrix import *
import random


screen = new_screen()
color = [ 0, 255, 0 ]
matrix1 = [[1,2,3,1],[10,20,30,1],[100,200,300,1],[400,500,600,1]]
matrix2=new_matrix()
#print matrix
print("Testing Print_Matrix of[[1,2,3,1],[10,20,30,1],[100,200,300,1],[400,500,600,1]]")
print_matrix(matrix1)

#identity matrix
print("Testing Identity Matrix")
ident(matrix2)
print_matrix(matrix2)

#testing matrix identity multiplication

print("Testing Matrix Identity Multiplication")
matrix_mult(matrix1,matrix2)
print_matrix(matrix2)

#Testing add_edge 
matrix3 = new_matrix(rows=0,cols=0)
add_edge(matrix3,1,2,3,4,5,6)
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
print_matrix(matrix3)

#Testing Matrix multiplication Part 2
matrix4 = new_matrix(rows=0,cols=0)
add_edge(matrix4, 1, 2, 3, 4, 5, 6)
add_edge(matrix4, 7, 8, 9, 10, 11, 12)
print("Testing Matrix mult. m1 =")
print_matrix(matrix4)
print("Testing Matrix mult. m1 *m2")
matrix_mult(matrix4,matrix3)
print_matrix(matrix3)

#Image of Sad Face
final_matrix = new_matrix(rows=0,cols=0)
add_edge(final_matrix,100,100,0,400,100,0)
add_edge(final_matrix,400,100,0,400,400,0)
add_edge(final_matrix,400,400,0,100,400,0)
add_edge(final_matrix,100,400,0,100,100,0)

add_edge(final_matrix,200,350,0,200,250,0)
add_edge(final_matrix,300,350,0,300,250,0)

add_edge(final_matrix,150,150,0,200,200,0)
add_edge(final_matrix,200,200,0,300,200,0)
add_edge(final_matrix,300,200,0,350,150,0)
draw_lines( final_matrix, screen, color )
display(screen)

