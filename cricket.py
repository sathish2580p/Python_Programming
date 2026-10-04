# WAP to find the total score of a cricket team by using follwing conditions 
# 1)accept the total no of user names based on the total no of input players 

total_players = 2


players_name = []

for i in range(total_players):
    name = input("Enter player name: ")
    players_name.append(name)

total_overs = int(input("Enter total overs: "))

values = [0, 1, 2, 4, 6,
          'bowled', 'catch', 'run out', 'lbw', 'stump', 'wide']

total_score = 0
wickets = 0
balls = 0

for i in range(total_overs):
    print("Over:", i + 1)

    while balls < 6:
        value = input("Enter ball result: ")

        if value.isdigit():
            value = int(value)

            if value in [0, 1, 2, 4, 6]:
                total_score = total_score + value
                balls = balls + 1

        elif value == "wide":
            total_score = total_score + 1
            # Wide does not increase balls

        elif value in ["bowled", "catch", "run out", "lbw", "stump"]:
            wickets = wickets + 1
            balls = balls + 1

        else:
            print("Invalid input")

        if wickets == total_players - 1:
            break

    if wickets == total_players - 1:
        break

print("\nPlayers:", players_name)
print("Total Score:", total_score)
print("Wickets:", wickets)
print("Overs:", balls // 6, ".", balls % 6)