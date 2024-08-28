import random

lst = random.sample(range(0, 50), 25)
lenght = len(lst)

print(lst)
noi = 0
while lenght > 0:
    swapped = False

    for i in range(lenght):
        if i+1 == len(lst):
            break
        if lst[i+1] < lst[i]:
            lst[i+1], lst[i]= lst[i], lst[i+1]
            swapped = True

    if not swapped:
        break

    noi += 1
    lenght -= 1


print("Number of iterations: " + str(noi))
print(lst)