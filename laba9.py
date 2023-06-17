class E1(BaseException):
    pass

class E2(BaseException):
    pass

class E3(BaseException):
    pass

class E_Class:
    def method1(self, argument):
        if argument < 0:
            raise E1("Argument should be non-negative")
        elif argument == 0:
            raise E2("Argument should be non-zero")
        else:
            return argument ** 2

    def method2(self, argument1, argument2):
        if argument1 == argument2:
            raise E3("Arguments should be different")
        else:
            return argument1 + argument2

    def method3(self, argument):
        if not isinstance(argument, str):
            raise TypeError("Argument should be a string")
        elif len(argument) < 5:
            raise ValueError("String should be at least 5 characters long")
        else:
            return argument.upper()
        
class FixException:
    def __init__(self, obj):
        self.obj = obj

    def fix_method1(self, argument):
        try:
            result = self.obj.method1(argument)
        except E1 as x:
            print("Error:", x)
            result = None
        except E2 as x:
            print("Error:", x)
            result = None
        return result

    def fix_method2(self, argument1, argument2):
        try:
            result = self.obj.method2(argument1, argument2)
        except E3 as x:
            print("Error:", x)
            result = None
        return result

    def fix_method3(self, argument):
        try:
            result = self.obj.method3(argument)
        except TypeError as x:
            print("Error:", x)
            result = None
        except ValueError as x:
            print("Error:", x)
            result = None
        return result
    
obj = E_Class()
fix = FixException(obj)

print(fix.fix_method1(2))
print(fix.fix_method1(-1))

print(fix.fix_method2(2, 3))
print(fix.fix_method2(2, 2))

print(fix.fix_method3("hello"))
print(fix.fix_method3(123))

print(fix.fix_method3("hi"))