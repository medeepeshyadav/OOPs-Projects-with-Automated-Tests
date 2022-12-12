# Testing primenumbers module
import pytest
from primenumbers import (SchoolMethod, FermatMethod, 
SieveOfEratosthenes, SieveOfSundaram, MillerRabin)

# creating fixtures of each primality test classes
@pytest.fixture
def school_method_obj() -> SchoolMethod:
    sm = SchoolMethod()
    return sm

@pytest.fixture
def fermat_method_obj() -> SchoolMethod:
    fm = FermatMethod(k=50)
    return fm

@pytest.fixture
def sieve_of_eratosthenes_obj() -> SchoolMethod:
    soe = SieveOfEratosthenes()
    return soe

@pytest.fixture
def sieve_of_sundaram_obj() -> SchoolMethod:
    sos = SieveOfSundaram()
    return sos

@pytest.fixture
def miller_rabin_obj() -> SchoolMethod:
    mr = MillerRabin(k=50)
    return mr

# Testing SchoolMethod class
@pytest.mark.parametrize("numbers", [10, 100, 1000, 10000, 100000])
def test_SchoolMethod(school_method_obj: SchoolMethod, numbers) -> None:
    list_of_primes = school_method_obj.get_primes(numbers)
    
    if numbers == 10:
        assert 4 == len(list_of_primes)
    if numbers == 100:
        assert 25 == len(list_of_primes)
    if numbers == 1000:
        assert 168 == len(list_of_primes)
    if numbers == 10000:
        assert 1229 == len(list_of_primes)
    if numbers == 100000:
        assert 9592 == len(list_of_primes)

# Testing FermatMethod class
@pytest.mark.parametrize("numbers", [10, 100, 1000, 10000])
def test_FermatMethod(fermat_method_obj: FermatMethod, numbers) -> None:
    list_of_primes = fermat_method_obj.get_primes(numbers)
    
    if numbers == 10:
        assert 4 == len(list_of_primes)
    if numbers == 100:
        assert 25 == len(list_of_primes)
    if numbers == 1000:
        assert 168 == len(list_of_primes)
    if numbers == 10000:
        assert 1229 == len(list_of_primes)

# Testing SieveOfEratosthenes class
@pytest.mark.parametrize("numbers", [10, 100, 1000, 10000, 100000])
def test_SieveOfEratosthenes(sieve_of_eratosthenes_obj: SieveOfSundaram, numbers) -> None:
    list_of_primes = sieve_of_eratosthenes_obj.get_primes(numbers)
    
    if numbers == 10:
        assert 4 == len(list_of_primes)
    if numbers == 100:
        assert 25 == len(list_of_primes)
    if numbers == 1000:
        assert 168 == len(list_of_primes)
    if numbers == 10000:
        assert 1229 == len(list_of_primes)
    if numbers == 100000:
        assert 9592 == len(list_of_primes)

# Testing SieveOfSundaram class
@pytest.mark.parametrize("numbers", [10, 100, 1000, 10000, 100000])
def test_SieveOfSundaram(sieve_of_sundaram_obj: SieveOfSundaram, numbers) -> None:
    list_of_primes = sieve_of_sundaram_obj.get_primes(numbers)
    
    if numbers == 10:
        assert 4 == len(list_of_primes)
    if numbers == 100:
        assert 25 == len(list_of_primes)
    if numbers == 1000:
        assert 168 == len(list_of_primes)
    if numbers == 10000:
        assert 1229 == len(list_of_primes)
    if numbers == 100000:
        assert 9592 == len(list_of_primes)

# Testing MillerRabin class
@pytest.mark.parametrize("numbers", [10, 100, 1000, 10000])
def test_MillerRabin(miller_rabin_obj: MillerRabin, numbers) -> None:
    list_of_primes = miller_rabin_obj.get_primes(numbers)
    
    if numbers == 10:
        assert 4 == len(list_of_primes)
    if numbers == 100:
        assert 25 == len(list_of_primes)
    if numbers == 1000:
        assert 168 == len(list_of_primes)
    if numbers == 10000:
        assert 1229 == len(list_of_primes)





