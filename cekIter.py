import time as time
import numpy as np
iter = 10000

a = time.clock()
for i in np.arange(iter):
    pass
b = time.clock()
print("numpy")
print(b-a)

a = time.clock()
for i in range(iter):
    pass
b = time.clock()
print("normal")
print(b-a)
