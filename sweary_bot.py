def sweary_bot():
# A function for when the world is being a bastard. Type in your situation,
# and bask in the sweary incredulity of sweary_bot!
    input('What are we angry about now? \n')
    from random import randint
    a = randint(0,3) #selects a random integer between 0 and 9. Increase this if you wat to add more responses
    if a==0: #the integer selected corresponds to the responses below. Customize as you like.
        print ("ARE YOU FUCKING KIDDING ME?! \n")
    elif a==1:
        print ("THOSE BASTARDS! \n")
    elif a==2:
        print ("ASFJHFDJGKJLREHGWFFFFUUUUUUUUUCK! \n")
    elif a==3:
        print ("FUCK! \n")