import random

def treasure_game():
    print("🧭 Welcome to Treasure Finder! 🏆")
    print("Find the hidden treasure in 3 guesses!\n")
    
    treasure = random.choice(["beach", "forest", "cave"])
    hints = {
        "beach": ["Look where waves crash", "Sand castles nearby", "Seagulls fly above"],
        "forest": ["Listen for owls", "Tall trees guard it", "Moss grows near"],
        "cave": ["Watch for bats", "Echoes point the way", "Stalactites hang above"]
    }
    
    for attempt in range(3):
        print(f"\nGuess {attempt+1}: Where is the treasure?")
        print("1. Beach 🏖️  2. Forest 🌲  3. Cave 🕳️")
        guess = input("Choose (1-3): ")
        
        location = ["beach", "forest", "cave"][int(guess)-1]
        
        if location == treasure:
            print(f"\n🎉 You found the treasure in the {treasure}! 🏆")
            return
        else:
            print(f"\nNot here! Hint: {hints[treasure][attempt]}")
    
    print(f"\n💔 Game Over! The treasure was in the {treasure}.")

treasure_game()



