# defines the zone a variable is accessed
my_name = 'James' # Global scope

def print_name():
    global my_name # to override Global scope,we use the keyword 'global'
    my_name = 'Gloria' # Local scope
 
    print('the name inside the function is', my_name) # access local scope
print_name()    

print('the name outside the function is', my_name) # access global scope