# for school method
import math

# for Miller-Rabin primality test 
import random

class SchoolMethod:
    """
    Finds prime numbers smaller than n, using
    School method testing.
    """
    def get_primes(self, n: int) -> list:
        """
        Finds the prime numbers smaller than n, using
        School method of primality test
        """
        primes = []
        num = 0
        while num <= n:
            if self.isPrime(num):
                primes.append(num)
            num = num + 1

        return primes

    def isPrime(self, num: int) -> bool:
        """
        School Method of primality test
        """
        # if number is less than 2
        # its not prime
        if num < 2:
            return False

        # if number is 2
        # it is prime
        elif num == 2:
            return True

        # check if numbers is divisible by the
        # numbers in range 2 to its sq root
        # if yes, then number is not prime
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False

        # else number is prime
        return True


class SieveOfEratosthenes:
    """
    Finds prime numbers smaller than n, using
    Sieve of Eratosthenes algorithm.
    """
    def get_primes(self, n):
        """ 
        this method generates all the prime
        numbers smaller than given number.
        """
        list_of_primes = list(range(2, n+1))

        index = 0
        t = 2

        while t*t < n:
            for i in list_of_primes[index+1:]:
                if i%t == 0:
                    list_of_primes.remove(i)

            index +=1
            t = list_of_primes[index]

        return list_of_primes

class SieveOfSundaram:
    """
    Finds prime numbers smaller than n, using
    Sieve of Sundaram algorithm.
    """

    def get_primes(self, n):
        primes = []
        nNew = n//2

        marked = [0]*(nNew)

        for i in range(1, nNew):
            j = i

            while((i + j + 2*i*j) < nNew):
                marked[i + j + 2*i*j] = 1

                j+=1

        if n>2:
            primes.append(2)

        for i in range(1, nNew):
            if not(marked[i]):
                primes.append(2*i + 1)

        return primes    

class FermatMethod:
    def __init__(self, k) -> None:
        self.k = k
    def get_primes(self, n):
        primes = []
        num = 0
        while num <= n:
            if self.isPrime(num):
                primes.append(num)
            num = num + 1

        return primes

    def isPrime(self, num):
        """
        Checks if number is prime using
        Fermat Method for primality test
        """
        if num < 2 or num == 4:
            return False

        if num == 2 or num == 3:
            return True

        else:
            for i in range(self.k):
                # pick a random number from [2, n-2]
                # above corner cases make sure that n > 4
                a = 2 + random.randint(1, num-4)

                # Fermat's little theorem
                if (a**(num-1))%num != 1:
                    return False
        return True

class MillerRabin:
    """
    Its a probablistic method to check if the
    given number is prime or not. Based on Fermat's
    Little theorem.
    """
    def __init__(self, k):
        # k is the accuracy of the test
        self.k = k

    def get_primes(self, n):
        primes = []
        num = 2
        while num <= n:
            if self.isPrime(num):
                primes.append(num)
            num +=1

        return primes 

    def miller_test(self, n:int, d:int) -> bool:
        """
        this method is called for all k trials
        """

        # pick a random number [2, n-2]
        # corner cases make sure n > 4
        a  = 2 + random.randint(1, n-4)

        # compute a^d mod n
        x = (a**d) % n

        if (x == 1 or x == n-1):
            return True

        # Keep squaring x while one
        # of the following doesn't
        # happen
        # (i) d does not reach n-1
        # (ii) (x^2) % n is not 1
        # (iii) (x^2) % n is not n-1
        while d != n-1:

            # calculating x^2
            x = (x*x) % n

            # double up the power
            d *= 2

            if x == 1:
                return False

            if x == n-1:
                return True

        return False

    def isPrime(self, num: int) -> bool:

        # edge cases
        if num <= 1 or num == 4:
            return False

        if num <= 3:
            return True

        if num%2 == 0:
            return False
        
        # Finding r such that n = 2^d * r + 1, (r > 0)
        d = num-1

        while d % 2 == 0:
            d //= 2

        # iterate k times
        for i in range(self.k):
            if self.miller_test(num, d) == False:
                return False

        return True

if __name__ == "__main__":
    p = SieveOfSundaram()
    primes = p.get_primes(1000)
    print(primes, '\n')
    print(f"Number of prime numbers smaller than 1000, \
generated using {p.__class__.__name__}: {len(primes)}")