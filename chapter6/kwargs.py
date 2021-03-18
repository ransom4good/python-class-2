# Meaning Keyword arguments. Gives you key and value result.

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(key1='Value1', key2='Value2', key3='Value3')

def state_capital(**kwargs):
    for state, capital in kwargs.items():
        print(F'The Capital of {state} is {capital}')
state_capital(imo='Owerri', jigawa='Dutse', Kwara='Ilorin')        
state_capital(
            imo='Owerri', 
            jigawa='Dutse', 
            Kwara='Ilorin',
            kogi='Lokoja',
            Nasarawa='Lafia',
            Ogun='Abeokuta',
            Osun= 'Osogbo' )        