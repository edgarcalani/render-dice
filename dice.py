import random

def roll_dice():
    num = random.randint(1, 6) #incluye el 1 y 6
    #print('dado', num)
    return num

if __name__ == '__main__':
    print(roll_dice())