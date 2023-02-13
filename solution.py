import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import numpy as np
import constants as c

class SOLUTION:
   def __init__(self):
      self.numLinks = np.random.randint(3,10)
      self.dimensions = (np.random.rand(self.numLinks, 3).round(1) + 0.5) * 2
      self.hasSensor = np.random.randint(0,2,self.numLinks)

      self.maxHeight = self.dimensions[0][2]
      for dim in self.dimensions:
         self.maxHeight = max(self.maxHeight, dim[2])
   
   def Create_World(self):
      pyrosim.Start_SDF("world.sdf")
      pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
      pyrosim.End()

   def Create_Body(self):
      pyrosim.Start_URDF("body.urdf")

      color = "blue"
      if self.hasSensor[0] == 1:
            color = "green"
      pyrosim.Send_Cube(name='Cube0', pos=[0,0,self.maxHeight/2], size=self.dimensions[0], color=color)
      pyrosim.Send_Joint(name='Cube0_Cube1', parent='Cube0', child='Cube1', type='revolute', position=[0,self.dimensions[0][1]/2,0], jointAxis="1 0 0")

      for i in range(1, self.numLinks-1):
         color = "blue"
         if self.hasSensor[i] == 1:
            color = "green"
         pyrosim.Send_Cube(name='Cube'+str(i), pos=[0,self.dimensions[i][1]/2,self.maxHeight/2], size=self.dimensions[i], color=color)
         pyrosim.Send_Joint(name='Cube'+str(i)+'_Cube'+str(i+1), parent='Cube'+str(i), child='Cube'+str(i+1), type='revolute', position=[0,self.dimensions[i][1],0], jointAxis="1 0 0")
      
      color = "blue"
      if self.hasSensor[self.numLinks-1] == 1:
         color = "green"
      pyrosim.Send_Cube(name='Cube'+str(self.numLinks-1), pos=[0,self.dimensions[self.numLinks-1][1]/2,self.maxHeight/2], size=self.dimensions[self.numLinks-1], color=color)

      pyrosim.End()

   def Create_Brain(self):
      pyrosim.Start_NeuralNetwork("brain.nndf")

      curr = 0
      for i in range(self.numLinks):
         if self.hasSensor[i] == 1:
            pyrosim.Send_Sensor_Neuron(name = curr, linkName='Cube'+str(i))
            curr += 1

      for i in range(self.numLinks-1):
         pyrosim.Send_Motor_Neuron( name = i+curr , jointName = 'Cube'+str(i)+'_Cube'+str(i+1))

      for i in range(self.numLinks):
         if self.hasSensor[i] == 1:
            for j in range(self.numLinks-1):
               pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j+curr , weight = np.random.rand() * 2 - 1 )

      pyrosim.End()

   def Start_Simulation(self):
      self.Create_World()
      self.Create_Body()
      self.Create_Brain()
      os.system("python3 simulate.py " + "GUI" + " 2&>1 &")

   def Set_ID(self, id):
      self.myID = id
