class Vehicle():
    def __init__(self,bodystyle):
        self.bodystyle=bodystyle

    def drive(self, speed):
         self.mode = "driving"
         self.speed = speed
class Car(Vehicle):
    def __init__(self,enginetype):
        super().__init__("Car")
        self.wheels=4
        self.dorrs=4
        self.enginetype=enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my  " ,self.enginetype , "car at " ,self.speed
              )


class motorycycle(Vehicle):
    def __init__(self,hassidecar,enginetype):
        super().__init__("Motorcycle")
        if(hassidecar):
            self.wheels=3
        else:
            self.wheels=2
            self.enginetype=enginetype

car1=Car("Gas")
car2=Car("diesel")
mc1=motorycycle(True, "gas")

print(car1.enginetype)
print(car2.wheels)
print(car2.dorrs)

print(car1.drive(20))

