"""
aiajsdkafoefpokwepfdoedpefw-inator
"""
import sys
import random

aiajsdkafoefpokwepfdoedpefw = ['a', 'i', 'j', 's', 'd', 'k', 'f', 'o', 'e', 'p', 'w']

print("aiajsdkafoefpokwepfdoedpefw-inator\n")

menu = """1) make commit title
2) make commit description
3) aiajsdkafoefpokwepfdoedpefw (might crash your PC lmfao)
4) quit

make your choice (1/2/3/4): """

while True:
    try:
        choice = int(input(menu))
    except ValueError:
        print("\nthat wasnt very aiajsdkafoefpokwepfdoedpefw of you to not enter a valid number\n")
        continue
    else:
        if not 1 <= choice <= 4:
            print("\nthat wasnt very aiajsdkafoefpokwepfdoedpefw of you to not enter a number between 1 and 4\n")
            continue
        if choice == 4:
            print("\nmay aiajsdkafoefpokwepfdoedpefw bless you\nbye!!! *dies of amongus imposter*\n")
            sys.exit()
        break

if choice == 1:
    print(''.join(random.sample(aiajsdkafoefpokwepfdoedpefw * 3, 27)))
elif choice == 2:
    while True:
        try:
            line_count = int(input("how many lines of aiajsdkafoefpokwepfdoedpefw fam? "))
        except ValueError:
            print("\nthat wasnt very aiajsdkafoefpokwepfdoedpefw of you to not enter a valid number\n")
            continue
        else:
            break
    for i in range(line_count):
        spaces = ' ' * random.randint(0, 10)
        print(spaces + ''.join(random.sample(aiajsdkafoefpokwepfdoedpefw * 5, random.randint(27, 54))))
else:
    while True:
        print(''.join(random.sample(aiajsdkafoefpokwepfdoedpefw * 1000000, 1000000)), end='')
