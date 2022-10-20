class Car:
    def __init__(self, engine):
        self.engine = engine

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

diesel_engine = Engine('diesel')
ford = Car(diesel_engine)