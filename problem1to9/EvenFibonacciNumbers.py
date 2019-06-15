from Fibonacci import *
def EvenFibonacciNumbers(UpTo=4000000):
    return sum([i for i in Fibonacci(1,2,UpTo) if i%2==0])
