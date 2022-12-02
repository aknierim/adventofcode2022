import requests
import os

session = os.getenv('AOC_SESSION')
session_cookie = {'session': str(session)}


def get_input(year: int, day: int):
    """Get your puzzle input for a given day and year.
    """
    data_list = []
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    if session == ("" or None):
        raise ValueError("No session token provided as env variable.")

    req = requests.get(url, cookies=session_cookie, stream=True)

    for line in req.text.splitlines():
        data_list.append(line)

    return data_list
