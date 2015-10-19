# Commentory: Use of Mixins
# When we want to provide lot of optional features in a class
# When we want to provide a feature in lots of classes
# We want to provide lot of non optional features, but we want
# separate classed (in separate modules) so each module is about
# one feature


# super class is better because it is computed indirect reference.

from abc import abstractmethod

class Ancestor:
    def method(self):
        pass

        
class Parent(Ancestor):
    def __init__(self):
        super().__init__()

    def method(self):
        print("In Parent")
        super().method()


class Parent2(Ancestor):
    def __init__(self):
        super().__init__()

    def method(self):
        print("In Parent2")
        # super().method()


class Child(Parent, Parent2):
    pass

c = Child()
c.method()
