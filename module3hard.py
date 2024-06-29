def calculate_structure_sum(data_structure):

    sum_all = 0

    if isinstance(data_structure, (int, float)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_all += calculate_structure_sum(item)
    elif isinstance(data_structure, tuple):
        for item in data_structure:
            sum_all += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_all += calculate_structure_sum(key)
            sum_all += calculate_structure_sum(value)

    return sum_all

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)