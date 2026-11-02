list = ["A1", "B2", "A1", "C3", "B2", "D4"]

unique_list = []

for item in list:
    if unique_list.count(item) == 0:
        unique_list.append(item)

print(unique_list)
