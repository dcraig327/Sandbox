from time import time

count = 10000000
time_list = []
for i in range(count):
    start = time()
    end = time()
    delta = end - start
    time_list.append(delta)

max = 0
for n in time_list:
    if n > max:
        max = n

avg = sum(time_list) / len(time_list)
print(f"count: {count}\navg: {avg}\nmax: {max}\n")