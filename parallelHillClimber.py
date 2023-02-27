import copy
from solution import SOLUTION
import constants as c
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
   def __init__(self):
      os.system("rm brain*.nndf")
      os.system("rm fitness*.nndf")

      self.parents = {}
      self.nextAvailableID = 0
      for i in range(c.populationSize):
         self.parents[i] = SOLUTION(self.nextAvailableID)
         self.nextAvailableID += 1
      self.parents[0].Start_Simulation("GUI")
      self.fitnessByGeneration = []
   
   def Evolve(self):
      self.Evalulate(self.parents)
      for currentGeneration in range(c.numberOfGenerations):
         print('### STARTING GENERATION', currentGeneration+1, '/', c.numberOfGenerations)
         self.Evolve_For_One_Generation()

   def Evolve_For_One_Generation(self):
      self.Spawn()
      self.Mutate()
      self.Evalulate(self.children)
      # self.Print()
      self.Select()

   def Spawn(self):
      self.children = {}
      for i in range(len(self.parents)):
         self.children[i] = copy.deepcopy(self.parents[i])
         self.children[i].Set_ID(self.nextAvailableID)
         self.nextAvailableID += 1

   def Mutate(self):
      for i in self.children:
         self.children[i].Mutate()

   def Select(self):
      best = self.parents[0].fitness

      for i in self.children:
         best = min(best, self.children[i].fitness, self.parents[i].fitness)
         if self.children[i].fitness < self.parents[i].fitness:
            self.parents[i] = self.children[i]
      print('BEST FITNESS:', best)
      self.fitnessByGeneration.append(-best)
   
   def Evalulate(self, solutions):
      for i in solutions:
         solutions[i].Start_Simulation("DIRECT")
      for i in solutions:
         solutions[i].Wait_For_Simulation_To_End()

   def Print(self):
      for i in self.parents:
         print("FITNESS:", self.parents[i].fitness, self.children[i].fitness)
   
   def Show_Best(self):
      minIndex = 0
      minVal = self.parents[0].fitness
      for i in self.parents:
         if self.parents[i].fitness < minVal:
            minVal = self.parents[i].fitness
            minIndex = i
      print('FINAL FITNESS:', self.parents[minIndex].fitness, '\n')
      self.parents[minIndex].Start_Simulation("GUI")
   
   def GetAllFitnesses(self):
      return self.fitnessByGeneration
