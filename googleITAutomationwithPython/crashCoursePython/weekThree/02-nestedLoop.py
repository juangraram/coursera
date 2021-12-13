# Example nested loops
for left in range(7):
    for right in range (left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        # if home_team is not equal to away_team
        if home_team != away_team:
            print(home_team + " vs " + away_team)
