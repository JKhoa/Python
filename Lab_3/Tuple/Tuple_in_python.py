import itertools
def Find_size():

    # sample Tuples#-
    Tuple1 = ("A", 1, "B", 2, "C", 3)#-
    Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")#-
    Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))#-
    #-
    # print the sizes of sample Tuples#-
    print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")#-
    print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")#-
    print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")#-

def Max_and_min():
    import heapq
    test_tup = (5, 20, 3, 7, 6, 8)
    # printing original tuple
    print("The original tuple is : " + str(test_tup))
    K = 2
    smallest = heapq.nsmallest(K, test_tup)
    largest = heapq.nlargest(K, test_tup)
    result = tuple(sorted(smallest + largest))
    print("The extracted values : " +str(result))

def Add_to_tuple():
    a = [1, 2, 3, 4, 5]
    res = list((n, n**3) for n in a)
    print(res)

def Adding_tuple_to_list():
    t1 = (1, 2, 3, 4)
    t2 = ('a', 'b', 'c', 'd')
    t3 = (True, False, True, False)
    print(tuple(list(t1) + list(t2) + list(t3)))

def Soft_by_second_items():
    a = [(1, 3), (4, 1), (2, 2)] 
    a.sort(key=lambda x: x[1])
    print(a)
def All_pair_combinations():
    # initializing tuples
    test_tuple1 = (4, 5)
    test_tuple2 = (7, 8)

    # printing original tuples
    print("The original tuple 1 : " + str(test_tuple1))
    print("The original tuple 2 : " + str(test_tuple2))

    # Lặp qua từng phần tử a trong test_tuple1 và từng phần tử b trong test_tuple2, tạo các cặp (a, b).
    res = [(a, b) for a in test_tuple1 for b in test_tuple2] + [(a, b) for a in test_tuple2 for b in test_tuple1]

    # printing result
    print("All pair combinations of 2 tuples : " + str(res))



Find_size()
Max_and_min()
Add_to_tuple()
Adding_tuple_to_list()
Soft_by_second_items()
All_pair_combinations()