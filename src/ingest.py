import pandas as pd
from src.injury_scrape import scrape_injuries
from src.minutes_scrape import get_player_minutes

def load_data():
    injury = scrape_injuries()

    minutes_rows = []

    for p in injury.player.unique():
        ml, ma = get_player_minutes(p)
        minutes_rows.append([
            p,
            ml if ml is not None else 28,
            ma if ma is not None else 34
        ])

    minutes = pd.DataFrame(
        minutes_rows,
        columns=["player", "minutes_last", "minutes_avg"]
    )

    df = injury.merge(minutes, on="player", how="left")
    df["b2b"] = 0  # schedule auto branchable next

    return df
