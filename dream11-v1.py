import itertools

# Player Sentimental Data
player_sentimental = {
    'Ravindra Jadeja': 80,
    'Ruturaj Gaikwad': 80,
    'Faf du Plessis': 80,
    'Virat Kohli': 70,
    'Rachin Ravindra': 70,
    'Daryl Mitchell': 70,
    'Shivam Dube': 70,
    'Mustafizur Rahman': 70,
    'Deepak Chahar': 60,
    'Ajinkya Rahane': 60,
    'Glenn Maxwell': 50,
    'Cameron Green': 50,
    'Maheesh Theekshana': 40,
    'Tushar Deshpande': 40,
    'Dinesh Karthik': 30,
    'Mohammed Siraj': 30,
    'Alzarri Joseph': 30,
    'Anuj Rawat': 30,
    'MS Dhoni': 20,
    'Karn Sharma': 20,
    'Mayank Dagar': 20,
    'Rajat Patidar': 20,
    'Sameer Rizvi': 20,
    'Yash Dayal': 10
}

# Sort players based on sentimental values in descending order
sorted_players = sorted(player_sentimental.items(), key=lambda x: x[1], reverse=True)

# Divide players into two groups: sentimental value 100 and less than 100
sentimental_100 = [player for player, sentiment in sorted_players if sentiment == 100]
sentimental_less_100 = [player for player, sentiment in sorted_players if sentiment < 100]

# Create combinations for players with sentimental value 100
teams = list(itertools.product(sentimental_100, repeat=11))

# Assign players with sentimental value less than 100 to remaining teams
remaining_players = sentimental_less_100 * 20
for i, team in enumerate(teams):
    for player in team:
        if player not in sentimental_100:
            teams[i] += (remaining_players.pop(0),)

# Print the 20 combinations of teams
for i, team in enumerate(teams, 1):
    print(f"Team {i}: {team}")
