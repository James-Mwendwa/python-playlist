def team(dictionary):
    for key, val in dictionary.items():
        print(f'The {key} have {val} NBA titles')

NBA_teams = {}

while True:
    team_name = input('Enter the team name:')
    team_titles = input('Enter number of titles:')
    NBA_teams[team_name] = team_titles

    another = input('Add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

team(NBA_teams)