def Convert_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    res_dict = dict(zip(keys, values))
    print(res_dict)


def Merge_dict():
    dict1 = {'Ten': 10, 'Twenty': 20}
    dict2 = {'Thirty': 30, 'Forty': 40}
    merged_dict = {**dict1, **dict2}
    print(merged_dict)

def Delete_list_of_keys():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }
    # Keys to remove
    keys = ["name", "salary"]
    for k in keys:
        sample_dict.pop(k)
    print(sample_dict)
def Rename_list_of_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)
def Change_value_list():
    sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
    }

    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)
    
Convert_dict()
Merge_dict()
Delete_list_of_keys()
Rename_list_of_keys()
Change_value_list()