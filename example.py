from data_type import *

a = uint8(255)
b = uint8(1)
print(a + b) # 0

a = int8(127)
b = int8(1)
print(a + b) # -128

a = uint8(-1)
print(a) # 255

a = vec([1, 2, 3])
b = vec([4, 5, 6])
print(a + b) # vec([5, 7, 9])

a = vec([[1, 2, 3], [4, 5, 6]])
b = vec([[7, 8, 9], [10, 11, 12]])
print(a + b) # vec([[8, 10, 12], [14, 16, 18]])
print(a * b) # vec([[7, 16, 27], [40, 55, 72]])

a = vec([1, 2, 3])
b = vec([1, 2, 4])
print(a == b) # vec([True, True, False])
print(a != b) # vec([False, False, True])

a = vec([[1, 2, 3], [4, 5, 6]])
print(a.T) # vec([[1, 4], [2, 5], [3, 6]])

a = vec([[1, 2, 3], [4, 5, 6]])
print(a * 5) # vec([[5, 10, 15], [20, 25, 30]])

a = vec([[1, 2, 3], [4, 5, 6]])
b = vec([3,5,7])
print(a.dot(b)) # vec([34, 79])
print(type(a.dot(b))) # vec([34, 79])

print(a.rank) # 2

a = autotype(1)
print(type(a)) # Integer

a = autotype(1.0)
print(type(a)) # Real

a = autotype(1.0+1.0j)
print(type(a)) # Complex

a = autotype([1, 2, 3])
print(type(a)) # vec

a = autotype([[1, 2, 3], [4, 5, 6]])
print(type(a)) # vec

a = autotype("123")
print(type(a)) # String

a = autotype((123.0, 456.0))
print(type(a)) # Tuple
