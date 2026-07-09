#FirstClass Function
def say_hello(name):
    return f"Hello {name}"
greet_function = say_hello
print(greet_function("Harsh"))
print(say_hello("Harsh"))
def apply_operation(func,value):
    return func(value)
def double(x):
    return x * 2
print(apply_operation(double,5))
def make_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier
double = make_multiplier(20)
print(double(2))
operations = {
    'add': lambda x,y: x+y,
    'subtract': lambda x,y: x-y,

}
print(operations['add'](10,5))
print(operations['subtract'](10,5))