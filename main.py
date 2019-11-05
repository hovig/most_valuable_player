"""
Written by: Hovig Ohannessian
Email: hovigg@hotmail.com
"""

import sys, glob
import pandas as pd
sys.path.insert(0, 'files')
sys.path.insert(1, 'modules')
from algorithms import open_file, read_all_lines_from_file


# Initialize variables for use
lines, hball, bball, b_collect, h_collect = [], [], [], [], []
basketball_df, handball_df = pd.DataFrame(), pd.DataFrame()

basketball_df['game_name'], basketball_df['player_name'], basketball_df['nickname'], basketball_df['number'], basketball_df['team_name'] =  '', '', '', '' , ''
basketball_df['position'], basketball_df['scored_points'], basketball_df['rebounds'], basketball_df['assists'], basketball_df['rating_points'] = '', '', '' , '', ''

handball_df['game_name'], handball_df['player_name'], handball_df['nickname'], handball_df['number'], handball_df['team_name'] = '', '', '', '' , ''
handball_df['position'], handball_df['goals_made'], handball_df['goals_received'], handball_df['rating_points'] = '', '', '', ''

b_game_name, b_player_name, b_nickname, b_number, b_team_name, b_position, b_scored_points, b_rebounds, b_assists = [], [], [], [], [], [], [], [], []
h_game_name, h_player_name, h_nickname, h_number, h_team_name, h_position, h_goals_made, h_goals_received = [], [], [], [], [], [], [], []

games = [bball, hball]
game = ''


# Loop through provided text files
for i in glob.glob('files/*.txt'):
    my_file_handle = open_file(i, 'r')
    lines_from_file = read_all_lines_from_file(my_file_handle)
    for single_line in lines_from_file:
        if i.split('.')[0].split('files/')[1].upper() == 'HANDBALL':
            hball.append(single_line.replace("\n", ""))
        elif i.split('.')[0].split('files/')[1].upper() == 'BASKETBALL':
            bball.append(single_line.replace("\n", ""))


# Loop through the list of each game type
for i,j in enumerate(games):
    for k,l in enumerate(j):
        # Get the game name from the 1st line
        if k == 0:
            game = l
        else:
            # Loop through values of each line
            for m,n in enumerate(l.split(";")):
                # Check for each game type and store values
                if game == 'BASKETBALL':
                    b_game_name.append(game)
                    if m == 0:
                        b_player_name.append(n)
                    elif m == 1:
                        b_nickname.append(n)
                    elif m == 2:
                        b_number.append(n)
                    elif m == 3:
                        b_team_name.append(n)
                    elif m == 4:
                        b_position.append(n)
                    elif m == 5:
                        b_scored_points.append(n)
                    elif m == 6:
                        b_rebounds.append(n)
                    elif m == 7:
                        b_assists.append(n)
                elif game == 'HANDBALL':
                    h_game_name.append(game)
                    if m == 0:
                        h_player_name.append(n)
                    elif m == 1:
                        h_nickname.append(n)
                    elif m == 2:
                        h_number.append(n)
                    elif m == 3:
                        h_team_name.append(n)
                    elif m == 4:
                        h_position.append(n)
                    elif m == 5:
                        h_goals_made.append(n)
                    elif m == 6:
                        h_goals_received.append(n)


# Assign values to its proper column
basketball_df['game_name'] = b_game_name[:len(b_player_name)]
basketball_df['player_name'] = b_player_name
basketball_df['nickname'] = b_nickname
basketball_df['number'] = b_number
basketball_df['team_name'] = b_team_name
basketball_df['position'] = b_position
basketball_df['scored_points'] = b_scored_points
basketball_df['rebounds'] = b_rebounds
basketball_df['assists'] = b_assists


# Calculate the rating points of each basketball player
for i,j in enumerate(basketball_df['player_name']):
    if basketball_df['position'][i] == 'C':
        b_collect.append(int(basketball_df['scored_points'][i]) * 2 + int(basketball_df['rebounds'][i]) * 1 + int(basketball_df['assists'][i]) * 3)
    elif basketball_df['position'][i] == 'F':
        b_collect.append(int(basketball_df['scored_points'][i]) * 2 + int(basketball_df['rebounds'][i]) * 2 + int(basketball_df['assists'][i]) * 2)
    elif basketball_df['position'][i] == 'G':
        b_collect.append(int(basketball_df['scored_points'][i]) * 2 + int(basketball_df['rebounds'][i]) * 3 + int(basketball_df['assists'][i]) * 1)
basketball_df['rating_points'] = b_collect


# Assign values to its proper column
handball_df['game_name'] = h_game_name[:len(h_player_name)]
handball_df['player_name'] = h_player_name
handball_df['nickname'] = h_nickname
handball_df['number'] = h_number
handball_df['team_name'] = h_team_name
handball_df['position'] = h_position
handball_df['goals_made'] = h_goals_made
handball_df['goals_received'] = h_goals_received


# Calculate the rating points of each handball player
for i,j in enumerate(handball_df['player_name']):
    if handball_df['position'][i] == 'F':
        h_collect.append(20 + int(handball_df['goals_made'][i]) * 1 + int(handball_df['goals_received'][i]) * (-1))
    elif handball_df['position'][i] == 'G':
        h_collect.append(50 + int(handball_df['goals_made'][i]) * 5 + int(handball_df['goals_received'][i]) * (-2))
handball_df['rating_points'] = h_collect


# Print the basketball most valuable player details
basketball_mvp = basketball_df[basketball_df['rating_points'] == max(basketball_df['rating_points'])]
print("Basketball MVP is the following:\n", basketball_mvp.to_json(orient='records'), "\n")


# Print the handball most valuable player details
handball_mvp = handball_df[handball_df['rating_points'] == max(handball_df['rating_points'])]
print("Handball MVP is the following:\n", handball_mvp.to_json(orient='records'), "\n")
