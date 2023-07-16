import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'sissor']
while True:
    user_input = input('choose one of rock paper or sissor or Q to quit: ')
    user_input = user_input.lower()
    if user_input == 'q':
        # quit()
        break
    
    if user_input not in options: #list is in brackets and in python i can use 'in' 
        continue
    
    random_number = random.randint(0,2)
    #rock = 0, paper = 1, sissor = 2
    computer_pick = options[random_number]
    print('computer picked:', computer_pick +'.') #using comma adds space where + doesnt
    
    if user_input != 'q' and user_input == computer_pick:
        print('tie')
        continue
    elif user_input == 'rock' and computer_pick == 'sissor':
        print('user won this one as you picked', user_input, 'and the computer picked', computer_pick)
        user_wins+=1
         
    elif user_input == 'paper' and computer_pick == 'rock':
        print('user won this one as you picked', user_input, 'and the computer picked', computer_pick)
        user_wins+=1
         
    elif user_input == 'sissor' and computer_pick == 'paper':
        print('user won this one as you picked', user_input, 'and the computer picked', computer_pick)
        user_wins+=1
         
    else:
        print('you lost because you picked', user_input, 'and the computer picked', computer_pick)
        computer_wins+=1
     
     
print('you won', user_wins, 'times and', 'the computer won', computer_wins , 'times')
print('goodbye, thank you for playing')