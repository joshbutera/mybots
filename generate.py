import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length, width, height = 1, 1, 1
x, y, z = 0, 0, height/2


for x in range(0, 5):
   for y in range(0, 5):
      length, width, height = 1, 1, 1
      for i in range(0, 10):
         pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z+i] , size=[length,width,height])
         length *= 0.9
         width *= 0.9
         height *= 0.9

pyrosim.End()