import pandas as pd
import requests

def load_nba_schedule():
    """
    Load NBA schedule from Basketball-Reference (team schedule).
    Returns: DataFrame(team, date)
    """
    teams = [
        "ATL","BOS","BKN","CHA","CHI","CLE","DAL","DEN","DET","GSW",
        "HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK",
        "OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"
    ]

    rows = []

    for team in teams:
        try:
            url = f"https://www.basketball-reference.com/teams/{team}/2025_games.html"
            tables = pd.read_html(url)
            sched = tables[0]

            sched = sched[sched["G"].notna()]
            sched["Date"] = pd.to_datetime(sched["Date"])

            for d in sched["Date"]:
                rows.append([team, d])

        except Exception:
            continue

    return pd.DataFrame(rows, columns=["team", "date"])


def compute_b2b(schedule_df):
    schedule_df = schedule_df.sort_values(["team", "date"])
    schedule_df["prev_date"] = schedule_df.groupby("team")["date"].shift(1)

    schedule_df["b2b"] = (
        (schedule_df["date"] - schedule_df["prev_date"]).dt.days == 1
    ).astype(int)

    return schedule_df
