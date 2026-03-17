import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    
    your_score = 0
    computer_score = 0
    
    print("---Rock Paper Scissors Game---")
    print("Press q for exit the game.\n")
    
    while True:
        your_choice = input("Your choice is (rock, paper, scissors): ").lower()
        
        if your_choice == 'q':
            print("\nGame Over!")
            print(f"General Score -> You: {your_score} - Computer: {computer_score}")
            break
        
        if your_choice not in options:
            print("Please choose right ones.")
            continue
        
        computer_option = random.choice(options)
        print(f"Computer's Choice: {computer_option}")
        
        if your_choice == computer_option:
            print("Draw! 🤝")
            
        elif (your_choice == "rock" and computer_option == "scissors") or \
            (your_choice == "paper" and computer_option == "rock") or \
            (your_choice == "scissors" and computer_option == "paper"):
                print("You Won! 🎉")
                your_score += 1
                
        else:
            print("You Lose. 🤖")
            computer_score += 1
            
        print(f"Score: You {your_score} - {computer_score} Computer\n" + "-"*30)
        
if __name__ == "__main__":
    rock_paper_scissors()