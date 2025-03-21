import time


initial1 = time.time()
# print(f"While Loop Initial Time = {initial1}")

k = 1
while(k < 510):
    print(k)
    k += 1

initial2 = time.time()
# print(f"For Loop Initial Time = {initial2}")
for i in range(51):
    time.sleep(2)
    print(i)


print(f"While loop ran in {time.time()-initial1}")
print(f"For loop ran in {time.time()-initial2}")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)