import pickle


class CarRecord:  # declaring a class without other methods
    def __init__(self):  # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00

# ThisCar = CarRecord()
#
# CreateFile = open('CarFile.Dat', 'xb')
# CarFile = open('CarFile.DAT', 'rb+')
# Address = hash(ThisCar.VehicleID)
# CarFile.seek(Address)
# pickle.dump(ThisCar, CarFile)
# CarFile.close()

#TO Find a record from a given Vehicle ID:
thisVehicleId = ""
CarFile = open('CarFile.Dat', 'rb')
Address = hash(thisVehicleId)
CarFile.seek(Address)
ThisCar = pickle.load(CarFile)
CarFile.close()

print(ThisCar)