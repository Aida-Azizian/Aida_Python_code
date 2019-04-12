import random
def comment(m):
    if m<3:
        print('Wow, You did really awesome')    
    elif m>=3 and m<5:
        print('You did well ')        
    elif m>5 and m<=7:
        print('You can do better')
    elif m>7:
        print('You need to try harder next time')

def play():
    m=0
    print('Lets Play')
    guess=int(input('What is your guess?'))
    secret=random.randint(0,99)
    while guess!=secret:
        if abs(guess-secret)>=8:
              if guess>secret:
                   print('That is high,try lower number.')
              else:
                   print('That is low,try higher number.')
        elif 2< abs(guess-secret)<8:
              print('You are close to the secret number.')
        elif abs(guess-secret)<=2:
              print('You are very close to the secret number.')     
        guess=int(input('What is your guess?\n'))
        m=m+1
        if guess==secret:
            print('Congratulations')
            print('You can guess the secret number after',m,'iteration')
            comment(m)

play()
