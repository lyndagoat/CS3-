class Bill:
    amount = 0
    def __init__(self,amount):
        self.amount = amount
    def pay(self, amount):
        self.amount -= Payment.amount
        print("Paying with",Payment.mode)
        print("Balance:",self.amount)

class Payment:
    amount = 0
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    
    def __init__(self, name, amount):
        
        self.mode = name
        self.amount = amount

bigbill = Bill(1000)
bayad = Payment(900)
bigbill.pay(bayad)

gcash = Ewallet("GCas",67)
bigbill.pay(gcash)


ewallet = Ewallet("PisayCash", 33)
bigbill.pay(ewallet)
