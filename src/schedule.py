import pandas as pd

def compute_b2b(schedule_df):
    schedule_df = schedule_df.sort_values(["team", "date"])
    schedule_df["prev"] = schedule_df.groupby("team")["date"].shift(1)
    schedule_df["b2b"] = (
        (schedule_df["date"] - schedule_df["prev"]).dt.days == 1
    ).astype(int)
    return schedule_df[["team", "date", "b2b"]]
