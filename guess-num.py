import random
r = random.randint(1,100) 
while True :
    num = input('請猜一個數字')
    num = int(num) 
    if num == r :
        print('恭喜你猜對了')
        break  
    elif num > r :
        print('比答案數字大') 
    elif num < r : 
        print('比答案數字小')  
        
