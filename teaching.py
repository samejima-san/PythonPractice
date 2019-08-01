#what are the names of the 4 data types, write them in comments next to them
variable = "Luis" #String 
variable = 1 #Interger 
variable = 0.0 #Float 
variable = True #Boolean

#What is this block of code called?
def Blank(): #function
    return

#What is the difference between these two variables
variable = 1
variable = "1"

#What will this output
variable = "1"

if(variable == 1):
    print("Yo")
elif(variable == "1"):#This one!
    print("Yo but different")
else:
    print("Literally anything different")

#What will this output
variable = 1 #or True
#0 = false

if(variable == True):#This one
    print("Pick me!")
else:
    print("no pick me")

#What will happen here
variable = 3

if(variable == 3):
    print("Hello")
if(variable > 0):
    print("world")
else:
    print("how are you")
#it will print hello world

#What will this print
k = 1 + 4 * 3
print(k)
#print 13 according to pemdas

#What is this called?
hello = [1,2,3,4,5,6] #list

#what will this do?
returnvalue = hello.pop() #takes things out of your list
print(returnvalue)
print(hello)

#What will this do?
hello.append(7) #Add things to the list
print(hello)

#Explain the lines of this 
class Player():
    def __init__(self,name,health,speed,defence): #Constructor
        self.name = name
        self.health = health
        self.speed = speed
        self.defence = defence
        self.mana = 100.0
        self.multiplyer = 1.0
        self.isBlocking = False
        self.isAlive = True #setting all the players variables
        
    def Attack(self, other):#Why do we add "self" in our functions for classes?
        if(self.speed > other.speed):#because you want to effect this classes attributes/variables
            other.health -= 5 * self.multiplyer
        else:
            other.health -= 2 * self.multiplyer

    def TakeDamage(self, other):
        if(self.isBlocking == True):
            self.health -= other.attack * .5
        else:
            self.health -= other.attack

    def Block(self):
        self.isBlocking = True

    def SlowSpell(self, other):
        self.mana -= 5.0
        other.speed -= 20

    def DamageBoost(self):
        self.mana -= 10.0
        self.multiplyer = 3.0

    def death(self):
        if(self.health <= 0):
            self.isAlive = False


Aaron = Player("Aaron",150,75,100)
Rose = Player("Rose", 75, 200, 75)
Luis = Player("Luis", 250, 50, 50)
Eric = Player("Eric", 100,100,100) #creating players

party = [Eric, Luis, Rose, Aaron] #list of players


#What is this called and what does it do?
num = 0 
while True: #While loop
    print(num)
    num += 1 #count to infinity

#What will this do
for player in party: #for loop
    print("Hey, my name is {} and I have a speed of {} i am kind of a big deal".format(player.name, player.speed))




#If you understand all of this congrats! you're a beginner at python!
#Its time to brainstorm on projects that YOU want to complete
#Use these basics to have at it and complete your goals
#Whether you want to make games or website or apps the world is yours
