import random 

top_of_range = input('type in a number: ')
guess_counter = 0 

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please input a greater number next time')
        quit()
else: 
    print('please input a number')
    quit()
        
random_number = random.randint(0, top_of_range)
print('answer is :' + str(random_number))

while True:
    ans = input('guess a number: ')
    guess_counter += 1
    if ans.isdigit():
        ans = int(ans)
    else: 
        print('please print a number next time')
        continue
    
    if ans == random_number:
            print('you are correct')
            print('you took', guess_counter, ' many  guess(es)')
            break
        
    elif ans < random_number:
        print('you were below the actual number!')
    elif ans > random_number:
        print('your guess was greater than the actual number!')
    else:
        print('you are wrong, try again ') 
         
        continue