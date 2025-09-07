# Higher-Lower Game 🎮

A fun and interactive Python-based guessing game where players compare the follower counts of different personalities. Test your intuition and knowledge while trying to achieve the highest score possible!

## 🎯 Game Description

The Higher-Lower game is a simple yet engaging game where players are presented with two personalities and must guess which one has more followers. The game continues as long as the player makes correct guesses, with each correct guess adding to their score.

## ✨ Features

- Beautiful ASCII art interface
- Random selection of personalities from a data set
- Score tracking system
- Interactive command-line interface
- Continuous gameplay until wrong guess

## 🛠️ Code Structure

The game is built using Python and consists of several key components:

### Main Components

1. **Imports and Setup**
   ```python
   import random
   import Data
   import logo
   ```
   - The game utilizes the `random` module for selecting personalities
   - Custom modules `Data` and `logo` contain game data and ASCII art

2. **Data Formatting Function**
   ```python
   def format_data(ac):
       name = ac["name"]
       Description = ac["Hobbies"]
       Country = ac["Country"]
       return f"{name} a {Description} from {Country}"
   ```
   - Formats the personality data for display
   - Shows name, hobbies, and country of origin

3. **Comparison Function**
   ```python
   def check_followers(f_1, f_2, user_guess):
       if f_1 > f_2 and user_guess == 'a':
           return True
       elif f_2 > f_1 and user_guess == 'b':
           return True
       else:
           return False
   ```
   - Validates user guesses
   - Compares follower counts
   - Returns True for correct guesses, False otherwise

### Game Loop

The main game loop:
- Randomly selects two different personalities
- Displays their information with VS screen
- Takes user input ('A' or 'B')
- Updates score for correct guesses
- Continues until an incorrect guess is made

## 🎮 How to Play

1. Run the Python script
2. You'll be presented with two personalities, A and B
3. Type 'A' or 'B' to guess who has more followers
4. For each correct guess, your score increases by 1
5. Game continues until you make a wrong guess
6. Try to achieve the highest score possible!

## 🔧 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Lakshitpythondevloper/Higher-Lower-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Higher-Lower-game
   ```
3. Run the game:
   ```bash
   python Higher-Lower.py
   ```

## 🎯 Game Logic

The game follows this logical flow:
1. Two random personalities are selected from the database
2. Their information is displayed to the player
3. Player makes a guess
4. The follower counts are compared
5. Score is updated if correct
6. Game continues with new personalities if correct
7. Game ends if guess is incorrect

## 🌟 Features Explained

### Random Selection
- Uses Python's `random.choice()` to select personalities
- Ensures no duplicate selections in the same round

### Score Tracking
- Maintains a running score (`Current_score`)
- Displays score before each round
- Final score shown when game ends

### Error Handling
- Checks for duplicate personality selection
- Handles case-insensitive user input
- Clear feedback on game end

## 📝 Dependencies

- Python 3.x
- Custom modules:
  - `Data.py` (contains personality database)
  - `logo.py` (contains ASCII art)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for bugs or feature requests.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Happy Gaming! 🎮
