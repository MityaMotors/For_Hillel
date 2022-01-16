def check_homework(first_str:str = "john marta james Morgan Adam Maria huang"):
    str_list = first_str.split(' ')
    new_list = []
    for item in str_list:
        item.capitalize()
        new_list.append(item)
    return new_list

if __name__ == "__main":
    data = """"""