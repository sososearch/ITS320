#------------------------------------------------------------------------
# Program Name: String Values in Reverse Order
# Author: Musung Kim
# Date: 2/7/2021
#------------------------------------------------------------------------
# Pseudocode: This program will create an automobile class that will be
# used by a dealership as a vehicle inventory program.
#------------------------------------------------------------------------
# Program Inputs: Vehicle make, model, color, year and mileage
# Program Outputs: Output of all vehicle inventory to a text file.
#------------------------------------------------------------------------

print('Vehicle Inventory - Main Menu\n')
class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._mileage = 0
    def addVehicle(self):
        try:
            self._make = input('\nInput vehicle make: ')
            self._model = input('Input vehicle model: ')
            self._year = int(input('Input vehicle year: '))
            self._color = input('Input vehicle color: ')
            self._mileage = int(input('Input vehicle mileage: '))
            return True
        except ValueError:
            print('\nPlease try again using numbers for mileage and year\n')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._mileage])

class Inventory:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('Vehicle has been added\n')
    def viewInventory(self):
        print('\t'.join(['', 'Make', 'Model', 'Year', 'Color', 'Mileage']))
        for idx, vehicle in enumerate(self.vehicles):
            print(idx + 1, end='\t')
            print(vehicle)

inventory = Inventory()
while True:

    print('1 - Add Vehicle')
    print('2 - Delete Vehicle')
    print('3 = View Current Inventory')
    print('4 - Update Vehicle')
    print('5 - Export Current Inventory')
    print('6 - Quit')
    userInput=input('\nPlease select a number from above options: ')
    if userInput=="1":
        #add a vehicle to inventory
        inventory.addVehicle()
    elif userInput=='2':
        #delete a vehicle from inventory
        if len(inventory.vehicles) < 1:
            print('\nSorry, there are no vehicles in this inventory\n')
            continue
        inventory.viewInventory()
        item = int(input('\nPlease enter the number associated with the vehicle to be removed: \n'))
        if item - 1  > len(inventory.vehicles):
            print('\nThis is an invalid number\n')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print ()
            print('\nThis vehicle has been removed\n')
    elif userInput == '3':
        #list all the vehicles
        if len(inventory.vehicles) < 1:
            print('\nSorry, there are no vehicles in this inventory\n')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        #edit vehicle
        if len(inventory.vehicles) < 1:
            print('\nSorry, there are no vehicles in this inventory\n')
            continue
        inventory.viewInventory()
        item = int(input('\nPlease enter the number associated with the vehicle to be updated: \n'))
        if item - 1  > len(inventory.vehicles):
            print('\nThis is an invalid number\n')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True :
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print ()
                print('\nThis vehicle has been updated\n')
    elif userInput == '5':
        #export inventory to file
        if len(inventory.vehicles) < 1:
            print('\nSorry, there are no vehicles in this inventory\n')
            continue
        f = open('inventory.txt', 'w')
        f.write('\t'.join(['Make', 'Model', 'Year', 'Color', 'Mileage']))
        f.write('\n')
        for vechicle in inventory.vehicles:
            f.write('%s\n' %vechicle)
        f.close()
        print('\nVehicle inventory has been exported\n')
    elif userInput == '6':
        #exit the loop
        print('\nGoodbye')
        break
    else:
        #invalid user input
        print('\nThis is an invalid input. Please try again.\n')
