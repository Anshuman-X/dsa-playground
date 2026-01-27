import numpy as np

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers = numbers[numbers % 2 ==0]
print(even_numbers)

#Filter with mask

mask = numbers > 5

print("Numbers greater than 5 : ",numbers[mask])