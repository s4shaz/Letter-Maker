# Program to print an application using the template and input values
from datetime import datetime
from string import Template
date= datetime.now().strftime("%d %B, %Y")
#This function takes user input and types the letter
def writeLetter():
    type=int(input("Type of application letter? 1. Application to school principle for leave 2. Letter to the editor: "))
    #Letter for school application
    if (type==1):
        #Set of input data
        name=input("Enter your full name: ")
        school=input("Enter school name (with city): ")
        school=school.title()
        days=input("How many days of leave?: ")
        clas=input("Current class of student? (0 to skip): ")
        reason=int(input("Reason for leave? 1. Sick & 2. Family Occasion: "))
        #Application for sick leave
        if (reason==1):
            if (clas=='0'):
                template= Template("To, \nThe Principal \n$schl \n$dt \nRe: Application for leave of $d days \nDear Sir, \nWith due respect, this is to inform you that I, $nm studying in your school has been suffering from cold and fever from the last few days. The doctor has advised me to take a rest for $d days. \nIt is my humble request to please grant me this leave for $d days and I would be really obliged to you. \nThanking you, \nYours respectfully \n$nm")
                template = template.substitute(nm=name, dt=date, d=days, schl=school)
                print(template)
            else:
                template= Template("To, \nThe Principal \n$schl \n$dt \nRe: Application for leave of $d days \nDear Sir/Ma'am, \nWith due respect, this is to inform you that I, $nm studying in your school has been suffering from cold and fever from the last few days. The doctor has advised me to take a rest for $d days. \nIt is my humble request to please grant me this leave for $d days and I would be really obliged to you. \nThanking you, \nYours respectfully \n$nm \nClass $cl")
                template = template.substitute(nm=name, dt=date, d=days, schl=school, cl=clas)
                print(template)
        #Application for family occasion 
        elif (reason==2):
            if (clas=='0'):
                template=Template("To, \nThe Principal \n$schl \n$dt \nRe: Leave application for a family function. \nDear Sir/Ma'am \nI, $nm, am a student of your school. With due respect I inform you that I am going out of station for $d days to attend a family function. Therefore, I will not be able to attend the school for the upcoming $d days. As it is a family function of great importance, my presence is expected. Therefore, kindly grant me $d days leave. \nI shall be immensely obliged to you. I promise to not let this leave affect my studies. \nYours sincerely \n$nm")
                template = template.substitute(nm=name, dt=date, d=days, schl=school)
                print(template)
            else:
                template=Template("To, \nThe Principal \n$schl \n$dt \nRe: Leave application for a family function. \nDear Sir/Ma'am \nI, $nm, am a student of class $cl studying in your school. With due respect I inform you that I am going out of station for $d days to attend a family function. Therefore, I will not be able to attend the school for the upcoming $d days. As it is a family function of great importance, my presence is expected. Therefore, kindly grant me $d days leave. \nI shall be immensely obliged to you. I promise to not let this leave affect my studies. \nYours sincerely \n$nm \n$cl")
                print(template)
        else:
            ask=input("Wrong value enter! Try again? (y/n)")
            ask=ask.lower()
            if (ask=='y'):
                writeLetter()
            else:
                print("Have a nice day!")
    elif (type==2):
        ask=input("Letter to editor is still in development. Try again? (y/n)")
        if (ask=='y'):
            writeLetter()
        else:
            print("Have a nice day!")
    else:
        ask=input("Letter to editor is still in development. Try again? (y/n)")
        if (ask=='y'):
            writeLetter()
        else:
            print("Have a nice day!")


if __name__=='__main__':
    writeLetter()       