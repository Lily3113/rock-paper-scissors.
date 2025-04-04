import time
import random

def treasure_hunt():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    ~ Hello! Welcome to    ~
    ~   TREASURE HUNT!    ~
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    time.sleep(1)
    
    gems_won = []
    
    # Define all rounds with their properties
    rounds = [
        {
            "gem": "Ruby",
            "type": "Riddle",
            "question": "I am the 12th letter of the alphabet. What am I?",
            "hint": "The letter comes after K",
            "answer": "l",
            "emoji": "💎"
        },
        {
            "gem": "Gold",
            "type": "Riddle",
            "question": "What has keys but can't open locks?",
            "hint": "Musicians play this",
            "answer": "piano",
            "emoji": "🏆"
        },
        {
            "gem": "Diamond",
            "type": "Clue",
            "question": "I'm the hardest natural material",
            "hint": "Engagement rings often feature me",
            "answer": "diamond",
            "emoji": "💠"
        },
        {
            "gem": "Emerald",
            "type": "Riddle",
            "question": "I have cities but no houses, forests but no trees, and water but no fish. What am I?",
            "hint": "You use me for navigation",
            "answer": "map",
            "emoji": "✨"
        }
    ]
    
    # Shuffle the rounds to randomize order
    random.shuffle(rounds)
    
    # Play each round
    for i, round_data in enumerate(rounds, 1):
        print(f"\n=== ROUND {i}: Win a {round_data['gem'].upper()} ===")
        print(f"{round_data['type']}: {round_data['question']}")
        print(f"Hint: {round_data['hint']}")
        
        if input("Answer: ").lower().strip() == round_data["answer"]:
            print(f"Correct! You won a {round_data['gem'].upper()}! {round_data['emoji']}")
            gems_won.append(round_data["gem"])
        else:
            print(f"Oops! The answer was '{round_data['answer']}'")
    
    # Results
    print("\n===== FINAL RESULTS =====")
    if gems_won:
        print(f"You won {len(gems_won)} gems:")
        for gem in gems_won:
            print(f"- {gem}")
    else:
        print("You didn't win any gems this time.")
    
    print("\nThanks for playing Treasure Hunt!")

# Start the game
treasure_hunt()