team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

user_input = input().split(" ")
game_over = False

for player in user_input:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break

team_a_count = len(team_a)
team_b_count = len(team_b)

print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if game_over:
    print("Game was terminated")
