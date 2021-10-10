num_list = [370, 67, 98, 4, 87, 1, 2, 65, 456, 8, 34, 789, 0]
result = [num_list[i] for i in range(1, len(num_list)) if num_list[1] > num_list[i-1]]
print(result)
