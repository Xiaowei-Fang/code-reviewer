import os, sys  # Unused import warning

def bad_function( ):
    unused_var = 5
    x=10
    y   = 20
    return x+y

def another_bad_function():
    undefined_variable = some_undefined_variable  # This should cause an error
    print(undefined_variable)

# Line too long warning
def function_with_long_line():
    return "This is a very long line that exceeds the maximum line length allowed by pylint which is usually 100 characters but sometimes 88 or another value depending on the configuration"

# Too many local variables
def function_with_too_many_locals():
    var1 = 1
    var2 = 2
    var3 = 3
    var4 = 4
    var5 = 5
    var6 = 6
    var7 = 7
    var8 = 8
    var9 = 9
    var10 = 10
    var11 = 11
    var12 = 12
    var13 = 13
    var14 = 14
    var15 = 15
    var16 = 16
    return var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16

class BadClass:
    def __init__(self):
        self.value = None
    
    # Missing docstring
    def method_without_docstring(self):
        return self.value
    
    # Too many instance attributes
    def create_many_attributes(self):
        self.attr1 = 1
        self.attr2 = 2
        self.attr3 = 3
        self.attr4 = 4
        self.attr5 = 5
        self.attr6 = 6
        self.attr7 = 7
        self.attr8 = 8
        self.attr9 = 9
        self.attr10 = 10
        self.attr11 = 11
        self.attr12 = 12
        self.attr13 = 13
        self.attr14 = 14
        self.attr15 = 15
        self.attr16 = 16
        self.attr17 = 17
        self.attr18 = 18
        self.attr19 = 19
        self.attr20 = 20