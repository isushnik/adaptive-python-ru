def durak(card1, card2, adv):
    # suits = ['C', 'D', 'H', 'S']
    values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    v1, s1 = card1[:-1], card1[-1]
    v2, s2 = card2[:-1], card2[-1]

    if s1 == s2:
        if values.index(v1) > values.index(v2):
            print('First')
        else:
            print('Second')
    elif s1 == adv:
        print('First')
    elif s2 == adv:
        print('Second')
    else:
        print('Error')

card1, card2 = input().split()
adv = input()
durak(card1, card2, adv)

# durak('AH', 'JH', 'D')  # First
# durak('AH', 'JS', 'S')  # Second
# durak('7C', '10H', 'S')  # Error
