# yes we can change the self in this code an nothing will happen unless we aslo dont change self. to the word we have use as a input.

from random import randint

class Train:

    def __init__(self,TrainNo):
        self.TrainNo = TrainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.TrainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.TrainNo} is Running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no:{self.TrainNo}from{fro}to {to} is {randint(222,5555,)}")


t =Train(1239)
t.book("Rampur","Delhi")
t.getstatus()
t.getFare("Rampur","Delhi")



