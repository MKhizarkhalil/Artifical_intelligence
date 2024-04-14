
#1
"""
import math
help(math)
print(math.sqrt(9))
"""
#2
"""
from math import sqrt
sqrt(4)
"""
#3
"""
from math as maths
print(maths.sqrt(9))

from math import sqrt as squareroot
> squareroot(9)
"""
#4
"""
import time 
x = time.time()
print(time.ctime(x))
time.sleep(3)
  
"""
#5
"""
 import glob
glob.glob("*.py")
"""   
#6
import random   
print(random.randint(1, 10),random.random())
x = [1,2,3,4,5]
#random.shuffle(x)
print(x)


random.sample(x,4)
print(random.sample(x,2))


