from solution import SOLUTION
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import matplotlib.pyplot as plt
from numpy import savetxt

data = []

for seed in range(1, 11):
   phc = PARALLEL_HILL_CLIMBER(seed)
   phc.Evolve()
   data.append(phc.GetAllFitnesses())
   phc.Show_Best()

savetxt('data.csv', data, delimiter=',')

# run = SOLUTION(0)
# run.Start_Simulation()