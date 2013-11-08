import sys
import prime
import math

def prime_factorization(n):
    num = n
    sqr_root = int(math.sqrt(num))
    factors = prime.prime_list(sqr_root)
    prime_factor = []
    for i in factors:
        if i*i > num:
            prime_factor.append(num)
            return prime_factor
        while num%i == 0:
            num /= i
            prime_factor.append(i)
        if num == 1:
            return prime_factor
    prime_factor.append(num)
    return prime_factor

def main(num):
    print prime_factorization(num)

main(int(sys.argv[1]))
