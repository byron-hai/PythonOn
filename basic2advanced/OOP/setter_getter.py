# -*- coding: utf-8 -*-

class Person:
    cnt = 0
    def __init__(self, name, age):
        self._name = name
        self.age = age
        Person.cnt += 1

    @classmethod
    def get_numbers(cls):
        return Person.cnt

    @staticmethod
    def say_hi():
        print("Hello~")

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

if __name__ == "__main__":
    person = Person('Li', 39)

    #print(person.name, person.age)
    #person.age = 32
    #print(person.name, person.age)
    [Person(str(i), str(i**2)) for i in range(100)]

    print(Person.get_numbers())
