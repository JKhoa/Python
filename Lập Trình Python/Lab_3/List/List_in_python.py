def Indexing():
    my_list = [10, 20, 'Jessa', 12.50, 'Emma']
    # accessing 2nd element of the list
    print(my_list[1])  # 20
    # accessing 5th element of the list
    print(my_list[4])  # 'Emma'
def List_slicing():
    my_list = [10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
    # Extracting a portion of the list from 2nd till 5th element
    print(my_list[2:5])
    # Output ['Jessa', 12.5, 'Emma']
def Remove_all_occurrences():
    my_list = list([6, 4, 6, 6, 8, 12])

    for item in my_list:
        my_list.remove(6)

    print(my_list)
    # Output [4, 8, 12]
def Remove_range():
    my_list = list([2, 4, 6, 8, 10, 12])
    # remove range of items
    # remove item from index 2 to 5
    del my_list[2:5]
    print(my_list)
    # Output [2, 4, 12]

    # remove all items starting from index 3
    my_list = list([2, 4, 6, 8, 10, 12])
    del my_list[3:]
    print(my_list)
    # Output [2, 4, 6]
def Sort_list():
    my_list = [10, 20, 12.50, 25, 50]
    my_list.sort()
    print(my_list)

Indexing()
List_slicing()
Remove_all_occurrences()
Remove_range()
Sort_list()