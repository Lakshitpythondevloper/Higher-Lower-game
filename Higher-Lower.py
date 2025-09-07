# Import Libraries
import random
import Data
import logo

# Import background

print(logo.BackGround)



# Create a function that formats the data

def format_data(ac):
    name = ac["name"]
    Description = ac["Hobbies"]
    Country = ac["Country"]

    return f"{name} a {Description} from {Country}"

# Check the user if he is wins or not and adding the scores when he wins. Create a function for that.
def check_followers(f_1,f_2,user_guess):
  if f_1 > f_2 and user_guess == 'a':
      return True
  elif f_2 > f_1 and user_guess == 'b':
      return True
  else:
      return False

Game_programm = True
Current_score = 0
while Game_programm:

    # Create two variables that contain data fo Data.py file

    account_a = random.choice(Data.Game_data)
    account_b = random.choice(Data.Game_data)

    # Import vs. background between two persons
    print(f"Current score: {Current_score}")
    print(f"Compare A: {format_data(account_a)}")
    print(logo.vs)
    print("\n")
    print(f"Vs. B: {format_data(account_b)}")

    # If there is same person then give an error message to the user.

    if account_a == account_b:
        print("Sorry there is an error! Try restart the game.")

    # Ask the user and set the variable name "guess"

    guess = input("There is a two persons Choose 'A' for 1st person or choose 'B' for second person: ").lower()

    # Add followers of the account

    follower_a = account_a["Followers_count"]
    follower_b = account_b["Followers_count"]

    is_correct = check_followers(follower_a,follower_b,guess)


    if is_correct:
        Current_score += 1
    else:
        Game_programm = False
        print("Sorry you lose the game try again!")