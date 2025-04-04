import random
import time

# Game setup
lives = 3
treasure_found = False

def game_over(reason):
    print(f"\n💀 Game Over! {reason}")
    exit()

def tree_of_wisdom():
    global treasure_found
    riddles = [
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What gets wetter as it dries?", "answer": "towel"},
        {"question": "I'm tall when young and short when old. What am I?", "answer": "candle"},
        {"question": "What has a head, a tail, but no body?", "answer": "coin"},
        {"question": "What can travel the world while staying in a corner?", "answer": "stamp"}
    ]
    
    print("\n🌳 You reach the Tree of Wisdom!")
    print("Answer all 5 riddles correctly to win the treasure!\n")
    
    correct = 0
    for riddle in riddles:
        print(f"❓ Riddle: {riddle['question']}")
        answer = input("Your answer: ").lower().strip()
        
        if answer == riddle['answer']:
            print("✅ Correct!\n")
            correct += 1
        else:
            print(f"❌ Wrong! The answer was: {riddle['answer']}\n")
    
    if correct == 5:
        print("🎉 You solved all riddles!")
        print("🏆 You found the treasure: **Golden Amulet of Wisdom**")
        treasure_found = True
    else:
        game_over(f"You got {correct}/5 correct. The tree denies you the treasure.")

def trap_labyrinth():
    print("\n⚫ You enter a dark, winding passage...")
    time.sleep(2)
    print("The walls start closing in...")
    time.sleep(2)
    print("You step on a hidden pressure plate!")
    time.sleep(1)
    game_over("💀 Poison darts shoot from the walls!")

def door_challenge():
    print("\n🚪 You stand before three mysterious doors:")
    print("1. 🔴 Red Door ")
    print("2. 🔵 Blue Door ")
    print("3. 🟢 Green Door ")
    
    choice = input("Choose a door (1-3): ")
    
    if choice == "1":
        print("\nYou open the Red Door...")
        time.sleep(1)
        print("It leads back to the start!")
        return "restart"
    elif choice == "2":
        print("\nYou open the Blue Door...")
        time.sleep(1)
        print("🌀 You're teleported to the second door!")
        time.sleep(1)
        print("It's a mirror! You're teleported again!")
        time.sleep(1)
        print("🌳 You appear before the Tree of Wisdom!")
        tree_of_wisdom()
    elif choice == "3":
        print("\nYou open the Green Door...")
        time.sleep(1)
        print("🌌 A dark pit awaits!")
        game_over("You fall into the abyss!")
    else:
        print("Invalid choice! The doors vanish!")
        game_over("The labyrinth collapses!")

def main():
    global lives
    print("=== 🏰 The Treasure Hunt===")
    print("Choose your path wisely...")
    
    while lives > 0 and not treasure_found:
        print(f"\n❤️ Lives: {lives}")
        print("1. ⚪ White Labyrinth ")
        print("2. ⚫ Black Labyrinth ")
        print("3. ⚡ Silver Labyrinth ")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            tree_of_wisdom()
        elif choice == "2":
            trap_labyrinth()
        elif choice == "3":
            result = door_challenge()
            if result == "restart":
                continue
        else:
            print("❌ Invalid choice! You lose a life.")
            lives -= 1
            continue
    
    if lives <= 0:
        game_over("You ran out of lives!")
    elif treasure_found:
        print("\n✨ You escaped with the treasure! You win!")

if __name__ == "__main__":
    main()



import random

def treasure_hunt():
    print("🏆 Treasure Hunt!")
    spots = ["beach", "forest", "cave"]
    treasure = random.choice(spots)
    
    for attempt in range(3, 0, -1):
        print(f"\nAttempts left: {attempt}")
        print("Search: 1.Beach 2.Forest 3.Cave")
        
        try:
            if spots[int(input("Choose 1-3: "))-1] == treasure:
                print(f"🎉 Found the treasure at {treasure}!")
                return
            print(f"💡 Hint: {' '.join(random.sample(treasure, len(treasure)))}")
        except:
            print("Invalid input!")
    
    print(f"💀 Game Over! Treasure was at {treasure}")

treasure_hunt()




