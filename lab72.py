import random

def create(size):
    matrix = {}
    for i in range(size[0]):
        matrix_list = []
        for k in range(size[1]):
            a = int(random.uniform(-34, 26))
            matrix_list.append(a)
        matrix[i+1] = matrix_list
    return matrix
def print_t(matrix):
    for i in matrix:
        print(matrix[i])


def change(matrix):
    for i in range(len(matrix)):
        list1 = matrix[i+1]
        list2 = sorted(list1)
        n_min = list2[0]
        n_max = list2[len(list2)-1]
        index_min =list1.index(n_min)
        index_max =list1.index(n_max)
        list1[index_min] = n_max
        list1[index_max] = n_min
        matrix.update({i+1:list1})
    return matrix


def main():
    matrix = create((8,6))
    print_t(matrix)
    print()
    change(matrix)
    print_t(matrix)
main()