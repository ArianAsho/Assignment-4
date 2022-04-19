
from  wirelessNetwork import WirelessNetworks #imports wirelessnetwork class

class Application: 
   def __init__(self): 
      self.listSens = []
      self.total = 0
      self.senDictionary = {}

      #imports the greetMessage method from wirelessNetworks
      net = WirelessNetworks()
      net.greetMessage()


      self.createSensors()
   
   #prints out a line to split the code
   def split(self):
      print("_*__*__*__*__*__*__*__*__*__*__*_")

   #this method is to create the sensors
   def createSensors(self):

      while True:
         #checks to see if the input that the user has put in is a number and nothing else
         try:
            numberOfSensors = int(input("Enter the number of sensors: "))
            break #breaks the loop after it sees the input is an int
         #if it is not a number it will ask for the user to input again
         except:
            print("This is an invalid entry for the number of sensors")
      self.totalSens(numberOfSensors)

      self.split()


      for sen in range(1, self.total + 1):   #checks to see if we have reached the max sensors and keeps going until it reaches it
         sen = WirelessNetworks()            

         #asks for the ID of the sensor
         id = (input("Enter the sensor ID: "))
         #loop to see if the id is a letter and nothing else
         while any(char.isdigit() for char in id):
            print("This is an invalid entry for the neighbour's name and/or distance!")
            id = input("Enter the sensor ID: ")
         sen.setID(id)
         
         #asks for the number of neighbours and checks to see if it is an int and keeps asking until it gets the right answer
         while True:
            try:
               numberOfNeighbours = int(input("Enter the number of neighbours: "))
               break
            except:
               print("This is an invalid entry for the number of neighbours")
         sen.setNeighbours(numberOfNeighbours)

         #checks to see if we have reached the max neighbours for the sensor and keeps going until it reaches it
         for neighbour in range(1, sen.neighbours + 1):
            neighbour = WirelessNetworks()

            #checks to see if the neighbourID is a letter and nothing else.
            neighbourId = input("Enter the neighbour for sensor " + sen.id + ": ")
            while any(char.isalpha() == False for char in neighbourId ):
               print("This is an invalid entry for the neighbour's name and/or distance!")
               neighbourId = input("Enter the neighbour for sensor " + sen.id + ": ")
            neighbour.setID(neighbourId)
         

            self.convrtToDict(sen, neighbour) 

      #asks for the o2 levels
         while True:
            try:
               o2 = int(input("Enter the Oxygen level in %: "))
               break
            except:
               print("This is an invalid entry for the oxygen level!")

         sen.setO2(o2)

   #asks for the temperture levels
         while True:

            try:
               temp = float(input("Enter the temperature measurement: "))
               break
            except:
               print("This is an invalid entry for the temperature!")

         sen.setTemp(temp)

         self.listSens.append(sen)
         self.split()

      self.findPath()
         

     #converts it to dictionary       
   def convrtToDict(self, sen, neighbour):

      m = (neighbour.id, int(input("Enter the distance to " + sen.id + ": ")))

      if sen.id not in self.senDictionary:

         self.senDictionary[sen.id] = [m]

      else:

         self.senDictionary[sen.id].append(m)
      
      #Find the path from the source to the destinations
   def findPath(self):
      source = input("Enter the source sensor: ")
      path = [source]
      target = input("Enter the destination sensor: ")
      try:
         self.pathFinder(target, source, path)
         print("Path= ",path)
      except RecursionError:
         print("The destination is not found")
      
   def pathFinder(self, target, source, path):
      if target == source:
         return(True)
      max = self.senDictionary[source][0]
      for id, m in self.senDictionary[source]:
         if m > max[1]:
            max = (id, m)
      path.append(max[0])
      return(self.pathFinder(max[0], target, path))

   def totalSens(self, count):
      self.total = count

Application()