import argparse
import pandas as pd
from src.ingest import load_demo_data
from src.features import build_features
from src.scoring import compute_fali
from src.decision import make_decision

def main(demo=True):
    df = load_demo_data() if demo else None
    df_feat = build_features(df)
    df_score = compute_fali(df_feat)
    df_out = make_decision(df_score)

    df_out.to_csv("outputs/weekly_table.csv", index=False)

    with open("outputs/report.md", "w") as f:
        for _, r in df_out.iterrows():
            f.write(
                f"**{r.player}** — FALI {r.fali:.0f} ({r.band})  \n"
                f"Drivers: {r.drivers}  \n"
                f"Decision: {r.decision}\n\n"
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    main(demo=args.demo)
