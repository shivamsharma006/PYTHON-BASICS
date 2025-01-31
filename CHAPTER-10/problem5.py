'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways'''
import random
class Train:

    def __init__(self,trainno):
        self.trainno = trainno

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainno} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train no is: {self.trainno}")

    def getFair(self,fro,to):
        print(f"Ticket fair in train no: {self.trainno} from {fro} to {to} is {random.randint(200,1000)}")

        

t = Train(23441)
t.book("Aligarh","Delhi")
t.getStatus()
t.getFair("Aligarh","Delhi")
