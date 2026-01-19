import numpy as np

print("####### BROADCASTING ########\n")


a = np.array([1, 2, 3, 4])
b = 2

print("a[] : ", a)
print("b[] : ", b)
print("[Broadcasting]  a * b : ", a * b)


"""	 Broadcasting Rule :
		shape1(x1, y1) , shape2(x2, y2)
		if shape1 == shape2 
		or (x1 != x2 and (x1 == 1 or x2 == 1))
		or (y1 != y2 and (y1 == 1 or y2 == 1) :
			broadcast
		else: error
"""

v1 = np.array([[1, 2, 3, 4]])
v2 = np.array([[1], [2], [3], [4]])

print(f"v1[]  {v1.shape} : {v1}");
print(f"v2[]  {v2.shape} : {v2}");

print(f"v1[] * v2[]  : {v1 * v2}");


"""
v1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
v2 = np.array([[1], [2], [3], [4]])

print(f"v1[]  {v1.shape} : {v1}"); # shape = (2, 4)
print(f"v2[]  {v2.shape} : {v2}"); # shape = (4, 1)

print(f"v1[] * v2[]  : {v1 * v2}");

OUTPUT :

ValueError: operands could not be broadcast together

"""


print("\n####### AGGREGATE FUNCTIONS ########\n")

array = np.array([[1, 2, 3, 4],
		  [5, 6, 7, 8]])


print(f"array[]  {array.shape} : {array}");
print(f"sum array[] : {np.sum(array)}")
print(f"mean array[] : {np.mean(array)}")
print(f"std array[] : {np.std(array)}")
print(f"min array[] : {np.min(array)}")
print(f"max array[] : {np.max(array)}")
print(f"argmin array[] : {np.argmin(array)}")
print(f"argmax array[] : {np.argmax(array)}")

print(f"sum rows array[] : {np.sum(array, axis = 1)}")
print(f"sum columns array[] : {np.sum(array, axis = 0)}")


print("\n####### FILTRING (MORE) ########\n")

v = np.array([[21, 17, 22, 2, 89, 36, 74, 17, 66, 3, 0]])

print(f"v[]  {v.shape} : {v}");

print(f"evens :{v[v % 2 == 0]}")
print(f"odds :{v[v % 2 != 0]}")


print("\n####### RANDOM NUMBERS ########\n")


rng = np.random.default_rng()

print(f"Generator : {rng}")
print(f"Random Number (low = 1, high = 100): {rng.integers(low = 1, high = 100)}")
print(f"Array Random Number (low = 1, high = 100): {rng.integers(low = 1, high = 100, size = 3)}")
print(f"Array Random Number (low = 1, high = 100): {rng.integers(low = 1, high = 100, size = (2, 5))}")

print(f"Random Number (low = -1, high = 1): {np.random.uniform(low = -1, high = 1)}")
print(f"Array Random Number (low = -1, high = 1): {np.random.uniform(low = -1, high = 1, size = (3, 4))}")


print("> SHUFFLE")

rng = np.random.default_rng()
rng.shuffle(a)
print(f"a[] shuffled : {a}")


fruits = np.array(["apple", "orange", "coconut", "peer", "watermelon"])
rng.shuffle(fruits)
print(f"fruits[] shuffled : {fruits}")
print(f"choosen fruit from fruits[] : {rng.choice(fruits)}")
print(f"Array Choosen Fruits from fruits[] : {rng.choice(fruits, size = 3)}")

