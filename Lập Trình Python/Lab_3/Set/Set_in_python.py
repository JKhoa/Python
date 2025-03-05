def Create_set():
    # set of mixed types intger, string, and floats
    sample_set = {'Mark', 'Jessa', 25, 75.25}
    print(sample_set)
    # Output {25, 'Mark', 75.25, 'Jessa'}

    # create a set using set constructor
    # set of strings
    book_set = set(("Harry Potter", "Angels and Demons", "Atlas Shrugged"))
    print(book_set)
    # output {'Harry Potter', 'Atlas Shrugged', 'Angels and Demons'}

    print(type(book_set))  

def Remove_set():
    color_set = {'red', 'orange', 'yellow', 'white', 'black'}
    # remove single item
    color_set.remove('yellow')
    print(color_set)
    # Output {'red', 'orange', 'white', 'black'}
    # remove single item from a set without raising an error
    color_set.discard('white')
    print(color_set)
    # Output {'orange', 'black', 'red'}
    # remove any random item from a set
    deleted_item = color_set.pop()
    print("item get deleted: " +deleted_item)

def Union_set():
    color_set1 = {'red', 'orange', 'yellow'}
    color_set2 = {'yellow', 'black', 'green'}
    # union of two sets
    union_color_set = color_set1 | color_set2
    print(union_color_set)
    # Output {'black', 'green', 'orange', 'red', 'yellow'}

def Soft_set():
    set1 = {20, 4, 6, 10, 8, 15}
    sorted_list = sorted(set1)
    #gán set cho sorted list
    sorted_set = set(sorted_list)
    print(sorted_set)
def Difference_set():
    color_set1 = {'red', 'orange', 'yellow'}
    color_set2 = {'yellow', 'black', 'green'}
    # difference between two sets
    diff_color_set = color_set1 - color_set2
    print(diff_color_set)

Create_set()
Remove_set()
Union_set()
Soft_set()
Difference_set()