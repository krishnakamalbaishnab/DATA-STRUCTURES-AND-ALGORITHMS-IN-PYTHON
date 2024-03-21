myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5 
#target = int(input("Enter the element to be searched: ")) #taking the element to be searched as input from the user


# if target in myList:
#     print(f"Element found at index {myList.index(target)}")

# else:
#     print("Element not found")


#leinear Search

def linearSearch(list, traget):
    for i, value in enumerate(list):
        if value == target:
            return i
        return -1

print(linearSearch(myList, target))