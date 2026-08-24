# An attempt to use collections and functions to shorten the code
print('=' * 50)
print('WELCOME TO THE DOOR ADVENTURE')
print('=' * 50)
print('Two adventures lie ahead.')
print('Complete the first to unlock the next')
print('=' * 50)

treasures_collected = []
treasures_merged = False # This tracks the mid game question
treasure_merged = False  # This tracks the final game question

# Using dictionaries to store the game set
game_set = {
    'A': {
        'name': 'LOC A', 'intro': 'PLACEHOLDER CLUE LOCA', 'Intro': 'loca',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCAi', 'ans': 'locai'},
            {'clue': 'PLACEHOLDER CLUE LOCAii', 'ans': 'locaii'},
            {'clue': 'PLACEHOLDER CLUE LOCAiii', 'ans': 'locaiii'},
            {'clue': 'PLACEHOLDER CLUE LOCAiv', 'ans': 'locaiv'},
            {'clue': 'PLACEHOLDER CLUE LOCAv', 'ans': 'locav'},
            {'clue': 'PLACEHOLDER CLUE LOCAvi', 'ans': 'locavi'},
        ]
    },
    'B': {
        'name': 'LOC B', 'intro': 'PLACEHOLDER CLUE LOCB', 'Intro': 'locb',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCBi', 'ans': 'locbi'},
            {'clue': 'PLACEHOLDER CLUE LOCBii', 'ans': 'locbii'},
            {'clue': 'PLACEHOLDER CLUE LOCBiii', 'ans': 'locbiii'},
            {'clue': 'PLACEHOLDER CLUE LOCBiv', 'ans': 'locbiv'},
            {'clue': 'PLACEHOLDER CLUE LOCBv', 'ans': 'locbv'},
            {'clue': 'PLACEHOLDER CLUE LOCBvi', 'ans': 'locbvi'},
        ]
    },
    'C': {
        'name': 'LOC C', 'intro': 'PLACEHOLDER CLUE LOCC', 'Intro': 'locc',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCCi', 'ans': 'locci'},
            {'clue': 'PLACEHOLDER CLUE LOCCii', 'ans': 'loccii'},
            {'clue': 'PLACEHOLDER CLUE LOCCiii', 'ans': 'locciii'},
            {'clue': 'PLACEHOLDER CLUE LOCCiv', 'ans': 'locciv'},
            {'clue': 'PLACEHOLDER CLUE LOCCv', 'ans': 'loccv'},
            {'clue': 'PLACEHOLDER CLUE LOCCvi', 'ans': 'loccvi'},
        ]
    },
    'D': {
        'name': 'LOC D', 'intro': 'PLACEHOLDER CLUE LOCD', 'Intro': 'locd',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCDi', 'ans': 'locdi'},
            {'clue': 'PLACEHOLDER CLUE LOCDii', 'ans': 'locdii'},
            {'clue': 'PLACEHOLDER CLUE LOCDiii', 'ans': 'locdiii'},
            {'clue': 'PLACEHOLDER CLUE LOCDiv', 'ans': 'locdiv'},
            {'clue': 'PLACEHOLDER CLUE LOCDv', 'ans': 'locdv'},
            {'clue': 'PLACEHOLDER CLUE LOCDvi', 'ans': 'locdvi'},
        ]
    },
    'E': {
        'name': 'LOC E', 'intro': 'PLACEHOLDER CLUE LOCE', 'Intro': 'loce',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCEi', 'ans': 'locei'},
            {'clue': 'PLACEHOLDER CLUE LOCEii', 'ans': 'loceii'},
            {'clue': 'PLACEHOLDER CLUE LOCEiii', 'ans': 'loceiii'},
            {'clue': 'PLACEHOLDER CLUE LOCEiv', 'ans': 'loceiv'},
            {'clue': 'PLACEHOLDER CLUE LOCEv', 'ans': 'locev'},
            {'clue': 'PLACEHOLDER CLUE LOCEvi', 'ans': 'locevi'},
        ]
    },
    'F': {
        'name': 'LOC F', 'intro': 'PLACEHOLDER CLUE LOCF', 'Intro': 'locf',
        'stages': [
            {'clue': 'PLACEHOLDER CLUE LOCFi', 'ans': 'locfi'},
            {'clue': 'PLACEHOLDER CLUE LOCFii', 'ans': 'locfii'},
            {'clue': 'PLACEHOLDER CLUE LOCFiii', 'ans': 'locfiii'},
            {'clue': 'PLACEHOLDER CLUE LOCFiv', 'ans': 'locfiv'},
            {'clue': 'PLACEHOLDER CLUE LOCFv', 'ans': 'locfv'},
            {'clue': 'PLACEHOLDER CLUE LOCFvi', 'ans': 'locfvi'},
        ]
    }
}

def show_doors():
    print('\n' + '=' * 50)
    print('CURRENT PROGRESS')
    print('=' * 50)
    
    has_abc = 'A' in treasures_collected and 'B' in treasures_collected and 'C' in treasures_collected
    has_def = 'D' in treasures_collected and 'E' in treasures_collected and 'F' in treasures_collected
    
    print('=' * 20)
    print('CHAPTER 1 DOORS')
    print('=' * 20)
    for door in ['A', 'B', 'C']:
        status = 'Completed' if door in treasures_collected else 'Available'
        print(f'Door {door}: {status}')
    
    print('=' * 20)
    print("CHAPTER 2 DOORS")
    print("=" * 20)
    if not has_abc:
        print("[LOCKED] Collect treasures A, B, and C first!")
    elif has_abc and not treasures_merged:
        print("[COMBINING REQUIRED] You have all 3 treasures! Type 'MERGE' to solve the final puzzle!")
    else:
        print("Chapter 1 Treasures Combined! Chapter 2 is active!")
        for door in ['D', 'E', 'F']:
            status = 'Completed' if door in treasures_collected else 'Available'
            print(f'Door {door}: {status}')
            
    if has_def and not treasure_merged:
        print('\n' + '=' * 20)
        print("FINAL ADVENTURE UNLOCKED")
        print("=" * 20)
        print("[COMBINING REQUIRED] You have all Chapter 2 treasures! Type 'MERGE' to finish the adventure!")
    elif treasure_merged:
        print('\nCONGRATULATIONS! You have completed the entire game!')

def merge_treasures_puzzle():
    global treasures_merged
    print('\n' + '=' * 50)
    print('THE CHAPTER 1 FINALE CHALLENGE')
    print('=' * 50)
    print('To fuse them and unlock Chapter 2, solve the ultimate riddle:')
    print('CLUE: PLACEHOLDER CHAPTER 1 CLUE')
    
    while True:
        ans = input('COMBINE PUZZLE > ').lower()
        if ans == 'middle answer':  
            print('\nSuccess! You may proceed to the next chapter\n')
            treasures_merged = True
            break
        else:
            print('\nIncorrect answer! Try again.\n')

def merge_treasure_final_puzzle():
    global treasure_merged
    print('\n' + '=' * 50)
    print('THE ULTIMATE GRAND FINALE')
    print('=' * 50)
    print('Combine all the treasures from Chapter 2 to claim victory!')
    print('CLUE: PLACEHOLDER FINAL CLUE')
    
    while True:
        ans = input('FINAL PUZZLE > ').lower()
        if ans == 'final answer':  
            print('\nYOU ARE A STAR!\n')
            treasure_merged = True
            break
        else:
            print('\nIncorrect answer! Try again.\n')

def play_location(door_letter):
    data = game_set[door_letter]
    while True:
        print('=' * 50)
        print(f"WELCOME TO {data['name']}")
        print('=' * 50)
        print('Solve this clue to enter the world')
        print(f"CLUE: {data['intro']}")
        
        while True:
            if input('>').lower() == data['Intro']:
                print('\nCorrect! You may continue\n')
                break
            print('\nIncorrect! Try again.\n')
        
        failed_location = False
        for stage in data['stages']:
            tries = 0
            while tries < 3:
                print(f"CLUE: {stage['clue']}")
                if input('>').lower() == stage['ans']:
                    print('\nCorrect! You may continue.\n')
                    break
                tries += 1
                print(f'\nIncorrect. Tries left: {3 - tries}')
            
            if tries == 3:
                print(f"\nYou failed too many times. Returning to {data['name']}.\n")
                failed_location = True
                break  
        
        if failed_location:
            continue
            
        print(f'\nCorrect! You found the treasure of location {door_letter}.\n')
        if door_letter not in treasures_collected:
            treasures_collected.append(door_letter)
        break

# Unified single door progression loop
while True:
    show_doors()
    
    has_abc = 'A' in treasures_collected and 'B' in treasures_collected and 'C' in treasures_collected
    has_def = 'D' in treasures_collected and 'E' in treasures_collected and 'F' in treasures_collected

    choice = input("\nChoose an option or type 'exit' to quit: ").upper()
    
    if choice == 'EXIT':
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm == 'yes' or confirm == 'y':
            if has_def and not treasure_merged:
                print("You're almost there! Thanks for playing!")
            else:
                print("Thanks for playing!")
            break
        else:
            print("\nReturning to the game...")
            continue
        
    elif choice == 'MERGE':
        if has_def and not treasure_merged:
            merge_treasure_final_puzzle()
        elif has_abc and not treasures_merged:
            merge_treasures_puzzle()
        elif treasure_merged:
            print("\nYou have completed everything already!")
        else:
            print("\nYou cannot merge yet. Keep collecting treasures!")
            
    elif choice in ['A', 'B', 'C']:
        if choice in treasures_collected:
            print(f"\nCompleted! Choose another loc.")
        else:
            play_location(choice)
        
    elif choice in ['D', 'E', 'F']:
        if not treasures_merged:
            print("\nACCESS DENIED!")
            print("You must type 'MERGE' and solve the combining question first!")
        elif choice in treasures_collected:
            print(f"\nCompleted! Choose another loc.")
        else:
            play_location(choice)
            
    else:
        print("\nInvalid choice! Please select a valid option.")
#slight hiccup: I'm trying to add a "pick another door option" and can't seem to get around it.
