def geometric(n, p, pdf=True):
    """
    Geometric distribution: A special case of negative distribution
    :param n: Total number of trials
    :param p: Probability of success
    :param pdf: Probability Density Function; if True then calculates probability for that number of trial
                else it calculates cumulative probability of first success in first n trials
    :return: It calculates probability of "first" success on given trial
    """
    if pdf:
        return ((1-p) ** (n-1)) * p
    else:
        return sum([geometric(i, p) for i in range(1, n+1)])


print('Probability of first success on fifth trial: {0}'.format(geometric(5, 0.7)))
print('Probability of first success in first five trials: {0}'.format(geometric(5, 0.7, pdf=False)))

