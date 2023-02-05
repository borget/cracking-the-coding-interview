"""
For all 6 digit numbers ABCDEF,
-- 100000-999999

239133

find the numbers that satisfy the following equation: (ABC+DEF)^2=ABCDEF


123456 ->(123+456)^2 =579^2=335241

123456 <> 335241 -- false
"""


def find_numbers():
    numbers = []

    for num in range(100000, 999999):
        left = int(num/1000)
        right = int(num % 1000)
        sqr_val = (left+right)**2

        if num == sqr_val:
            numbers.append(num)

    return numbers


if __name__ == "__main__":
    result = find_numbers()
    print(result)
