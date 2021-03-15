#THIS IS THE START OF MY PYTHON JOURNEY LMAOAOAO

print ("my first line")

#now something a little harder

first_name= 'bryan'

print(first_name)

last_name= 'duran'
print(last_name)

full=first_name+' '+last_name #this is called concatenation or smth
print(full)
print(full.title())
print(full.upper())
print(full.lower())

#see now ik how to made variables i think theyre called
#now watch me make like some lil greeting thing for a game LMAOAO

welc= 'Hello and welcome, '
welc2= ' to my universe.'
print(welc+full.title()+welc2)

#see how cool
#ok now for some math

print(2+2)
print(3*2)
print(3**2)

#ok now im gonna learn lists

bros= ['bryan','erick','jonathan']

for bro in bros:
    print('Good morning, '+bro.title()+'. There is breakfast ready.')

#if i wanna only talk to ONE specific one, do this

bruhs= ['bryan','erick','jonathan']
bruh=bruhs[1] #0 is the first number in python i think they dont use counting numbers
print('Good afternoon, '+bruh.title())

#now if i was like a hotel and wanted to greet every individual person we do this

guests= ['adam','bob','cody','dylan','evan']

for guest in guests:
    print('\nWelcome, '+guest.title()+'.')
    print('We hope you enjoy your stay!')
print('\nPlease let us know if you have any questions or requests.')

#NOW THIS IS WHERE WE GET A LIL TRICKY ok so we gonna learn to enumerate
#pretend we're like a reviewer
print('\n')
brands= ['chanel','dior','gucci','mk','coach']

for index, brand in enumerate(brands):
    place= str(index+1)
    print('Place #'+place+': '+brand.title()+'.')
