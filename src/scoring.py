import yaml

with open("config.yaml") as f:
    CFG = yaml.safe_load(f)

def compute_fali(df):
    df = df.copy()

    L = (
        CFG["weights"]["status"] * df.status_f +
        CFG["weights"]["return_window"] * df.return_f +
        CFG["weights"]["minutes_drop"] * df.minutes_drop +
        CFG["weights"]["schedule"] * df.schedule_f +
        CFG["weights"]["injury_type"] * df.injury_f
    )

    L += CFG["interactions"]["status_return"] * df.status_f * df.return_f
    L += CFG["interactions"]["return_schedule"] * df.return_f * df.schedule_f
    L += CFG["interactions"]["status_minutes"] * df.status_f * df.minutes_drop

    df["fali"] = (CFG["base_score"] - L).clip(0, 100)

    def band(x):
        if x < CFG["bands"]["dnp_high"]:
            return "High DNP risk"
        if x < CFG["bands"]["dnp_medium"]:
            return "Moderate risk"
        return "Stable"

    df["risk_band"] = df.fali.apply(band)

    df["drivers"] = "status / return / minutes"

    return df
