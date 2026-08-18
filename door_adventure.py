print('=' * 50)
print('WELCOME TO THE DOOR ADVENTURE')
print('=' * 50)
#The player has to complete the first adventure to unlock the second adventure.
print('Before you lies two adventures: Adventure A and Adventure B')
print('=' * 50)
print('WELCOME TO ADVENTURE A')
print('=' * 50)
treasures_collected=[]
def show_doors():
    print('\nDoors:')
    if 'A' in treasures_collected:
        print('Door A Completed')
    else:
        print('Door A Available')
    if 'B' in treasures_collected:
        print('Door B completed')
    else:
        print('Door B Available')
    if 'C' in treasures_collected:
        print('Door C Completed')
    else:
        print('Door C Available')
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
def location_a():
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
#all the answers are: placeholder answer (current loc)
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
        tries_iii=0
        while tries_iii<3:
            print('CLUE: PLACEHOLDER CLUE LOCAiii')
            answer_Aiii=input('>')
            answer_Aiii=answer_Aiii.lower()
            if answer_Aiii=='placeholder answer locaiii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_iii=tries_iii+1
                print('\nIncorrect. Tries left:' + str(3-tries_iii))
        if tries_iii==3:
                print('\nYou failed too many times. Returning to LocA.\n')
                continue
        tries_iv=0
        while tries_iv<3:
            print('CLUE: PLACEHOLDER CLUE LOCAiv')
            answer_Aiv=input('>')
            answer_Aiv=answer_Aiv.lower()
            if answer_Aiv=='placeholder answer locaiv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_iv=tries_iv+1
                print('\nIncorrect! Tries left:' + str(3-tries_iv))
        if tries_iv==3:
                print('\nYou failed too many times. Returning to LocA.\n')
                continue
        tries_v=0
        while tries_v<3:
            print('CLUE: PLACEHOLDER CLUE LOCAv')
            answer_Av=input('>')
            answer_Av=answer_Av.lower()
            if answer_Av=='placeholder answer locav':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_v=tries_v+1
                print('\nIncorrect! Tries left:' + str(3-tries_v))
        if tries_v==3:
                print('\nYou failed too many times. Returning to locA.\n')
                continue
        tries_vi=0
        while tries_vi<3:
            print('CLUE: PLACEHOLDER CLUE LOCAvi')
            answer_Avi=input('>')
            answer_Avi=answer_Avi.lower()
            if answer_Avi=='placeholder answer locavi':
                print('\nCorrect! You found the treasure of location A.\n')
                treasures_collected.append('A')
                break
            else:
                tries_vi=tries_vi+1
                print('\nIncorrect! Tries left:'+str(3-tries_vi))
        if tries_vi==3:
                print('\nYou failed too many times. Returning to locA.\n')
                continue
        else:
                break
    return True
if choice=='A':
    location_a()
    show_doors()
    
                
                
            
            
                
            
            
        