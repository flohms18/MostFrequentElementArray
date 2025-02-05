def MostFrequentElementinArray():
    MyArray = [1, 2, 8, 3, 2, 2, 2, 5, 1]
    print(max(MyArray, key = MyArray.count))
                
MostFrequentElementinArray()