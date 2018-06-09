from bs4 import BeautifulSoup
import requests
from groups import *

url = "http://www.espn.com/golf/leaderboard"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

field = soup.find_all('a', {'class':'full-name'})
players = [name.get_text() for name in field]

g = Groups()

event_group_a = []
event_group_b = []
event_group_c = []
event_group_d = []

for player in players:
    if player in g.group_a:
        event_group_a.append(player)
    elif player in g.group_b:
        event_group_b.append(player)
    elif player in g.group_c:
        event_group_c.append(player)
    else:
        event_group_d.append(player)

print("Group A")
print(event_group_a)
print("Group B")
print(event_group_b)
print("Group C")
print(event_group_c)
print("Group D")
print(event_group_d)
