import random
import colorama
from colorama import Fore, Style

# Initialize colorama for color support on Windows
colorama.init(autoreset=True)

def generate_code():
    """Generate a 3-digit code with unique digits."""
    digits = list(range(10))
    code = random.sample(digits, 3)
    return code

def provide_hint(guess, code):
    """Provide a hint based on the player's guess."""
    hint = []
    correct_in_place = 0
    correct_out_of_place = 0

    # Check for digits that are correct and in the right place
    for i in range(3):
        if guess[i] == code[i]:
            correct_in_place += 1
            hint.append(f"{Fore.GREEN}{guess[i]} (correct position){Style.RESET_ALL}")
        elif guess[i] in code:
            correct_out_of_place += 1
            hint.append(f"{Fore.YELLOW}{guess[i]} (wrong position){Style.RESET_ALL}")
        else:
            hint.append(f"{Fore.RED}{guess[i]} (not in code){Style.RESET_ALL}")

    hint_description = (
        f"{Fore.GREEN}{correct_in_place} correct in place{Style.RESET_ALL}, "
        f"{Fore.YELLOW}{correct_out_of_place} correct but in wrong place{Style.RESET_ALL}"
    )

    return hint, hint_description

def create_game():
    """Main function to run the guessing game."""
    code = generate_code()
    
    print(f"{Fore.CYAN}A 3-digit code has been generated. Try to guess it!{Style.RESET_ALL}")
    
    while True:
        guess = input(f"{Fore.CYAN}Enter your 3-digit guess: {Style.RESET_ALL}")

        if not guess.isdigit() or len(guess) != 3:
            print(f"{Fore.RED}Invalid input. Please enter exactly 3 digits.{Style.RESET_ALL}")
            continue
        
        guess = list(map(int, guess))
        if guess == code:
            print(f"{Fore.GREEN}Congratulations! You've guessed the code correctly!{Style.RESET_ALL}")
            break
        
        hint, description = provide_hint(guess, code)
        print(f"Hint: {' | '.join(hint)}")
        print(f"Summary: {description}\n")
    
    print(f"The correct code was: {code}")
    replay = input(f"{Fore.CYAN}Do you want to play again? (Y/N)\n{Style.RESET_ALL}").lower()
    if replay == 'y':
        print("\n" * 30)
        create_game()

if __name__ == "__main__":
    create_game()
