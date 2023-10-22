# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method
# Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"""{name}s age is {age}"""

    @property
    def getInfo(self, name, age):
        return self.info

import codewars_test as test
# from solution import *
#
# @test.describe("Fixed Tests")
# def fixed_tests():
#     names=["john","matt","alex","cam"]
#     ages=[16,25,57,39]
#     for i in range(4):
#         name,age=names[i],ages[i]
#         person=Person(name,age)
#         @test.it("Testing for %s and %s" %(repr(name),age))
#         def basic_test_cases():
#             test.assert_equals(person.info, name+"s age is "+str(age))