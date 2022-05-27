def greet(bot_name, birth_year):
    print("-------------------------------------------------------------")
    print("\nHello! My name is {0}.".format(bot_name))
    print("I was created by Vedashri in {0}.".format(birth_year))


def remind_name():
    print('\nPlease, remind me your name.')
    name = input()
    print("\nWhat a great name you have, {0}!\n".format(name))


def guess_age():
    print('Let me guess your AGE.')
    print('Enter remainders of dividing your age by 3, 5 and 7.\n')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    if (age<=25):
        print("Your age is {0}; that's a good time to start programming!".format(age))
    elif (age>25 and age<=40):
        print("Your age is {0}; that's a good time to earn and set up your life!".format(age))
    elif (age>40 and age<100):
        print("Your age is {0}; that's a good time to enjoy your life!".format(age))


def count():
    print('\n \nNow I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("\n \n Let's test your programming knowledge.")
    print("\nWhy do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.\n")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('AWESOME!')
   
def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
greet('Sophia', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()