import pandas as pd
from src.injury_scrape import scrape_injuries

def load_data():
    injury = scrape_injuries()

    # minutes (exemple minimal, à brancher plus tard)
    minutes = pd.DataFrame({
        "player": injury.player,
        "minutes_last": 28,
        "minutes_avg": 34
    })

    df = injury.merge(minutes, on="player", how="left")
    df["b2b"] = 0  # branchable plus tard

    return df
