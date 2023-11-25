class Garage():
    
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.t = 0
        self.parkingSpaces = parkingSpaces
        self.p = 0
        self.currentTicket = currentTicket
        self.total_tickets = len(self.tickets)
        self.total_spaces = len(self.parkingSpaces)
        self.pay = 0
    
    def takeTicket(self):
        
        print("\nPlease take a ticket!")
    
        self.t = self.tickets.pop(0)
        print(f"\nYou are ticket number {self.t}.")

        self.p = self.parkingSpaces.pop(0)
        print(f"\nYou have parking space number {self.p}.")

    def decreaseTicket(self):
        self.total_tickets -= 1
        
    def decreaseSpace(self):
        self.total_spaces -= 1

    def payForParking(self):
        print("\nPay the ticket, here! ")
        parking_garage.ticketAmount()


    def ticketAmount(self):
        self.pay = int(input("\nPlease display payment amount: "))
        parking_garage.ticketPaid()

    def ticketPaid(self):
        
        if self.pay == 5:
            parking_garage.updateTickets()
            print("Your ticket has been paid, you have 15 min to leave.")
            parking_garage.displayMessage()
            parking_garage.leaveGarage()
            
        else:
           print("\nWrong amount! Please pay the ticket!")
           parking_garage.displayPayment()
        
    def updateTickets(self):

        if self.pay == 5:
            self.currentTicket["Paid"] = True
            
            if self.currentTicket["Paid"] == True:
                print("\nPaid is valid")
        
        elif self.currentTicket["Paid"] == False:
            print("\nWelcome to our parking garage!")

    def leaveGarage(self):
        
        print("Please leave garage!")
        parking_garage.increaseSpace()
        parking_garage.increaseTicket()
        self.pay = 0
        run()

    def displayMessage(self):

        if self.pay == 5:
            print("\nThank You, have a nice day! ")
    
    def displayPayment(self):
        if self.pay != 5:
            
            self.pay = int(input("\nPlease display payment amount: "))
            parking_garage.displayThankyou()
   
    def displayThankyou(self):

        if self.pay == 5:
            parking_garage.updateTickets()
            parking_garage.displayMessage()
            parking_garage.leaveGarage()

        else:
            print("\nWrong amount! Please pay the ticket!")
            parking_garage.displayPayment()
      
    def increaseSpace(self):
        self.total_spaces += 1
        self.parkingSpaces.append(self.p)


    def increaseTicket(self):
        self.total_tickets += 1
        self.tickets.append(self.t)
        

ticket_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

spaces_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

ticket_price = {"Paid": False}


parking_garage = Garage(ticket_list, spaces_list, ticket_price)


def run():
    
    ticket_price["Paid"] = False
    parking_garage.updateTickets()

    while True:
        use = input("\nWant to use parking garage? ")

        if use.lower() == "yes":
        
            parking_garage.takeTicket()
            parking_garage.decreaseTicket()
            parking_garage.decreaseSpace()

            while True:
                pay_or_not = input("\nReady to pay for parking? ")

                if pay_or_not.lower() == "yes":
                    
                    parking_garage.payForParking()
                    break
                    
                elif pay_or_not.lower() == "no":
                    continue

                else:
                     print("\nPlease say yes or no please!")
                               
            break

        elif use.lower() == "no":
        
            print("\nHave a nice day!\n")
            break

        else: 
            print("\nPlease say yes or no please!")


run ()