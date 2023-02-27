from solution import SOLUTION
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import matplotlib.pyplot as plt

scores = []

for seed in range(1, 6):
   phc = PARALLEL_HILL_CLIMBER(1)
   phc.Evolve()
   scores.append(phc.GetAllFitnesses())
   plt.plot(phc.GetAllFitnesses(), label = "Seed " + str(seed))
   # phc.Show_Best()

plt.legend()
plt.show()

# run = SOLUTION(0)
# run.Start_Simulation()