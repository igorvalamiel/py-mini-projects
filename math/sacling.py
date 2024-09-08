import numpy as np

#getting the matrix
m, n = eval(input("What is the size of your matrix? (m, n): "))
l = []
for i in range(m):
    print(f'Type line {i+1}: [x1, x2, ..., xn]')
    line = eval(input())
    while len(line) != n:
        print("There is more/less itens than it should have.")
        print(f'Type line {i+1}: [x1, x2, ..., xn]')
        line = eval(input())
    l.append(line)

mat = np.array(l, dtype='f')
print(mat)
print()

#defining function for deleting zero's rows
del_list = []
def clear_null(mat, l):
    m = []
    for i in range(len(mat)):
        if i not in l:
            m.append(mat[i])
    return np.array(m)

#tranforming the pivot into 1
print("Tranforming all pivôs into 1")
for pos_lin, lin in enumerate(mat):
    ini = 0
    for it in lin:
        if it != 0: 
            ini=it
            break
    if ini == 0:
        del_list.append(pos_lin)
    else:
        mat[pos_lin, :] = lin/ini

mat = clear_null(mat, del_list)
del_list = []

print()
print(mat)
print()

#Scaling
def scaling_line(mat, pos):
    n = pos-1
    if pos != len(mat):
        for pos_lin2, lin2 in enumerate(mat):
            if pos_lin2 < pos: pass
            else:
                mat[pos_lin2,:] -= mat[n,:]
        print(mat)
        scaling_line(mat, pos+1)
    else:
        return None

scaling_line(mat, 1)

#deleting zero's rows
for pos_lin3, lin3 in enumerate(mat):
    if not np.any(lin3):
        del_list.append(pos_lin3)

mat = clear_null(mat, del_list)
del_list = []

print()
print(mat)
print()