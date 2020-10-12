from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print(self._nickname + ": WangWang")



class Cat(Pet):
    def make_voice(self):
        print(self._nickname + ": miao~")


def main():
    pets = [Dog('Cacy'), Cat('Sophia')]
    for pet in pets:
        pet.make_voice()


if __name__ == "__main__":
    main()
