from art import logo, vs
from game_data import data
import random

# format the account data into printable format
def format_data(account):
  """Format the account data into printable format."""
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
  """use if statement to check if user is correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    

# display
print(logo)
# score keeping
score = 0
game_should_continue = True
account_b = random.choice(data)  
# make the game repeatable
while game_should_continue:
  # generate random accounts from game data

  # move the option B to become the option A
  account_a = account_b
  account_b = random.choice(data)  
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  # ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # check if user is correct
  ## get follower count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  # give user feedback on their guesses
  if is_correct:
    score += 1
    print(f"You're right. Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, thats wrong. Final score: {score}.")