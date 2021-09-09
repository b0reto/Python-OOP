def even_parameters(f):
    def wrapper(*args):
        for arg in args:
            err_msg = "Please use only even numbers!"
            try:
                if arg % 2 != 0:
                    return err_msg
            except:
                return err_msg

        return f(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
