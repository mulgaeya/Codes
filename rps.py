import random 

def play():
    user = input("'1' for rock, '2' for paper, '3' for scissors\n")
    computer = random.choice(['1', '2', '3'])

    if user == computer:
        return "tie"

    if isWin(user, computer):
        return "you won!"
    
    return 'you lost!'

# 1(rock) > 3(scissors), 3 > 2(paper), 2 > 1
def isWin(player, opponent):
    # return true if player wins
    if (player == '1' and opponent == '3') or (player == '3' and opponent == '2') \
        or (player == '2' and opponent == '1'):
        return True

print(play())


