def add_one(num):
    return num + 1

def add_one_to_list(num_list):
    new_list = []
    for num in num_list:
        new_list.append(add_one(num))

    print(new_list)

add_one_to_list([5, 6, 7])