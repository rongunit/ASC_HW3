# ----------------------------- main.py ------------------------------
#  Исполняемый файл программы.
# -----------------------------------------------------------------------
import sys
from random import randint
import time

from parallelepiped import Parallelepiped
from shape import Shape
from sphere import Sphere
from tetrahedron import Tetrahedron


def generate_test(path, size):
    cont = []
    for i in range(size):
        key = randint(1, 3)
        if key == 1:
            cont.append(Sphere())
        elif key == 2:
            cont.append(Tetrahedron())
        elif key == 3:
            cont.append(Parallelepiped())

    out_file = open(path, "w")
    for i in cont:
        out_file.write(i.to_test() + "\n")
    out_file.close()


def run_with_rnd_data(shapes_arr, size, path_random, path_sorted):
    for i in range(size):
        key = randint(1, 3)
        if key == 1:
            shapes_arr.append(Sphere())
        elif key == 2:
            shapes_arr.append(Tetrahedron())
        elif key == 3:
            shapes_arr.append(Parallelepiped())

    rnd_file = open(path_random, "w")
    sorted_file = open(path_sorted, "w")
    for i in shapes_arr:
        rnd_file.write(i.to_test() + "\n")

    start = time.time()
    heap_sort(shapes_arr)
    print(f"Sort time: {time.time() - start} seconds.")
    for i in shapes_arr:
        sorted_file.write(i.to_test() + "\n")


def run_from_file(path, shapes_arr, output_path):
    input_file = open(path)
    line = input_file.readline()
    while line != "":
        s_arr = line.replace("\n", "").split(" ")
        shapes_arr.append(read_shape(s_arr))
        line = input_file.readline()
    input_file.close()

    start = time.time()
    heap_sort(shapes_arr)
    print(f"Time: {time.time() - start} seconds.")

    output_file = open(output_path, "w")
    for el in shapes_arr:
        output_file.write(el.to_string() + "\n")


# transforms an array into Shape object
def read_shape(str_array):
    index = str_array[0]
    if index == "1":
        str_array.remove("1")
        return Sphere(str_array)
    elif index == "2":
        str_array.remove("2")
        return Tetrahedron(str_array)
    elif index == "3":
        str_array.remove("3")
        return Parallelepiped(str_array)
    else:
        print("Error in container")


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n -
# размер кучи
def heapify(shapes_arr: [Shape], n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and shapes_arr[i].volume() < shapes_arr[l].volume():
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and shapes_arr[largest].volume() < shapes_arr[r].volume():
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i], shapes_arr[largest] = shapes_arr[largest], shapes_arr[i]  # свап

        # Применяем heapify к корню.
        heapify(shapes_arr, n, largest)


# Основная функция для сортировки массива заданного размера
def heap_sort(arrr: [Shape]):
    n = len(arrr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arrr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arrr[i], arrr[0] = arrr[0], arrr[i]  # свап
        heapify(arrr, i, 0)


if __name__ == '__main__':
    # ttt = []
    # for i in range(0, 100):
    #     arr = []
    #     ttt.append(run_from_file("tests/test5.txt", arr))
    # print("min = " + str(min(ttt)) + " max = " + str(max(ttt)))

    arr = []
    # run_from_file("tests/test1.txt", arr)

    if len(sys.argv) == 4:
        if sys.argv[1] != "--test" or (not sys.argv[2].isdigit()):
            print("Unsupported command arguments!")
        num = int(sys.argv[2])
        if num <= 0:
            print("Unsupported command arguments!")
        generate_test(sys.argv[3], num)

    # Для выолнения основной задачи программы
    elif len(sys.argv) == 5:
        if sys.argv[1] == "-f":
            run_from_file(sys.argv[2], arr, sys.argv[3])
        elif sys.argv[1] == "-n" and sys.argv[2].isdigit():
            num = int(sys.argv[2])
            if num <= 0:
                print("Unsupported command arguments! Negative amount of shapes!")
            run_with_rnd_data(arr, int(sys.argv[2]), sys.argv[3], sys.argv[4])
        else:
            print("Unsupported command! Use -n, -f or --test!")
    else:
        print("Unsupported amount of command arguments!")
