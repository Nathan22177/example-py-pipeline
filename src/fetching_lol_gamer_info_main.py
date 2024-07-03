import configparser
import os

from src.rito_api_support.fetch_functions import fetch_puuid, fetch_account_id

if __name__ == '__main__':
    config = configparser.ConfigParser()

    # initialize secrets
    config.read(os.path.join(os.path.dirname(__file__), 'secrets', 'dev.ini'))
    api_key = config['dev-info']['api-key']

    #initialize conf
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    player_name = config['player-info']['player_name']
    player_tag = config['player-info']['player_tag']

    # fetch rito's internal id to use for next queries
    puuid = fetch_puuid(api_key=api_key, player_name=player_name, player_tag=player_tag)

    # fetch summoner info
    player_info_json = fetch_account_id(api_key=api_key, puuid=puuid)

    print(player_info_json)