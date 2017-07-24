import math

content = dir(math)

print(content)

# Test package

import TestModule

print(TestModule.Tmin( 1, 2, 3, 4, -5, 6, 7 ))

print(TestModule.Tsum( 1, 2, 3, 4, -5, 6, 7 ))

print(TestModule.Tproduct( 1, 2, 3, 4, -5, 6, 7 ))
