from manager.manager import Manager, Gameweek
from tkinter import *
import requests
import json

# root = Tk()
# root.title("FPL Mini League Viewer")

# https://fantasy.premierleague.com/api/leagues-classic/653426/standings/ 653426 HCEL fantasy League
# https://fantasy.premierleague.com/api/entry/{}/history/

try:
    api_request = requests.get(r"https://fantasy.premierleague.com/api/leagues-classic/653426/standings/")
    api = json.loads(api_request.content)

    manager_ids_and_names = []
    manager_names = []
    team_names = []
    managers_dict_list = api['standings']['results']
    manager_ids_and_names = [(manager['player_name'], manager['entry']) for manager in managers_dict_list]

    # print(manager_ids_and_names)
    fpl_dict ={}
    for name, id in manager_ids_and_names:
        api_request = requests.get(r"https://fantasy.premierleague.com/api/entry/" + str(id) + r"/history/")
        api = json.loads(api_request.content)
        Gameweeks = api['current']
        manager_GW_info = [(GW['event'], GW['points'], GW['event_transfers_cost']) for GW in Gameweeks]
        fpl_dict[name]={}

        for Gamewk, points, points_deduction in manager_GW_info:
            fpl_dict[name][Gamewk] = Gameweek(name, Gamewk, points, points_deduction)


except Exception as e:
    api = "Error....."

print(fpl_dict['Bishal Khatri'][1])




# root.mainloop()
