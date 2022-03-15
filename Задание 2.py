my_list = []
for n in range(1,1000):
    sum = 0
    k = n
    while k>= 1:
        sum += k % 10
        k = k // 10
    if n % 3 == 0 and n % 5 != 0 and sum < 10:
       my_list.append(n)

print(my_list)
