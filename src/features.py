def build_features(df):
    df = df.copy()

    status_map = {
        "out": 1.0,
        "doubtful": 0.8,
        "questionable": 0.6,
        "probable": 0.3
    }

    injury_map = {
        "muscle": 1.0,
        "joint": 0.6
    }

    df["status_f"] = df.status.map(status_map).fillna(0.5)
    df["injury_f"] = df.injury_type.map(injury_map).fillna(0.5)
    df["return_f"] = (df.return_days < 7).astype(int)
    df["minutes_drop"] = (
        (df.minutes_avg - df.minutes_last).clip(lower=0) / df.minutes_avg
    )
    df["schedule_f"] = df.b2b

    return df
