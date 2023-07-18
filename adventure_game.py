name = input('type in your name: ')
print('Welcome', name, 'to this adventure!')

answer = input('you are on a dirt road, you have reached an end, you can either go right or left, which way do you want to go? choose one: ').lower()

if answer == 'left':
    answer = input('it is a river, youu can walk or swim across it chose one: ').lower()
    
    if answer == 'walk':
        print('you walked too far, u died')
    elif answer == 'swim':
        print('you swam and made it across')
    else:
        print('you didnt choose a valid option, you die')
        quit()    
    
        
        
elif answer == 'right':
    answer = input('you hit a bridge, do you want to cross it or go around it? choose one: ').lower()
    if answer=='cross it':
        print('you crossed it')
    elif answer =='go around it':
        print('you did not make around it')
    else:
        print('invalid option, you died')
        quit()
else:
    print('not a valid option, you loose')
    quit()

print('thank you for playing', name)