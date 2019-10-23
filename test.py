import secrets
import sys
secureNumber=secrets.SystemRandom()

while True:
    print('___Welcome to our Game___')
    press1=int(input('Press 1 to Read Rule or Press 2 To Play Game:>'))
    if press1==1:
        print('>Age must be more than 18:')
        print('>Show money more than 5000')
        print('>U must use more than 1000 each time:')
    if press1==2:
        uName=input('Please enter your name:>')
        uAge=int(input('Please enter your Age:>'))

        while len(uName)>2 and uAge>17:
            print('You can play game now')
            print('Welcome :>',uName)
            while True:
                sMoney=int(input('Please enter your Show Money:>'))
                while sMoney>4999:   
                    while True:                 
                        print('This is your money $',sMoney)
                        inputMoney=int(input('Please enter money to Play:>'))
                        luckyNumber=int(input('Please enter your Lucky Number:>'))
                        systemNumber=secureNumber.randint(10,99)
                        if luckyNumber==20:
                            print('You are win in 2D Game')
                            sMoney=(inputMoney*10)+(sMoney-inputMoney)
                            print('This is your All Money:>',sMoney)
                            toQuit=int(input('Press 0 To play Again:>'))
                            if toQuit!=0:
                                sys.exit('pye pye')
                            else:
                                continue
                                                                             
                        print('Try Again...LuckyNumber is',systemNumber)
                        sMoney=sMoney-inputMoney
                        if sMoney<1000:
                            print('You have Not enough money $',sMoney)
                            break
                        
                print('Please More Money')
        
        print('Please read agin the rule')
        