import numpy as np

print("######### EXAM NUMPY ##########")

print("###### PART 1 ######\n")

temperatures = np.array([[22.5, 23.1, 21.8, 20.2, 19.5, 18.9, 19.2],
			[15.3, 15.8, 16.2, 14.9, 14.1, 13.7, 14.0],
			[28.5, 29.1, 28.8, 27.3, 26.5, 25.9, 26.2],
			[10.2, 11.5, 12.1, 11.8, 10.5, 9.8, 10.1]])

print("Temperatures :")
print(temperatures)

print("Temperatures dim = ", temperatures.ndim)
print("Temperatures shape = ", temperatures.shape)
print("Temperatures nb elts = ", temperatures.shape[0] *  temperatures.shape[1])

print("Temperatures mean = ", np.mean(temperatures))
print("Temperatures min = ", np.min(temperatures))
print("Temperatures max = ", np.max(temperatures))
print("Temperatures data type = ", temperatures.dtype)


print("\n###### PART 2 #######\n")

print("Station 3 : Day 5 = ", temperatures[2, 4])
print("Station 2 : ", temperatures[1])
print("Day 4 : ", temperatures[:,3])
print("Station 1-2 : Day 2-5 : ")
t = temperatures[:2, 1:5]
print(t)
print("shape = ", t.shape)

t = temperatures[:,0::2]
print(t)
print("shape = ", t.shape)


print("\n###### PART 3 #######\n")

temps_f = temperatures * (9/5) + 32
print("Temperatures : ")
print(temps_f)

tmp_mean = np.mean(temperatures)
tmp_std = np.std(temperatures)
tmp_normalized = (temperatures - tmp_mean) / tmp_std

print("Mean : ", tmp_mean)
print("Std : ", tmp_std)
print("Normalized : ")
print(tmp_normalized)


print("Temperature > 25 :")
print(temperatures > 25)
print("Count :", len(temperatures[temperatures > 25]))


s_mean = []
for i in range(temperatures.shape[0]):
	s_mean.append(np.mean(temperatures[i]))

for i in range(len(s_mean)): print(f"Station {i + 1} mean :", s_mean[i])

d_mean = []
d_std = []
for i in range(temperatures.shape[1]):
	d_mean.append(np.mean(temperatures[:,i]))

#for i in range(len(d_mean)): print(f"Day {i + 1} mean :", d_mean[i])

for i in range(temperatures.shape[1]):
	d_std.append(np.std(temperatures[:,i]))

#for i in range(len(d_mean)): print(f"Day {i + 1} std :", d_std[i])


tmp_col_normalized = (temperatures[:,::] - d_mean) / d_std

print("Column-wise normalization : ")
print(tmp_col_normalized)


r = np.array([[1], [0.5], [2], [0.2]])

print("r :")
print(r)
print("r shape = ", r.shape)

print("Temperatures - r :")
print(temperatures - r)


print("\n####### PART 4 ########\n")


print(f"Coldest Station : Station {np.argmin(s_mean)} with mean = {np.min(s_mean)}")
print(f"Warmest Station : Station {np.argmax(s_mean)} with mean = {np.max(s_mean)}")
s_std = []
for i in range(temperatures.shape[0]):
	s_std.append(np.std(temperatures[i]))

for i in range(temperatures.shape[0]):
	print(f"Station {i + 1}: {s_std[i]}°C")

for i in range(temperatures.shape[0]):
	print(f"Station {i + 1} | Mean : {np.mean(temperatures[i])} | Max : {np.max(temperatures[i])} | Std : {s_std[i]}")
