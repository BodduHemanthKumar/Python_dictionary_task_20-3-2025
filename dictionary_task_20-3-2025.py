# Task:-
# 1. Print the list of prime numbers and non prime numbers separately in given list.
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime =[]
non_prime = []
for i in range(0,len(num),1):
    number = num[i]
    fact = 0
    for j in range(1,number+1,1):
        if number%j ==0:
            fact+=1
    if fact==2:
        prime.append(number)
    if fact!=2:
        non_prime.append(number)
print("Prime list = ",prime)
print("non Prime list = ",non_prime)

