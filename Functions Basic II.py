def countdown(num):
    countList = []
    for i in range(num, -1, -1):
        countList.append(i)
    return countList

print(countdown(5))

def print_return(list):
    print(list[0])
    return(list[1])

print_return([2,4])

def first_plus_leng(list):
    print(list[0] + len(list))

first_plus_leng([1,2,3,4,5])

def greater_than_second(list):
    greater_list = []
    for i in list:
        if len(list) < 2:
            return False
        elif i > list[1]:
            greater_list.append(i)
    return greater_list

print(greater_than_second([2,4,7,8,10,3]))

def length_and_value(length, val):
    num = []
    for i in range(length):
        num.append (val)
    return num

print(length_and_value(5, 7))