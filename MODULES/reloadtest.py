
import time
import reloadmod
from imp import reload

# print(reloadmod.add(11,22))
# print("Entered into sleeping state")
# time.sleep(20)
# import reloadmod
# print("Exiting from sleeping state")
# print(reloadmod.mul(10,22))

# No differnce though matter how many times we are importing the function.


# the above problem can be solved by using reload by importing imp module
print(reloadmod.add(11,22))
print("Entered into sleeping state")
time.sleep(20)
print("Exiting from sleeping state")
reload(reloadmod)
print(reloadmod.mul(10,22))
