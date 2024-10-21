import time

start = time.time()
time.sleep(10)
end= time.time()

print(start)
print(end)
print(end-start)

start = time.time()
time.sleep(5)
end = time.time()

print(end-start)
