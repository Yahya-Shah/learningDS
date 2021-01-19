a = [12, 13, 100, 1, 15, 10, 1000, 15, 18, 10, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 16, 17, 19, 20, 200, 201, 1002]


def mean():
    length_of_a_set = len(a)
    sum_of_a_set = sum(a)
    finding_mean = sum_of_a_set % length_of_a_set

    print("Total Length = ", length_of_a_set)
    print("Total Sum = ", sum_of_a_set)
    print("Mean = ", finding_mean)


print("-------------------------------------")
print("Finding Mean of the given DataSet")
mean()


def median():
    length_of_a_set = len(a)

    if length_of_a_set % 2 == 0:
        middle = int(len(a) / 2)
        mid = a[middle] + 1
        print("Medians if the given number in dataset are even")
        print("Total Length of numbers = ", length_of_a_set)
        print("Medians = ", a[middle], mid)

    elif length_of_a_set % 2 != 0:
        middle = int(len(a) / 2)
        print("Total Length of numbers = ", length_of_a_set)
        print("Median if numbers in given dataset are odd")
        print("Median = ", a[middle])


print("-------------------------------------")
print("Finding Median of the given DataSet")
median()


def mode():
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                print("Repeating numbers =", a[j])


print("-------------------------------------")
print("Finding Mode of the given DataSet")
mode()
