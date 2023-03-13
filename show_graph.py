from numpy import loadtxt
import matplotlib.pyplot as plt

data = loadtxt('data.csv', delimiter=',')

for i in range(len(data)):
    plt.plot(data[i], label = "Seed" + str(i+1))


plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Fitness vs. Generation')
plt.legend()
plt.show()