def print_list(my_list:list):
    # print(len(my_list))
    for i in range(0, len(my_list)):
        if i == len(my_list)-1:
            print(f"{my_list[i]}")
        else:
            print(f"{my_list[i]} -> ", end='')