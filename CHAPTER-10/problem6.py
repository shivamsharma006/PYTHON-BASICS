'''
 Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.'''

# Yes, We Can you change the self-parameter inside a class to something else.

import random
class Train:

    def __init__(sel,trainno):
        sel.trainno = trainno

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainno} from {fro} to {to}") 
        
    def getStatus(self):
        print(f"Train no is: {self.trainno}")

    def getFair(self,fro,to):
        print(f"Ticket fair in train no: {self.trainno} from {fro} to {to} is {random.randint(200,1000)}")

        

t = Train(23441)
t.book("Aligarh","Delhi")
t.getStatus()
t.getFair("Aligarh","Delhi")