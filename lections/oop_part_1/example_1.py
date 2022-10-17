class Car:
    def __init__(this, wheels, engine, body, transmission, engine_value):
        this.wheels = wheels
        this.engine = engine
        this.body = body
        this.transmission = transmission
        this.engine_value = engine_value

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


ford = Car(wheels='18', engine='diesel', body='sedan', transmission='manual', engine_value=2.4)
lexus = Car(wheels='20', engine='gas', body='crossover', transmission='auto', engine_value=3.0)

ford.increase_speed()
lexus.increase_speed()
