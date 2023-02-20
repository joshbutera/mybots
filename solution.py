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
      self.dimensions = (np.random.rand(self.numLinks, 3) + 0.5)
      self.hasSensor = np.random.randint(0,2,self.numLinks)
      self.connections = [[] for i in range(self.numLinks)]

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
      pyrosim.Send_Cube(name='Cube0', pos=[0,0,self.maxHeight], size=self.dimensions[0], color=color)

      for i in range(1, self.numLinks):
         color = "blue"
         if self.hasSensor[i] == 1:
            color = "green"
         self.connections[i-1].append(i)

         temp = np.random.randint(0,3)
         position = [0, 0, 0]
         position[temp] = self.dimensions[i-1][temp] * random.choice([-1, 1])

         pyrosim.Send_Joint(name='Cube'+str(i-1)+'_Cube'+str(i), parent='Cube'+str(i-1), child='Cube'+str(i), type='revolute', position=position, jointAxis="1 0 0")
         pyrosim.Send_Cube(name='Cube'+str(i), pos=[0,0,self.maxHeight/2], size=self.dimensions[i], color=color)

      pyrosim.End()

   def Create_Brain(self):
      pyrosim.Start_NeuralNetwork("brain.nndf")

      curr = 0
      for i in range(self.numLinks):
         if self.hasSensor[i] == 1:
            pyrosim.Send_Sensor_Neuron(name = curr, linkName='Cube'+str(i))
            curr += 1

      temp = curr
      for i in range(len(self.connections)):
         for j in self.connections[i]:
            pyrosim.Send_Motor_Neuron( name = temp , jointName = 'Cube'+str(i)+'_Cube'+str(j))
            temp += 1

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
