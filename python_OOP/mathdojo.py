# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:

# PART III
# Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.

class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for arg in args:
            if type(arg) ==list or type(arg) == tuple:
                for value in arg:
                   self.total += value
            else:
                self.total += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.total -= value
            else:
                self.total -= arg
        return self
        
md_easy = MathDojo()
print md_easy.add(2).add(2,5).subtract(3,2).total
md_with_lists = MathDojo()
print md_with_lists.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).total
md_with_tuples = MathDojo()
print md_with_tuples.add(2,(2,2), [2,2,2]).subtract(2,(2,2),[2,2]).total
