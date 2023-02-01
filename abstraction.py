#create a class that contains at least one abstract method and one reg method
#create a child class that defines the implementation of its parents abstract method
#create an object that uses both the parent and child methods


from abc import ABC, abstractmethod
class payment(ABC):
    def bill(self,amount):
        print("You owe: ",amount)

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPay(payment):
    def pay(self,amount):
        print('Your purchase amount of {} is now paid '.format(amount))

obj = CreditCardPay()
obj.bill("$100")
obj.pay("$100")
