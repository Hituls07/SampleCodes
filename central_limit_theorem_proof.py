import random
import matplotlib.pyplot as plt

s1 = random.sample(range(1,10000), 100)
s2 = random.sample(range(1,10000), 100)
s3 = random.sample(range(1,10000), 100)


rand_samp_mean =[]
for i in range(100):
    for population in  [s1, s2, s3]:
        rand_samp_mean.append(sum(random.sample(population, 4)) / 4)



labels = ['s1', 's2', 's3', 'Normal Distribution']
plt.figure(figsize= (10, 10))
index = 0
for i in [s1, s2, s3, rand_samp_mean]:
    plt.subplot(2, 2, index + 1)
    plt.hist(i)
    plt.title(labels[index])
    index += 1

plt.show()
