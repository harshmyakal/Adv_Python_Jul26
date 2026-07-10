#function Composition
def add_two(x):
    return x + 2
def subtract_five(x):
    return x - 5

#Manual Composition
def compose_function(value):
    result = add_two(value)
    result = subtract_five(result)
    return result

#Composition using a helper function
def compose(*function):
    def composed_func(x):
        result = x
        for func in function:
            result = func(result)
        return result
    return composed_func
        #Ceate a pipeline
pipeline = compose(add_two, subtract_five)
print(pipeline(20)) 