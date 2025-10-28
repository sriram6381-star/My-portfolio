from abc import ABC,abstractmethod

class sri:
    @abstractmethod
    def iphone():
        pass
    @abstractmethod
    def ns():
        pass

class life(sri):
    def iphone():
        print("i have i phone 16")

    def ns():
        print("i have ns 200 bike")


ad=life()
ad.iphone()
ad.ns()