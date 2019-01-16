import time
import random 

print('Rock...')
time.sleep(0.5)
print('Paper...')
time.sleep(0.5)
print('Scissors...')
time.sleep(0.5)
print('Shoot!')

# Player picks what weapon to play
player_move = input('What move do you chose? ')

# Computer chooses it's move
computer_move = random.choice(["Rock", "Paper", "Scissors"])

print('Player move is: ' + player_move)
print('Computer move is: ' + computer_move)

if player_move == "Rock" and computer_move == "Scissors":
	print("You win! Rock crushes scissors.")
if player_move == "Rock" and computer_move == "Paper":
	print("you lose! paper covers rock.")
if player_move == "Scissors" and computer_move == "Paper":
	print("You win! Scissors cuts Paper.")
	if player_move == "Rock" and computer_move == "Rock":
	print("Its a tie!.")
	if player_move == "Scissors" and computer_move == "scissors":
	print("Its a tie!.")
	if player_move == "Paper" and computer_move == "Paper":
	print("Its a tie!.")
	if player_move == "Paper" and computer_move == "Scissors":
	print("You lose! Scissors cuts Paper.")
	if player_move == "scissors" and computer_move == "Rock":
	print("You lose! Rock crushes Scissors.")
	