import requests


def fetch_puuid(api_key, player_name, player_tag):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{player_name}/{player_tag}"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    return response.json()['puuid']


def fetch_account_id(api_key, puuid):
    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": f"{api_key}"
    }

    response = requests.get(url, headers=headers)

    return response.json()
