import pandas as pd
import requests

def get_player_minutes(player_name):
    """
    Fetch last game minutes and season average minutes
    using Basketball-Reference player game log.
    """
    try:
        # crude name normalization (OK for POC)
        last, first = player_name.split(" ", 1)
        slug = (first[:2] + last[:5]).lower()

        url = f"https://www.basketball-reference.com/players/{slug[0]}/{slug}01/gamelog/2025"
        tables = pd.read_html(url)

        games = tables[0]
        games = games[games["MP"].notna()]

        minutes_last = float(games.iloc[-1]["MP"])
        minutes_avg = float(games["MP"].astype(float).mean())

        return minutes_last, minutes_avg

    except Exception:
        return None, None
