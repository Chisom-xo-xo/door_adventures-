print('=' * 50)
print('WELCOME TO THE DOOR ADVENTURE')
print('=' * 50)
#The player has to complete the first adventure to unlock the second adventure.
print('Before you lies two adventures: Adventure A and Adventure B')
print('=' * 50)
print('WELCOME TO ADVENTURE A')
print('=' * 50)
#When the player enters the first door, they have three accessible doors to pick from.
print('\nBefore you lies three doors: Door A, Door B, Door C.')
#For now, A is the only available path
while True:
    choice=input('Which door do you choose? (Door A, B, or C)\n>')
    choice=choice.upper()
    if choice=='A' or choice=='B' or choice=='C':
        break
    else:
        print('\nDoor does not exist. Please choose A, B, or C.\n')
print('\nYou chose Door' + choice)
#LOCATION A
if choice=='A':
    while True:
        print('=' * 50)
        print('WELCOME TO LOC A')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCA')
        while True:
            answer=input('>')
#answer: placeholder answer loca
            answer=answer.lower()
            if answer=='placeholder answer loca':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries=0
        while tries<3:
            print('CLUE: PLACEHOLDER CLUE LOCAi')
            answer_Ai=input('>')
#answer: placeholder answer locai
            answer_Ai=answer_Ai.lower()
            if answer_Ai=='placeholder answer locai':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries=tries+1
                print('\nIncorrect. Tries left: ' + str(3-tries))
        if tries==3:
            print('\nYou failed too many times. Returning to LocA.\n')
            continue
        tries_ii=0
        while tries_ii<3:
            print('CLUE: PLACEHOLDER CLUE LOCAii')
            answer_Aii=input('>')
            answer_Aii=answer_Aii.lower()
            if answer_Aii=='placeholder answer locaii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_ii=tries_ii+1
                print('\nIncorrect. Tries left: '+ str(3-tries_ii))
        if tries_ii==3:
                print('\nYou failed too many times. Returnng to LocA.\n')
                continue
        else:
                break
            
        