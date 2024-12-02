from pprint import pprint


class BaseClass:
    num_call_base = 0

    def call_class(self):
        print(f"Base class was run")

        self.num_call_base += 1

        
class LeftClass(BaseClass):
    num_call_left = 0

    def call_class(self):
        super().call_class()

        print(f"Left class was run")

        self.num_call_left += 1

class RightClass(BaseClass):
    num_call_right = 0

    def call_class(self):
        super().call_class()

        print(f"Right class was run")

        self.num_call_right += 1

class SubClass(RightClass, LeftClass):
    num_call_sub = 0

    def call_class(self):
        super().call_class()

        print(f"Sub class was run")

        self.num_call_sub += 1


diamond_problem = SubClass()

diamond_problem.call_class()

print()

print(f"Sub class run count: {diamond_problem.num_call_sub} Left class run count: {diamond_problem.num_call_left} Right class run count: {diamond_problem.num_call_right} Base class run count: {diamond_problem.num_call_base} <<----\n")

pprint(SubClass.__mro__)