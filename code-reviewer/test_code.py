def hello_world():
    print("Hello, World!")
    x = 10
    y = 20
    return x + y

# Intentionally create a pylint warning
def bad_function( ):
    unused_var = 5
    print("This function has issues")