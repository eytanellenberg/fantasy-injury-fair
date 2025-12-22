import yaml

with open("config.yaml") as f:
    CFG = yaml.safe_load(f)

def make_decision(df):
    df = df.copy()

    def decide(x):
        if x < CFG["thresholds"]["risky"]:
            return "Bench"
        if x < CFG["thresholds"]["start"]:
            return "Risky start"
        return "Start"

    df["decision"] = df.fali.apply(decide)
    return df
