def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


numbers = list(map(int, input().split()))
print(filter_prime(numbers))