import sys

def check_prime(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True

def prime_list(n):
    print "check out number from 1 to " + `n`
    prime_list = []
    for i in xrange(2,n):
        if check_prime(i):
            prime_list.append(i)
            print `i` + " is prime!"
    # print prime_list
    return prime_list

# prime_list(int(sys.argv[1]))
