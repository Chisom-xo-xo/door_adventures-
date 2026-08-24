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
#answer:  loca
            answer=answer.lower()
            if answer=='loca':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries=0
        while tries<3:
            print('CLUE: PLACEHOLDER CLUE LOCAi')
            answer_Ai=input('>')
#all the answers are the current loc
            answer_Ai=answer_Ai.lower()
            if answer_Ai=='locai':
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
            if answer_Aii=='locaii':
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
            if answer_Aiii=='locaiii':
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
            if answer_Aiv=='locaiv':
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
            if answer_Av=='locav':
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
            if answer_Avi=='locavi':
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
#answer:  locb
            answer_b=answer_b.lower()
            if answer_b=='locb':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries_bi=0
        while tries_bi<3:
            print('CLUE: PLACEHOLDER CLUE LOCBi')
            answer_Bi=input('>')
#all the answers are the current loc
            answer_Bi=answer_Bi.lower()
            if answer_Bi=='locbi':
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
            if answer_Bii=='locbii':
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
            if answer_biii=='locbiii':
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
            if answer_biv=='locbiv':
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
            if answer_bv=='locbv':
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
            if answer_bvi=='locbvi':
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
#answer: locc
            answer_c=answer_c.lower()
            if answer_c=='locc':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')
        tries_c=0
        while tries_c<3:
            print('CLUE: PLACEHOLDER CLUE LOCCi')
            answer_ci=input('>')
#all the answers are the current loc
            answer_ci=answer_ci.lower()
            if answer_ci=='locci':
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
            if answer_cii=='loccii':
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
            if answer_ciii=='locciii':
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
            if answer_civ=='locciv':
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
            if answer_cv=='loccv':
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
            if answer_cvi=='loccvi':
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
        
print('\nWould you like to proceed to the next adventure?\n')
while True:
    continue_choice=input('yes/no)\n>')
    continue_choice=continue_choice.lower()
    if continue_choice=='yes':
        print('\nWelcome to your next adventure brave one\n')
        break
    elif continue_choice=="no":
        print('Sorry, no backing out now. Welcome to your next adventure')
        break
    else:
        print('\nPlease type yes or no.\n')
treasure_collected=[]
def show_door():
    print('\nDoors:')
    if 'D' in treasure_collected:
        print('Door D - Completed')
    else:
        print('Door D - Available')
    if 'E' in treasure_collected:
        print('Door E - Completed')
    else:
        print('Door E - Available')
    if 'F' in treasure_collected:
        print('Door F - Completed')
    else:
        print('Door F - Available')
    
#ADVENTURE B - LOCATION D
def location_d():
    while True:
        print('=' * 50)
        print('WELCOME TO LOC D')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCD')
        while True:
            answer_d=input('>')
            answer_d=answer_d.lower()
            if answer_d=='locd':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')

        tries_di=0
        while tries_di<3:
            print('CLUE: PLACEHOLDER CLUE LOCDi')
            answer_di=input('>')
            answer_di=answer_di.lower()
            if answer_di=='locdi':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_di=tries_di+1
                print('\nIncorrect! Tries left:' + str(3-tries_di))
        if tries_di==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue

        tries_dii=0
        while tries_dii<3:
            print('CLUE: PLACEHOLDER CLUE LOCDii')
            answer_dii=input('>')
            answer_dii=answer_dii.lower()
            if answer_dii=='locdii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_dii=tries_dii+1
                print('\nIncorrect! Tries left:' + str(3-tries_dii))
        if tries_dii==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue

        tries_diii=0
        while tries_diii<3:
            print('CLUE: PLACEHOLDER CLUE LOCDiii')
            answer_diii=input('>')
            answer_diii=answer_diii.lower()
            if answer_diii=='locdiii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_diii=tries_diii+1
                print('\nIncorrect! Tries left:' + str(3-tries_diii))
        if tries_diii==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue

        tries_div=0
        while tries_div<3:
            print('CLUE: PLACEHOLDER CLUE LOCDiv')
            answer_div=input('>')
            answer_div=answer_div.lower()
            if answer_div=='locdiv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_div=tries_div+1
                print('\nIncorrect! Tries left:' + str(3-tries_div))
        if tries_div==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue

        tries_dv=0
        while tries_dv<3:
            print('CLUE: PLACEHOLDER CLUE LOCDv')
            answer_dv=input('>')
            answer_dv=answer_dv.lower()
            if answer_dv=='locdv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_dv=tries_dv+1
                print('\nIncorrect! Tries left:' + str(3-tries_dv))
        if tries_dv==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue

        tries_dvi=0
        while tries_dvi<3:
            print('CLUE: PLACEHOLDER CLUE LOCDvi')
            answer_dvi=input('>')
            answer_dvi=answer_dvi.lower()
            if answer_dvi=='locdvi':
                print('\nCorrect! You found the treasure of Location D.\n')
                treasure_collected.append('D')
                break
            else:
                tries_dvi=tries_dvi+1
                print('\nIncorrect! Tries left:' + str(3-tries_dvi))
        if tries_dvi==3:
            print('\nYou failed too many times. Returning to LocD.\n')
            continue
        else:
            break
    return True
#ADVENTURE B - LOCATION E
def location_e():
    while True:
        print('=' * 50)
        print('WELCOME TO LOC E')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCE')
        while True:
            answer_e=input('>')
            answer_e=answer_e.lower()
            if answer_e=='loce':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')

        tries_ei=0
        while tries_ei<3:
            print('CLUE: PLACEHOLDER CLUE LOCEi')
            answer_ei=input('>')
            answer_ei=answer_ei.lower()
            if answer_ei=='locei':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_ei=tries_ei+1
                print('\nIncorrect! Tries left:' + str(3-tries_ei))
        if tries_ei==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue

        tries_eii=0
        while tries_eii<3:
            print('CLUE: PLACEHOLDER CLUE LOCEii')
            answer_eii=input('>')
            answer_eii=answer_eii.lower()
            if answer_eii=='loceii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_eii=tries_eii+1
                print('\nIncorrect! Tries left:' + str(3-tries_eii))
        if tries_eii==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue

        tries_eiii=0
        while tries_eiii<3:
            print('CLUE: PLACEHOLDER CLUE LOCEiii')
            answer_eiii=input('>')
            answer_eiii=answer_eiii.lower()
            if answer_eiii=='loceiii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_eiii=tries_eiii+1
                print('\nIncorrect! Tries left:' + str(3-tries_eiii))
        if tries_eiii==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue

        tries_eiv=0
        while tries_eiv<3:
            print('CLUE: PLACEHOLDER CLUE LOCEiv')
            answer_eiv=input('>')
            answer_eiv=answer_eiv.lower()
            if answer_eiv=='loceiv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_eiv=tries_eiv+1
                print('\nIncorrect! Tries left:' + str(3-tries_eiv))
        if tries_eiv==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue

        tries_ev=0
        while tries_ev<3:
            print('CLUE: PLACEHOLDER CLUE LOCEv')
            answer_ev=input('>')
            answer_ev=answer_ev.lower()
            if answer_ev=='locev':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_ev=tries_ev+1
                print('\nIncorrect! Tries left:' + str(3-tries_ev))
        if tries_ev==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue

        tries_evi=0
        while tries_evi<3:
            print('CLUE: PLACEHOLDER CLUE LOCEvi')
            answer_evi=input('>')
            answer_evi=answer_evi.lower()
            if answer_evi=='locevi':
                print('\nCorrect! You found the treasure of Location E.\n')
                treasure_collected.append('E')
                break
            else:
                tries_evi=tries_evi+1
                print('\nIncorrect! Tries left:' + str(3-tries_evi))
        if tries_evi==3:
            print('\nYou failed too many times. Returning to LocE.\n')
            continue
        else:
            break
    return True
#ADVENTURE B - LOCATION F
def location_f():
    while True:
        print('=' * 50)
        print('WELCOME TO LOC F')
        print('=' * 50)
        print('Solve this clue to enter the world')
        print('CLUE:PLACEHOLDER CLUE LOCF')
        while True:
            answer_f=input('>')
            answer_f=answer_f.lower()
            if answer_f=='locf':
                print('\nCorrect! You may continue\n')
                break
            else:
                print('\nIncorrect! Try again.\n')

        tries_fi=0
        while tries_fi<3:
            print('CLUE: PLACEHOLDER CLUE LOCFi')
            answer_fi=input('>')
            answer_fi=answer_fi.lower()
            if answer_fi=='locfi':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_fi=tries_fi+1
                print('\nIncorrect! Tries left:' + str(3-tries_fi))
        if tries_fi==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue

        tries_fii=0
        while tries_fii<3:
            print('CLUE: PLACEHOLDER CLUE LOCFii')
            answer_fii=input('>')
            answer_fii=answer_fii.lower()
            if answer_fii=='locfii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_fii=tries_fii+1
                print('\nIncorrect! Tries left:' + str(3-tries_fii))
        if tries_fii==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue

        tries_fiii=0
        while tries_fiii<3:
            print('CLUE: PLACEHOLDER CLUE LOCFiii')
            answer_fiii=input('>')
            answer_fiii=answer_fiii.lower()
            if answer_fiii=='locfiii':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_fiii=tries_fiii+1
                print('\nIncorrect! Tries left:' + str(3-tries_fiii))
        if tries_fiii==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue

        tries_fiv=0
        while tries_fiv<3:
            print('CLUE: PLACEHOLDER CLUE LOCFiv')
            answer_fiv=input('>')
            answer_fiv=answer_fiv.lower()
            if answer_fiv=='locfiv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_fiv=tries_fiv+1
                print('\nIncorrect! Tries left:' + str(3-tries_fiv))
        if tries_fiv==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue

        tries_fv=0
        while tries_fv<3:
            print('CLUE: PLACEHOLDER CLUE LOCFv')
            answer_fv=input('>')
            answer_fv=answer_fv.lower()
            if answer_fv=='locfv':
                print('\nCorrect! You may continue.\n')
                break
            else:
                tries_fv=tries_fv+1
                print('\nIncorrect! Tries left:' + str(3-tries_fv))
        if tries_fv==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue

        tries_fvi=0
        while tries_fvi<3:
            print('CLUE: PLACEHOLDER CLUE LOCFvi')
            answer_fvi=input('>')
            answer_fvi=answer_fvi.lower()
            if answer_fvi=='locfvi':
                print('\nCorrect! You found the treasure of Location F.\n')
                treasure_collected.append('F')
                break
            else:
                tries_fvi=tries_fvi+1
                print('\nIncorrect! Tries left:' + str(3-tries_fvi))
        if tries_fvi==3:
            print('\nYou failed too many times. Returning to LocF.\n')
            continue
        else:
            break
    return True
while len(treasure_collected)<3:
    show_door()
    while True:
        Choice=input('\nWhich door do you choose?\n>')
        Choice=Choice.upper()
        if Choice in treasure_collected:
            print('\nYou already completed that door. Choose another.\n')
        elif Choice=='D' or Choice=='E' or Choice=='F':
            break
        else:
            print('\nThat is not a valid door. Please choose D, E, or F.\n')
            
    if Choice=='D':
        location_d()
    elif Choice=='E':
        location_e()
    elif Choice=='F':
        location_f()
print('\nCongratulations! You have collected all three treasures!')
print('\nYou place all three treasures together.')
print('CLUE: PLACEHOLDER FINAL CLUE')
while True:
    final_answer=input('>')
    final_answer=final_answer.lower()
#answer=adventure final answer
    if final_answer=='adventure final answer':
        print('=' * 50)
        print('\nCONGRATULATIONS! YOU ARE A STAR!\n')
        print('=' * 50)
        break
    else:
        print('\nIncorrect! Try again.\n')
        





        


    
                
                
            
            
                
            
            
        

    
                
                
            
            
                
            
            
        

    
                
                
            
            
                
            
            
        