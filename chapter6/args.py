# It helps pass unlimited amount of argument

def states(name1, name2):
    print(name1, name2)
states('lagos', 'Abuja') 

def print_states(*args):
    print(args)
print_states('Lagos', 'Abuja', 'Rivers', 'Ibadan')


def add (*args):
    total = 0
    for n in args:
        total += n
    print(total)
add(2,3,4,5,1)
        