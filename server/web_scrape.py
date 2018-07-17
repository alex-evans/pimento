from bs4 import BeautifulSoup
import requests
from groups import *

class Event:

    def __init__(self): 

        # url = "http://www.espn.com/golf/leaderboard"
        # url = "http://www.espn.com/golf/leaderboard?tournamentId=401025255"
        # url = "http://travelerschampionship.com/travelers-championship-announces-2018-player-field/"
        url = "http://www.espn.com/golf/leaderboard?tournamentId=401025259"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        field = soup.find_all('a', {'class':'full-name'})
        # field = soup.find_all('td')
        # players = [name.get_text().replace(" ","") for name in field]
        players = [name.get_text() for name in field]

        g = Groups()

        self.event_group_a = []
        self.event_group_b = []
        self.event_group_c = []
        self.event_group_d = []
        self.field = field
        for player_name in players:
        #     player_array = player.split(",")
        #     player_name = player_array[1] + " " + player_array[0]
            if player_name in g.group_a:
                self.event_group_a.append(player_name)
            elif player_name in g.group_b:
                self.event_group_b.append(player_name)
            elif player_name in g.group_c:
                self.event_group_c.append(player_name)
            else:
                self.event_group_d.append(player_name)


if __name__=='__main__':

    event = Event()

    print("Group A")
    print(event.event_group_a)
    print("Group B")
    print(event.event_group_b)
    print("Group C")
    print(event.event_group_c)
    print("Group D")
    print(event.event_group_d)
