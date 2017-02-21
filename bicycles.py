class Bicycle(object):
    def __init__(self, model = "Standard", weight = 10, cost = 10):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return ("Model: {0}, weight: {1}, cost: {2}".format(self.model,self.weight,self.cost))
#end of class


class BicycleShop(object):
    def __init__(self, name = "Bike Shop", margin = 0.1, profit = 0):
        self.name = name
        self.margin = margin
        self.profit = profit
        self.inventory = []
    
    def addBike(self, bike):
        self.inventory.append(bike)
    
    def sellBike(self, bike, customer):
        if (bike in self.inventory):
            print("Found the bike")
            i = self.inventory.index(bike)
            if (customer.buyBike(bike)):
                self.profit = self.profit + (bike.cost * self.margin)
                self.inventory.remove(bike)
        else:
            print("Shop doesn't have this bike in inventory")
                
    def __str__(self):
        return ("{0} has {1} bikes and {2} profit".format(self.name,len(self.inventory),self.profit))
#end of class

class Customer(object):
    def __init__(self, name = "Joe", money = 0):
        self.name = name
        self.money = money
        self.bikes = []
    
    def buyBike(self, bike):
        if(self.money >= bike.cost):
            self.money = self.money - bike.cost
            self.bikes.append(bike)
            print("Bought the bike")
            return True
        else:
            print("{0} has only {1}, not enough to cover cost of bike {3}".format(self.name,self.money,bike.cost))
            return False
        print(self.bikes)
    
    def __str__(self):
        return ("{0} has {1} money left and has bought {2} bikes".format(self.name, self.money, len(self.bikes)))

