class Car:
    def __init__(this, wheels, engine, body, transmission, engine_value):
        this.wheels = wheels
        this.engine = engine
        this.body = body
        this.transmission = transmission
        this.engine_value = engine_value

    def __cooperation_engine_transmission(self):
        print('Do smth')

    def new_coop(self):
        self.__cooperation_engine_transmission()

    def open_door(self):
        print('open door')

    def increase_speed(self):
        if self.engine_value == 2.4:
            print('0-100 = 10s')
        elif self.engine_value == 3.0:
            print('0-100 = 8s')
        else:
            print('Unknown')

    def stop(self):
        print('stop')


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

jeff = Person('Jeff', 'Body', 35)
print(jeff.name)
print(jeff._surname)
print(jeff.__age)
