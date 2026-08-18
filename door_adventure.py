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


#LOCATION B
def location_b():
    while True:
        print('=' * 50)
        print('WELCOME TO LOC B')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCB')
        while True:
            answer_b=input('>')
#answer: placeholder answer locb
            answer_b=answer_b.lower()
            if answer_b=='placeholder answer locb':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries_bi=0
        while tries_bi<3:
            print('CLUE: PLACEHOLDER CLUE LOCBi')
            answer_Bi=input('>')
#all the answers are: placeholder answer (current loc)
            answer_Bi=answer_Bi.lower()
            if answer_Bi=='placeholder answer locbi':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_bi=tries_bi+1
                print('\nIncorrect. Tries left: ' + str(3-tries_bi))
        if tries_bi==3:
            print('\nYou failed too many times. Returning to LocB.\n')
            continue
        tries_bii=0
        while tries_bii<3:
            print('CLUE: PLACEHOLDER CLUE LOCBii')
            answer_Bii=input('>')
            answer_Bii=answer_Bii.lower()
            if answer_Bii=='placeholder answer locbii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_bii=tries_bii+1
                print('\nIncorrect. Tries left: '+ str(3-tries_bii))
        if tries_bii==3:
                print('\nYou failed too many times. Returnng to LocB.\n')
                continue
        tries_biii=0
        while tries_biii<3:
            print('CLUE: PLACEHOLDER CLUE LOCBiii')
            answer_biii=input('>')
            answer_biii=answer_biii.lower()
            if answer_biii=='placeholder answer locbiii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_biii=tries_biii+1
                print('\nIncorrect. Tries left:' + str(3-tries_biii))
        if tries_biii==3:
                print('\nYou failed too many times. Returning to LocB.\n')
                continue
        tries_biv=0
        while tries_biv<3:
            print('CLUE: PLACEHOLDER CLUE LOCBiv')
            answer_biv=input('>')
            answer_biv=answer_biv.lower()
            if answer_biv=='placeholder answer locbiv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_biv=tries_biv+1
                print('\nIncorrect! Tries left:' + str(3-tries_biv))
        if tries_biv==3:
                print('\nYou failed too many times. Returning to LocB.\n')
                continue
        tries_bv=0
        while tries_bv<3:
            print('CLUE: PLACEHOLDER CLUE LOCBv')
            answer_bv=input('>')
            answer_bv=answer_bv.lower()
            if answer_bv=='placeholder answer locbv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_bv=tries_bv+1
                print('\nIncorrect! Tries left:' + str(3-tries_bv))
        if tries_bv==3:
                print('\nYou failed too many times. Returning to locB.\n')
                continue
        tries_bvi=0
        while tries_bvi<3:
            print('CLUE: PLACEHOLDER CLUE LOCBvi')
            answer_bvi=input('>')
            answer_bvi=answer_bvi.lower()
            if answer_bvi=='placeholder answer locbvi':
                print('\nCorrect! You found the treasure of location B.\n')
                treasures_collected.append('B')
                break
            else:
                tries_bvi=tries_bvi+1
                print('\nIncorrect! Tries left:'+str(3-tries_bvi))
        if tries_bvi==3:
                print('\nYou failed too many times. Returning to locB.\n')
                continue
        else:
                break
    return True


#LOCATION C
def location_c():
    while True:
        print('=' * 50)
        print('WELCOME TO LOC C')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCC')
        while True:
            answer_c=input('>')
#answer: placeholder answer locc
            answer_c=answer_c.lower()
            if answer_c=='placeholder answer locc':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries_c=0
        while tries_c<3:
            print('CLUE: PLACEHOLDER CLUE LOCCi')
            answer_ci=input('>')
#all the answers are: placeholder answer (current loc)
            answer_ci=answer_ci.lower()
            if answer_ci=='placeholder answer locci':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_c=tries_c+1
                print('\nIncorrect. Tries left: ' + str(3-tries_c))
        if tries_c==3:
            print('\nYou failed too many times. Returning to LocC.\n')
            continue
        tries_cii=0
        while tries_cii<3:
            print('CLUE: PLACEHOLDER CLUE LOCCii')
            answer_cii=input('>')
            answer_cii=answer_cii.lower()
            if answer_cii=='placeholder answer loccii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_cii=tries_cii+1
                print('\nIncorrect. Tries left: '+ str(3-tries_cii))
        if tries_cii==3:
                print('\nYou failed too many times. Returnng to LocC.\n')
                continue
        tries_ciii=0
        while tries_ciii<3:
            print('CLUE: PLACEHOLDER CLUE LOCCiii')
            answer_ciii=input('>')
            answer_ciii=answer_ciii.lower()
            if answer_ciii=='placeholder answer locciii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_ciii=tries_ciii+1
                print('\nIncorrect. Tries left:' + str(3-tries_ciii))
        if tries_ciii==3:
                print('\nYou failed too many times. Returning to LocC.\n')
                continue
        tries_civ=0
        while tries_civ<3:
            print('CLUE: PLACEHOLDER CLUE LOCCiv')
            answer_civ=input('>')
            answer_civ=answer_civ.lower()
            if answer_civ=='placeholder answer locciv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_civ=tries_civ+1
                print('\nIncorrect! Tries left:' + str(3-tries_civ))
        if tries_civ==3:
                print('\nYou failed too many times. Returning to LocC.\n')
                continue
        tries_cv=0
        while tries_cv<3:
            print('CLUE: PLACEHOLDER CLUE LOCCv')
            answer_cv=input('>')
            answer_cv=answer_cv.lower()
            if answer_cv=='placeholder answer loccv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_cv=tries_cv+1
                print('\nIncorrect! Tries left:' + str(3-tries_cv))
        if tries_cv==3:
                print('\nYou failed too many times. Returning to locC.\n')
                continue
        tries_cvi=0
        while tries_cvi<3:
            print('CLUE: PLACEHOLDER CLUE LOCCvi')
            answer_cvi=input('>')
            answer_cvi=answer_cvi.lower()
            if answer_cvi=='placeholder answer loccvi':
                print('\nCorrect! You found the treasure of location C.\n')
                treasures_collected.append('C')
                break
            else:
                tries_cvi=tries_cvi+1
                print('\nIncorrect! Tries left:'+str(3-tries_cvi))
        if tries_cvi==3:
                print('\nYou failed too many times. Returning to locC.\n')
                continue
        else:
                break
    return True
while len(treasures_collected)<3:
    show_doors()
    while True:
        choice=input('\nWhich door do you choose?\n>')
        choice=choice.upper()
        if choice in treasures_collected:
            print('\nYou already completed that door. Please select another door.\n')
        elif choice=='A' or choice=='B' or choice=='C':
            break
        else:
            print('\nThat door does not exist. Please choose A, B, or C.\n')
    if choice=='A':
        location_a()
    elif choice=='B':
        location_b()
    elif choice=='C':
        location_c()
        
print('\nCongratulations! You have collected all three treasures!')
print('\nYou place all three treasures together.')
print('CLUE: PLACEHOLDER FINAL CLUE')
while True:
    final_answer=input('>')
    final_answer=final_answer.lower()
    if final_answer=='placeholder final answer':
        print('=' * 50)
        print('\nCONGRATULATIONS! YOUR ADVENTURE COMES TO A CLOSE!\n')
        print('=' * 50)
        break
    else:
        print('\nIncorrect! Try again.\n')

    
                
                
            
            
                
            
            
        

    
                
                
            
            
                
            
            
        

    
                
                
            
            
                
            
            
        