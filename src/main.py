""" exString = set("HackerRank")
print(exString)
print("================1================")
exInt = set([1,2,1,2,3,4,5,6,0,9,12,22,3])
print(exInt)
print("================2================")
exStruct = set({"Hacker" : "DOSHI", "Rank" : 616 })
print(exStruct)
exStruct2 = set({"Z" : 1, "A" : "1" })
print(exStruct2)
exStruct2 = set({"Z" : 2, "A" : 1 })
print(exStruct2)
print("================3================")
exEnum = enumerate(['H','a','c','k','e','r','r','a','n','k'])
print(exEnum)
for index, exChar in enumerate(exEnum):
    print(f"Index {index}: {exChar}")
exEnumWithSet = set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
print(exEnumWithSet)
print("================4================") """

arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]

def average(arr):
    arrSet = set(arr)
    print(arrSet)
    print(len(arrSet))
    sumOfSet = sum(arrSet)
    print(sumOfSet)
    averageOfDistinct = sumOfSet / len(arrSet)
    print(averageOfDistinct)

average(arr)
