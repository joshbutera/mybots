import copy
from solution import SOLUTION
import constants as c
import os

class HILL_CLIMBER:
   def __init__(self):
      self.parent = SOLUTION()
   
   def Evolve(self):
      self.parent.Evalulate()
      os.system("python3 simulate.py GUI")
      for currentGeneration in range(c.numberOfGenerations):
         self.Evolve_For_One_Generation()

   def Evolve_For_One_Generation(self):
      self.Spawn()
      self.Mutate()
      self.child.Evalulate()
      self.Print()
      self.Select()

   def Spawn(self):
      self.child = copy.deepcopy(self.parent)

   def Mutate(self):
      self.child.Mutate()

   def Select(self):
      if self.child.fitness > self.parent.fitness:
         self.parent = self.child

   def Print(self):
      print("FITNESS:", self.parent.fitness, self.child.fitness)
   
   def Show_Best(self):
      os.system("python3 simulate.py GUI")
