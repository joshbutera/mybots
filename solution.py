import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import numpy as np
import constants as c

class SOLUTION:
   def __init__(self, myID):
      # np.random.seed(seed)
      self.numLinks = 13
      self.hasSensor = np.random.randint(0,2,self.numLinks)
      self.weights = np.random.rand(self.numLinks,self.numLinks-1) * 2 - 1
      self.connections = [set() for i in range(self.numLinks)]
      self.myID = myID

      self.dimensions = [
         [2 + np.random.rand() * .1 - 0.05,0.8 + np.random.rand() * .1- 0.05,0.6 + np.random.rand() * .1- 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.3 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.5 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.75 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.3 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.5 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.75 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.3 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.5 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.75 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.3 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.5 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05],
         [0.2 + np.random.rand() * .1 - 0.05,0.2 + np.random.rand() * .1 - 0.05,0.75 + np.random.rand() * .1 - 0.05]
      ]

      self.colors = []
      for i in self.hasSensor:
         if i:
            self.colors.append("green")
         else:
            self.colors.append("blue")
      
      self.connections = [set() for i in range(self.numLinks)]

      # give every cube a set of all possible directions (i.e [1, 0, 0], [0, -1, 0]) and remove directions whenever joint is connected in that direction
      # joint will pick random direction from set
   
   def Create_World(self):
      pyrosim.Start_SDF("world.sdf")
      pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
      pyrosim.End()

   def Create_Body(self):
      pyrosim.Start_URDF("body.urdf")
      initialHeight = 1
      pyrosim.Send_Cube(name='Cube0', pos=[0,0,initialHeight] , size=self.dimensions[0], color=self.colors[0])
      # pyrosim.Send_Cube(name='Cube0', pos=[0,0,5] , size=self.dimensions[0], color=self.colors[0])

      pyrosim.Send_Joint( name = "Cube0_Cube1" , parent= "Cube0" , child = "Cube1" , type = "revolute", position = [-self.dimensions[0][1]*2/5,self.dimensions[1][1]/3,initialHeight], jointAxis = "0 1 0")
      self.connections[0].add(1)
      pyrosim.Send_Cube(name="Cube1", pos=[0,self.dimensions[0][1]/2,0] , size=self.dimensions[1], color=self.colors[1])
      pyrosim.Send_Joint( name = "Cube1_Cube2" , parent= "Cube1" , child = "Cube2" , type = "revolute", position = [self.dimensions[1][0],2*self.dimensions[1][1],0], jointAxis = "0 1 0")
      self.connections[1].add(2)
      pyrosim.Send_Cube(name="Cube2", pos=[0,0,0] , size=self.dimensions[2], color=self.colors[2])
      pyrosim.Send_Joint( name = "Cube2_Cube3" , parent= "Cube2" , child = "Cube3" , type = "revolute", position = [self.dimensions[2][0]/4,0,-initialHeight/2], jointAxis = "0 1 0")
      self.connections[2].add(3)
      pyrosim.Send_Cube(name="Cube3", pos=[0,0,0] , size=self.dimensions[3], color=self.colors[3])
      
      pyrosim.Send_Joint( name = 'Cube0_Cube4' , parent= 'Cube0' , child = 'Cube4' , type = 'revolute', position = [-self.dimensions[0][1]*2/5,-self.dimensions[4][1]/3,initialHeight], jointAxis = "0 1 0")
      self.connections[0].add(4)
      pyrosim.Send_Cube(name='Cube4', pos=[0,-self.dimensions[0][1]/2,0] , size=self.dimensions[4], color=self.colors[4])
      pyrosim.Send_Joint( name = 'Cube4_Cube5' , parent= 'Cube4' , child = 'Cube5' , type = 'revolute', position = [self.dimensions[4][0],-2*self.dimensions[4][1],0], jointAxis = "0 1 0")
      self.connections[4].add(5)
      pyrosim.Send_Cube(name='Cube5', pos=[0,0,0] , size=self.dimensions[5], color=self.colors[5])
      pyrosim.Send_Joint( name = 'Cube5_Cube6' , parent= 'Cube5' , child = 'Cube6' , type = 'revolute', position = [self.dimensions[5][0]/4,0,-initialHeight/2], jointAxis = "0 1 0")
      self.connections[5].add(6)
      pyrosim.Send_Cube(name='Cube6', pos=[0,0,0] , size=self.dimensions[6], color=self.colors[6])
      
      pyrosim.Send_Joint( name = 'Cube0_Cube7' , parent= 'Cube0' , child = 'Cube7' , type = 'revolute', position = [self.dimensions[0][1]*2/5,-self.dimensions[4][1]/3,initialHeight], jointAxis = "0 1 0")
      self.connections[0].add(7)
      pyrosim.Send_Cube(name='Cube7', pos=[0,self.dimensions[0][1]/2,0] , size=self.dimensions[7], color=self.colors[7])
      pyrosim.Send_Joint( name = 'Cube7_Cube8' , parent= 'Cube7' , child = 'Cube8' , type = 'revolute', position = [self.dimensions[7][0],2*self.dimensions[7][1],0], jointAxis = "0 1 0")
      self.connections[7].add(8)
      pyrosim.Send_Cube(name='Cube8', pos=[0,0,0] , size=self.dimensions[8], color=self.colors[8])
      pyrosim.Send_Joint( name = 'Cube8_Cube9' , parent= 'Cube8' , child = 'Cube9' , type = 'revolute', position = [self.dimensions[8][0]/4,0,-initialHeight/2], jointAxis = "0 1 0")
      self.connections[8].add(9)
      pyrosim.Send_Cube(name='Cube9', pos=[0,0,0] , size=self.dimensions[9], color=self.colors[9])
      
      pyrosim.Send_Joint( name = 'Cube0_Cube10' , parent= 'Cube0' , child = 'Cube10' , type = 'revolute', position = [self.dimensions[0][1]*2/5,self.dimensions[4][1]/3,initialHeight], jointAxis = "0 1 0")
      self.connections[0].add(10)
      pyrosim.Send_Cube(name='Cube10', pos=[0,-self.dimensions[0][1]/2,0] , size=self.dimensions[10], color=self.colors[10])
      pyrosim.Send_Joint( name = 'Cube10_Cube11' , parent= 'Cube10' , child = 'Cube11' , type = 'revolute', position = [self.dimensions[10][0],-2*self.dimensions[10][1],0], jointAxis = "0 1 0")
      self.connections[10].add(11)
      pyrosim.Send_Cube(name='Cube11', pos=[0,0,0] , size=self.dimensions[11], color=self.colors[11])
      pyrosim.Send_Joint( name = 'Cube11_Cube12' , parent= 'Cube11' , child = 'Cube12' , type = 'revolute', position = [self.dimensions[11][0]/4,0,-initialHeight/2], jointAxis = "0 1 0")
      self.connections[11].add(12)
      pyrosim.Send_Cube(name='Cube12', pos=[0,0,0] , size=self.dimensions[12], color=self.colors[12])

      pyrosim.End()

   def Create_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

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

      temp = 0
      for source in range(0, self.numLinks):
         if self.hasSensor[source] == 1:
            for target in range(self.numLinks-1):
               pyrosim.Send_Synapse( sourceNeuronName = temp , targetNeuronName = target+curr , weight = self.weights[source][target] )
            temp += 1

      pyrosim.End()

   def Start_Simulation(self, directOrGUI):
      self.Create_World()
      self.Create_Body()
      self.Create_Brain()
      os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

   def Wait_For_Simulation_To_End(self):
      while not os.path.exists("fitness" + str(self.myID) + ".txt"):
         time.sleep(0.01)
      f = open("fitness" + str(self.myID) + ".txt", "r")
      self.fitness = float(f.read())
      os.system("rm fitness" + str(self.myID) + ".txt")

   def Mutate(self):
      randomRow = np.random.randint(0,self.numLinks-1)
      randomCol = np.random.randint(0,self.numLinks-2)
      self.weights[randomRow][randomCol] = random.random() * 2 - 1
      randomLink = np.random.randint(0,self.numLinks-1)
      self.dimensions[randomLink][np.random.randint(0,2)] += np.random.rand()/10 - 0.05

   def Set_ID(self, id):
      self.myID = id
