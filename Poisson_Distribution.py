"""
Poisson  Distribution
"""


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def poisson(lamb, k, pdf= True):
    """
    Poisson Distribution
    :param lamb: Average number of success that occur in a specified region
    :param k: Number of  success that occur in a specified region
    :param pdf: Probability Distribution Function;if false then calculates cumulative probability of at-least k occurrence
    :return: Probability of k occurrence
    """
    e = 2.718281
    if pdf:
        return (pow(e, -lamb) * pow(lamb, k)) / factorial(k)
    else:
        return sum([(pow(e, -lamb) * pow(lamb, i)) / factorial(i) for i in range(0, k + 1)])


# Average Number of patients seen in a clinic is 73 each day
print('Probability of seeing 80 patients on next day: {}'.format(poisson(73, 80)))
print('Probability of seeing at-least 80 patients on next day: {}'.format(poisson(73, 80, pdf=False)))
print('Probability of seeing more than 80 patients on next day: {}'.format(1-poisson(73, 80, pdf=False)))
