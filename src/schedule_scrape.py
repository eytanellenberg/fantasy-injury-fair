import pandas as pd

def load_nba_schedule():
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

            # 🔑 CONVERSION DATETIME (LE FIX)
            sched["Date"] = pd.to_datetime(sched["Date"], errors="coerce")

            sched = sched[sched["Date"].notna()]

            for d in sched["Date"]:
                rows.append([team, d])

        except Exception:
            continue

    return pd.DataFrame(rows, columns=["team", "date"])


def compute_b2b(schedule_df):
    schedule_df = schedule_df.copy()

    # 🔑 ASSURE datetime
    schedule_df["date"] = pd.to_datetime(schedule_df["date"], errors="coerce")

    schedule_df = schedule_df.sort_values(["team", "date"])
    schedule_df["prev_date"] = schedule_df.groupby("team")["date"].shift(1)

    schedule_df["b2b"] = (
        (schedule_df["date"] - schedule_df["prev_date"]).dt.days == 1
    ).astype(int)

    return schedule_df
