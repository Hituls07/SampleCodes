# import matplotlib.pyplot as plt


def factorial(num):
    if  num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def Combination(upper, lower):

    result = (1 / factorial(lower))
    for i in range(upper , upper-lower, -1):
        result *= i

    return result


def Binomial(n,x,p,pdf=True):

    """
    Binomial distribution
    :param n: Random Sample of n items
    :param x: number of times event x occur
    :param p: probability of event x occurrence
    :pdf: Probability Distribution Function, if False then calculates probability of at-least x occurrence
    :return: result of binomial distribution
    """
    if pdf:
        return Combination(n, x) * (p**x) * ((1-p)**(n-x))
    else:
        prod = 0
        for num in range(x + 1):
            prod += Combination(n, num) * (p**num) * ((1-p)**(n-num))

        return prod


# A fair coin tossed 5 times

# Probability of getting 5 heads
print(Binomial(10,5, 0.5))

# Probability of getting at most 5 heads
print(sum([Binomial(10, i, 0.5) for i in range(5, 11)]))

# Probability of getting at-least 5 heads
print(Binomial(10, 5, 0.5) + 1 - Binomial(10, 5, 0.5, pdf=False))