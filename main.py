from bicycles import Bicycle, BicycleShop, Customer

if __name__ == "__main__":
    print("Starting up...")
    
    bike1 = Bicycle("Red", 20, 100)
    bike2 = Bicycle("Blue", 20, 50)
    bike3 = Bicycle("Green", 20, 200)
    bike4 = Bicycle("Black", 20, 300)
    bike5 = Bicycle("Silver", 20, 100)
    bike6 = Bicycle("Purple", 20, 150)
    
    customer1 = Customer("Joe", 200)
    customer2 = Customer("Sally", 500)
    customer3 = Customer("Mike", 1000)
    
    shop1 = BicycleShop("Bike Shop", 0.2, 0)
    
    print(bike1)
    print(customer1)
    print(shop1)
    
    shop1.addBike(bike1)
    shop1.addBike(bike2)
    shop1.addBike(bike3)
    shop1.addBike(bike4)
    shop1.addBike(bike5)
    shop1.addBike(bike6)
    
    print(shop1)
    for i in shop1.inventory:
        print(i)
    
    shop1.sellBike(bike1, customer1)
    print(customer1)
    print(shop1)

    for i in shop1.inventory:
        print(i)
    
    shop1.sellBike(bike1, customer2)
    print(customer2)
    print(shop1)