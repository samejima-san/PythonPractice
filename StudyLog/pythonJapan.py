
import datetime
import pickle
class Person():
    def __init__(self):
        self.lthours = 0
        self.phours = 0
        self.plthours = 0
        self.japhours = 0
        self.japlthours = 0
        self.dhours = 0
        self.dlthours = 0
        self.d = datetime.date.today()

    def addhrsfromsave(self, blankPerson):
        self.lthours = self.lthours + blankPerson[0] + blankPerson[1] + blankPerson[2]
        self.plthours = self.plthours + blankPerson[2]
        self.japlthours = self.japlthours + blankPerson[1]
        self.dlthours = self.dlthours + blankPerson[0]

    def report(self):
        userinput = input('would you like to report some hours? y/n')
        if userinput == 'y':
            userinput = input('for which category? jap, pro, or draw?')
            if userinput == 'jap':
                self.japhours = int(input('how many hours did you study today?'))
                self.japlthours = self.japhours + self.japlthours
                self.lthours = self.lthours + self.japlthours
                print('Wow that is {} lifetime hours in Japanese, GANBARE!'.format(self.japlthours))
                with open('studylog.txt', 'w') as f:
                    f.write("total hours studying: {} \ntotal hours learning japanese: {} \ntotal hours programming: {} \ntotal hours drawing: {} \n {} \nhours today spent learning Japanese: {} \nhours today spent Programming: {} \nhours today spent Drawing: {} \n \n \n ".format(self.lthours, self.japlthours, self.plthours, self.dlthours, self.d, self.japhours, self.phours, self.dhours))
            elif userinput == 'pro':
                self.phours = int(input('how many hours did you study today?'))
                self.plthours = self.phours + self.plthours
                self.lthours = self.lthours + self.plthours
                with open('studylog.txt', 'w') as f:
                    f.write("total hours studying: {} \ntotal hours learning japanese: {} \ntotal hours programming: {} \ntotal hours drawing: {} \n {} \nhours today spent learning Japanese: {} \nhours today spent Programming: {} \nhours today spent Drawing: {} \n \n \n ".format(self.lthours, self.japlthours, self.plthours, self.dlthours, self.d, self.japhours, self.phours, self.dhours))
                print('Wow that is {} lifetime hours in programming!'.format(self.plthours))
            elif userinput == 'draw':
                self.dhours = int(input('how many hours did you draw today?'))
                self.dlthours = self.dhours + self.dlthours
                self.lthours = self.lthours + self.dlthours
                print('Wow that is {} lifetime hours drawing, youre such a loser!'.format(self.dlthours))
                with open('studylog.txt', 'w') as f:
                    f.write("total hours studying: {} \ntotal hours learning japanese: {} \ntotal hours programming: {} \ntotal hours drawing: {} \n {} \nhours today spent learning Japanese: {} \nhours today spent Programming: {} \nhours today spent Drawing: {} \n \n \n ".format(self.lthours, self.japlthours, self.plthours, self.dlthours, self.d, self.japhours, self.phours, self.dhours))
            else:
                print('see you next time.')
            f.close()
  

newPerson = Person()
i = True
savedPerson = None
userInput = input("Do you already have something saved? y/n")
if userInput == "y":
    while i == True:
        oldPerson = pickle.load(open("saveddata.dat", "rb")) #loading data
        newPerson.addhrsfromsave(oldPerson)
        newPerson.report()
        oldPerson = [newPerson.dlthours, newPerson.japlthours, newPerson.plthours]
        pickle.dump(oldPerson, open("saveddata.dat", "wb")) #saving data
        userInput = input("Do you have more hours to report? y/n ")
        if userInput == "n":
            i = False
else:
    while i == True:
        newPerson.report()
        oldPerson = [newPerson.dlthours, newPerson.japlthours, newPerson.plthours]
        pickle.dump(oldPerson, open("saveddata.dat", "wb")) #saving data
        userInput = input("Do you have more hours to report? y/n ")
        if userInput == "n":
            i = False
