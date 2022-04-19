class WirelessNetworks:


    BRAND_NAME = "Cisco"

    ADHOC_Mode = "ON"
   
    def __init__(self):
        self.id = ''
        self.oxygenLevel = 0
        self.temperature = 0.0
        self.neighbours = 0
        self.distance = ()
    
    def greetMessage(self):
        print("Welcome to the company's IoT-Based Health System\nThese are sensors of " + self.BRAND_NAME  + " brand, and the Ad Hoc Mode is " + self.ADHOC_Mode + "\n")
        print("*************************************************************")

    def setID(self, Id): #assigns the value of ID
        self.id = Id

    def getID(self):    #Returns the Value of ID
       return self.id


    def setO2(self, o2):    #assigns the value of o2 level
        self.oxygenLevel = o2

    def setTemp(self, temp):    #assigns the value of temp
        self.temperature = temp

    def setNeighbours(self, neighbours):    #assigns the value of neighbours
        self.neighbours = neighbours