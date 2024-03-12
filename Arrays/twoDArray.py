import numpy as np

myTwoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(myTwoDArray)

#the time complexity of the traversal operation is O(n*m) because we are visiting each element of the array once.


#the space complexity of the traversal operation is O(1) because we are not using any extra space to traverse the array. We are just visiting each element of the array once.

#inserting an element at a specific position in the array.

myTwoDArray = np.insert(myTwoDArray,1,[11,12,13],axis=0)

print(myTwoDArray)

#the time complexity of the insertion operation is O(n*m) because we are visiting each element of the array once.

#the space complexity of the insertion operation is O(n*m) because we are using extra space to insert the element in the array.

#inserting an element at a specific position in the array.

myTwoDArray = np.insert(myTwoDArray,1,[14,15,16],axis=1)

print(myTwoDArray)

#the time complexity of the insertion operation is O(n*m) because we are visiting each element of the array once.

#the space complexity of the insertion operation is O(n*m) because we are using extra space to insert the element in the array.

