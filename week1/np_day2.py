print("###### Operation and Linear Algebra ######\n")


import numpy as np 

v = np.array([1, 2, 3, 4, 5])
print("v[] = ", v)
print("v[] + 1 :", v + 1)
print("v[] * 2 :", v * 2)
print("v[] / 4 :", v / 4)
print("v[] ** 3: ", v ** 3)

print("\n####### Vectorized math funcs ######\n")

v1 = np.array([1, 5, 4, 3, 6])

print("v1[] : ", v1)
print("sqrt v1[]: ", np.sqrt(v1))

v2 = np.array([1.5, 2.33, 10.8, 4.53, 5.79])
print("v2[] : ", v2)

print("round v2[] : ", np.round(v2))
print("floor v2[] : ", np.floor(v2))
print("ceil v2[] : ", np.ceil(v2))
print("π = ", np.pi)
print("v1[] + v2[] = ", v1 + v2)
print("v1[] - v2[] = ", v1 - v2)
print("v1[] * v2[] = ", v1 * v2)
print("v2[] ** v1[] = ", v2 ** v1)

print("\n######### Comparaison Operators #######\n")

ages = np.array([16, 23, 32, 77, 22, 12, 45, 31, 27, 21, 84])

print("age == 20 : ", ages == 20)
print("age > 20", ages > 20)
print("age < 20", ages < 20)
ages[ages < 20] = 0
print("age < 20 => age = 0 : ", ages)

print("\n####### Filtring  ########\n")

ages = np.array([16, 23, 32, 77, 22, 12, 45, 31, 27, 21, 84])

print("Ages[] : ", ages)
teenagers = ages[ages <= 18]
print("teenagers : ", teenagers)
adults = ages[ages >= 30]
print("adults : ", adults)
