import pandas as pd
from src.injury_scrape import scrape_injuries
from src.minutes_scrape import get_player_minutes
from src.schedule_scrape import load_nba_schedule, compute_b2b

def load_data():
    # injuries
    injury = scrape_injuries()

    # minutes
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

    # schedule
    schedule = load_nba_schedule()
    schedule = compute_b2b(schedule)

    # ⚠️ POC simplification :
    # we assume all players play on their team's next game date
    # and we only care if that game is B2B
    # (sufficient for fantasy weekly risk)

    # TEMP mapping player -> team (to improve later)
    injury["team"] = "UNK"

    df = injury.merge(minutes, on="player", how="left")
    df["b2b"] = schedule.b2b.max()  # conservative: if team has B2B this week

    return df
