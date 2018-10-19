import numpy as np

def lol(epsilon, delta, p=0.1):
    return 4/((epsilon**2)*p) * np.log(2/delta)

# l = [
#     [0.2, 0.1  ],
#     [0.2, 0.05 ],
#     [0.2, 0.01 ],
#     [0.2, 0.001],
# ]
l = [
    [0.2, 0.1],
    [0.3, 0.1],
    [0.4, 0.1],
    [0.5, 0.1],
]



# 0.2  &  0.1     &   2995.73
# 0.2  &  0.05    &   3688.87
# 0.2  &  0.01    &   5298.31
# 0.2  &  0.001   &   7600.90

# 0.2  &   0.1    &   2995.7
# 0.3  &   0.1    &   1331.4
# 0.4  &   0.1    &   748.9
# 0.5  &   0.1    &   479.3

for i in l:
    print(lol(i[0], i[1]))
