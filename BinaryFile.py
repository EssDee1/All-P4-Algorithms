import pickle


class CarRecord:  # declaring a class without other methods
    def __init__(self):  # constructor
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


Car = [CarRecord() for i in range(100)]  # make a list of 100 car records

CarFile = open('CarFile.DAT', 'wb')

for i in range(100):
    pickle.dump(Car[i], CarFile)

CarFile.close()

CarFile = open('CarFile.DAT', 'rb')

NewCar = []

while True:
    try:
        NewCar.append(pickle.load(CarFile))
    except:
        print("End of File")
        break

CarFile.close()
print(NewCar)
