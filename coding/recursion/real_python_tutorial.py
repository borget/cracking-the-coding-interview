"""
https://realpython.com/python-recursion/
If you’re familiar with functions in Python, then you know that it’s quite common for one function to call another.
 In Python, it’s also possible for a function to call itself! A function that calls itself is said to be recursive,
  and the technique of employing a recursive function is called recursion.

It may seem peculiar for a function to call itself, but many types of programming problems are best expressed recursively.
 When you bump up against such a problem, recursion is an indispensable tool for you to have in your toolkit.

By the end of this tutorial, you’ll understand:

What it means for a function to call itself recursively
How the design of Python functions supports recursion
What factors to consider when choosing whether or not to solve a problem recursively
How to implement a recursive function in Python
"""


def count_down(n):
    if n <= 0:
        return n
    print(n)
    count_down(n-1)


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


def is_palindrome(word):
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome("civic"))
    # print(factorial(4))
    # count_down(100)
