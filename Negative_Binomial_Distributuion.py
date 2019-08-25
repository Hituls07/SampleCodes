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


def neg_binomial(x, n, p, pdf=True):
    """
    Negative Binomial Distribution
    Assumptions: Trials are independent and each trial is either success or failure
    :param x: The number of success to be observed
    :param n: Total number of trials required to produce x successes in a negative binomial experiment
    :param p: The probability of success on an individual trial
    :param pdf: Probability Density Function; if false then cumulative probability of rth success in first n trials
    :return: It calculates probability of xth success in nth trial
    """
    if pdf:
        return Combination(n-1, x-1) * pow(p, x) * pow(1-p, n-x)
    else:
        return sum([Combination(i-1, x-1) * pow(p, x) * pow(1-p, i-x) for i in range(1, n + 1)])


