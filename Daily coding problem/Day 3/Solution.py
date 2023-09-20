def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


pair = cons("a", "b")


def car(a, b):
    return a


def cdr(a, b):
    return b


print(pair(car))
print(pair(cdr))

# Explanation:
"""
The cons(a, b) function in this context is not a traditional "constructor" 
that creates pairs in the way you might expect in a typical programming language. Instead, it's 
implemented as a higher-order function that returns another function, often referred to as a closure or 
lambda function.

>>> Here's a step-by-step explanation of how cons(a, b) works:

- When you call cons(a, b) with two arguments, a and b, it creates a function pair(f) that takes 
 another function f as its argument. This inner function, pair, is returned as the result of calling 
 cons(a, b).

- The pair(f) function, when called with a function f, evaluates f(a, b) and returns the result of 
that evaluation.

- Essentially, pair acts as a function that "wraps" the values a and b. When you call pair(f) with a 
function f, it applies f to a and b and returns the result.

So, cons(a, b) effectively creates a container (a function) that can be opened with different functions 
(keys) to access its values (a and b). This concept is similar to closures in functional programming, 
where a function captures its surrounding state (in this case, a and b) and allows you to access that state
later by invoking the function with different "keys" (functions).

"""
