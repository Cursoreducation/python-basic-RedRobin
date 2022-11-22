BRIDGE_FEE = 18
BRIDGE_LABEL = 25

class PassageProhibited(Exception):
 def __init__(self, message):
     self.message = message

 def __str__(self):
     return f"You don't have money: {self.message}"

class Person:
 def __init__(self, money, label):
     self.money = money
     self.label = label

 @property
 def get_balance(self):
     return self.money

 @property
 def get_label(self):
     return self.label


def fare(func):
    def inner(person):
        if person.get_balance >= BRIDGE_FEE and person.get_label:
            person.money -= BRIDGE_FEE
        elif person.get_balance >= BRIDGE_FEE and not person.get_label:
            if person.get_balance >= BRIDGE_FEE + BRIDGE_LABEL:
                person.money -= BRIDGE_FEE + BRIDGE_LABEL
                person.label = True
            else:
                raise PassageProhibited("You don't have enough money to pass the bridge. "
                                        f"Your current balance is: {person.get_balance} "
                                        f"but the price is {BRIDGE_FEE + BRIDGE_LABEL}")
        else:
            raise PassageProhibited("You don't have enough money to pass the bridge. "
                                    f"Your current balance is: {person.get_balance} "
                                    f"but the price is {BRIDGE_FEE}")
        return func(person)
    return inner



@fare
def bridge(person):
    print(f'Person passed the bridge with money: {person.get_balance} and label: {person.get_label}')



anna = Person(money=30, label=True)
rob = Person(money=100, label=False)
mark = Person(money=10, label=True)
ted = Person(money=41, label=False)
bridge(anna)
bridge(rob)
bridge(mark)
bridge(ted)