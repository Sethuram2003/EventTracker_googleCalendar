
with open('list.txt') as f:
    data = f.read()
    data_into_list = data.split(",")
    print(data_into_list)
