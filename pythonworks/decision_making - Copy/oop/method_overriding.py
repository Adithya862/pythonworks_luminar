# method over riding #

class Bike:
    def start(self):
     print("kicker start")

    def breaking(self):
       print("drum break")

class HerohondaSplender(Bike):
    def start(self):
     print("self start")

    def breaking(self):
       print("abs breaking")
hobj=HerohondaSplender()
hobj.start()
hobj.breaking()

# inherit chyyathitt undavnm
# method signature must be same
# super()-parent class ne refer chyyan
