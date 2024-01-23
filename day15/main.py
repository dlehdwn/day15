#main
import my_math as mm

result = mm.add(10,10)
print(result)

from my_math import add
result = add(10,70)
print(result)

from my_math import * # * universal
result1 = add(10,70)
print(result1)
result2 = min(10,70)
print(result2)
