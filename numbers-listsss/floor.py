num = list(range(31))

print(num)

print(min(num))
print(max(num))
print(sum(num))


print("------------------------------")


un_millon = list(range(0, 1000001))

print(min(un_millon))
print(max(un_millon))
print(sum(un_millon))


print("---------------------------------------\n")

odd_numbers = list(range(1, 20, 2))

for i in odd_numbers:
    print(i)



print("---------------------------------------\n")

multi_3 = list(range(3, 32, 3))

for i in multi_3:
    print(i)

print("---------------------------------------\n")

cubes = list(range(1,11))

for cubi in cubes:
    print(cubi**3)

print("---------------------------------------\n")

comp_cubes = [i**3 for i in cubes]

print(comp_cubes)










