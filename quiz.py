print('hello welcome to my small game')

playing = input('do you wish to play the game? say yes or no ')

if playing.lower() != 'yes':
    print('okay quitting game')
    quit()
    
print('okay lets continue with the game')
score = 0

answer = input('what does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct')
    score+=1
else: 
    print('wrong')  
     
answer = input('what does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('correct')
    score+=1
else: 
    print('wrong')
       
    
answer = input('what does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('correct')
    score+=1
else: 
    print('wrong') 
       
    
answer = input('what should I ask her? ')
if answer.lower() == 'wanna go eat bingsu?':
    print('correct')
    score+=1
else: 
    print('wrong')   
    # score-=1
    
print('game has ended')
print('your total score is ' + str(score) + ' correct out of 4')
print('your percentage is ' + str((score / 4) * 100) + '%.') 