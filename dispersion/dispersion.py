# use my algoritms python-core
import numpy as np
import statistics
array = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
array.sort()


def dispersion_calc(array):
    if len(array) % 2 != 0:
        mediana = array[len(array)//2]
    else:
        mediana = (array[len(array)//2] + array[len(array)//2 - 1])/2

    sum = 0
    for i in range(len(array)):
        sum += (mediana-array[i])**2

    return sum/(len(array)-1)


def deviation_calc(array):
    return dispersion_calc(array)**0.5


dispersion = dispersion_calc(array)
deviation = deviation_calc(array)
print(dispersion, deviation)


# use statictics
data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
stdev = statistics.stdev(data)
print(stdev)


# use numpy
values = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
std = np.std(values, ddof=1)
print("Standard deviation:", std)
