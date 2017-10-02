from wikitables import import_tables
import sqlite3

#
# # pulls data from wikipedia table
# teams = 'Major professional sports teams of the United States and Canada'
#
# teams_dict = import_tables(teams)
# data = []
#
# # creates a list of dictionary elements
# for row in teams_dict[0].rows:
#     data.append(row)
#
# # converts the dictionary values from objects to strings
# for i in data:
#     for k in i:
#         i[k] = str(i[k])
#
#
# # create a new SQLlite database and generates a cursor for SQL execution
# conn = sqlite3.connect('sports_teams_database.sqlite')
# cur = conn.cursor()
#
#
# cur.execute('''CREATE TABLE sports_table1(id INTEGER PRIMARY KEY, team TEXT, city TEXT, league TEXT)''')
#
# for i in data:
#     cur.execute('''INSERT INTO sports_table1(team, city, league) VALUES(:Team, :City, :League)''', i)
#
#
# conn.commit()
# conn.close()

nba_players = 'List of current NBA team rosters'

nba_players_dict = import_tables(nba_players)

print(nba_players_dict)