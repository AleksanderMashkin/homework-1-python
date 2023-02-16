# from random import sample
# length_list = int(input("Ведите число длины списка: "))
# list_numbers = [i for i in sample(range(1, length_list*2), length_list)]
# print("рандомный список: ", list_numbers)
# sort_list = [list_numbers[i]
#             for i in range(1, len(list_numbers)) if list_numbers[i] > list_numbers[i-1]]
# print("sort list: ", sort_list)


# N = int(input("Введите до какого значения искать кратные числа"))
# list_numbers = [i for i in range(20, N) if i % 20 == 0 or i % 21 == 0]

# print("Список чисел кратных 20 или 21: ", list_numbers)



# names_workers = input("Введите имена сотрудников в одном предложении")

# def convert(function1):
    # return ([i for i in function1.split()])

# def names_dict(names):
    # res = {}
    # for names in names:
        # key = names[0].capitalize()
        #if key not in res:
            #res[key] = []
        #res[key].append(names)
    #return res

#print(names_dict(convert(names_workers)))

names_workers = input("Введите имена сотрудников в одном предложении")

def convert(function1):
    return ([i for i in function1.split()])

def names_dict(names):
    res = {}
    for names in names:
        key = names[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(names)
    return res

print(names_dict(convert(names_workers)))
