from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Format the account data into a printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(guess, A_follower, B_follower):
  """Use if statement to check if user is correct."""
  if A_follower > B_follower:
    return guess == "a"
  else:
    return guess == "b"
# Display art
print(logo)
score = 0
game_should_continue = True

account_B = random.choice(data)
while game_should_continue:
  
# Generate random from the game data.
  # Making account at position B become the next account of posiition A.
  
  account_A = account_B
  account_B = random.choice(data)
  while account_A == account_B:
     account_B = random.choice(data)
  
  print(f"Comapre A: {format_data(account_A)}")
  print(vs)
  print(f"Comapre B: {format_data(account_B)}")
  # Format the account data into printable format.
  
  #Ask user for a guess.
  guess = input("Who has more followers 'A' or 'B'? ").lower()
  # Check if user is correct.
  A_follower_count = account_A["follower_count"]
  B_follower_count = account_B["follower_count"]
  
  is_correct = check_answer(guess, A_follower_count, B_follower_count)
   #get follower count of each account
  
  # Use if statment to check if user is correct.
  
  # Clear the screen between rounds.
  clear()
  print(logo)
  #Give user feedback.
  #Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Finall score: {score}")
  
  
  
  #Make the game repeatable.
  
  
  
# Making account at position B become the next account of posiition A.


