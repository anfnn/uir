import random
def vibor_chel():
    print("Выбери, камень(1), ножницы(2), бумага(3)")
    vibor = int(input())
    if vibor == 1:
        print("вы выбрали камень")
    if vibor == 2:
        print("вы выбрали ножницы")
    if vibor == 3:
        print("вы выбрали бумага")
    while vibor not in [1,2,3]:
        vibor = input("Не та цифра, выбирай еще")
        vibor = int(input())
    return vibor

def vibor_computer():
    copik = random.randint(1,3)
    if copik == 1:
        print("комп выбрал камень")
    if copik == 2:
        print("комп выбрал ножницы")
    if copik == 3:
        print("комп выбрал бумага")
    return copik
def IGRA(chelik, copik):
    if copik == chelik:
        win=0
    if chelik == 1 and copik == 2:
        win=1
    if chelik == 1 and copik == 3:
        win=2
    if chelik == 2 and copik == 3:
        win=1
    if chelik == 3 and copik == 1:
        win=1
    if chelik == 3 and copik == 2:
        win=2
    if chelik == 2 and copik == 1:
        win=2
    if win == 0:
        return ("Ничья")
    if win == 1:
        return("Умничка, выйграл")
    if win ==2:
        return("Комп выйграл")

def game():
    a = vibor_chel()
    b = vibor_computer()
    c = IGRA(a,b)
    return c

def ask():
    print("Хотите продолжить игру?, 1 - true, 2 - false")
    t = int(input())
    while  t!=1 and t!=2:
        print("Введи другие данные")
        t = int(input())
    
    if t ==1:
          while t == 1:
            k = game()
            print(k)
            return ask()
    if t == 2:
        print("Poka")
        exit(0)
        
print("Привет, хочешь поиграть в камень ножницы бумага  true/false?")
answer = bool(input())
if answer == False:
    print("ну ладненько")
else:
    d = game()
    print(d)
    w = ask()
    print(w)

