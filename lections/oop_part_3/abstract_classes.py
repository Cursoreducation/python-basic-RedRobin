from abc import abstractmethod, ABC

# interface
class Vehicle(ABC):

    @abstractmethod
    def drive(self, test: str):
        raise NotImplementedError

    @abstractmethod
    def stop(self, hello: list):
        raise NotImplementedError


# abstact class
class Vehicle2(ABC):
    def __init__(self, body_type, engine, transmission):
        self.body_type = body_type
        self.engine = engine
        self.transmission = transmission

    def drive(self):
        print('I am driving')

    @abstractmethod
    def stop(self):
        raise NotImplementedError

class Car(Vehicle2):
    def __init__(self, body_type, engine, transmission):
        super().__init__(body_type, engine, transmission)
        self.body_type = body_type
        self.engine = engine
        self.transmission = transmission

    def drive(self):
        print('I am driving')

    def stop(self):
        print('I am stopping')

    def lock(self):
        print('Lock')


class Toyota(Vehicle):
    def __init__(self, body_type, engine, transmission):
        self.body_type = body_type
        self.engine = engine
        self.transmission = transmission

    def drive(self, test):
        print('Driving like Toyota')

    def stop(self, hello):
        print('Stopping like Toyota')

    def lock(self):
        print('Lock')


class Ford(Vehicle):
    def __init__(self, body_type, engine, transmission):
        self.body_type = body_type
        self.engine = engine
        self.transmission = transmission

    def drive(self):
        print('Driving like Ford')

    def stop(self):
        print('Stopping like Ford')

    def lock(self):
        print('Lock')


ford = Car(body_type='sedan', engine='diesel', transmission='manual')
# ford_1 = Vehicle(body_type='sedan', engine='diesel', transmission='manual')
ford.drive()


def hello():
    print('Hello')

def hello():
    print('Hi')

hello()