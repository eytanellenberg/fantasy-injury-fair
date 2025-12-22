from src.ingest import load_data
from src.features import build_features
from src.scoring import compute_fali
from src.decision import make_decision
import os

def main():
    os.makedirs("outputs", exist_ok=True)

    df = load_data()
    df = build_features(df)
    df = compute_fali(df)
    df = make_decision(df)

    df.to_csv("outputs/weekly_table.csv", index=False)

    with open("outputs/report.md", "w") as f:
        for _, r in df.iterrows():
            f.write(
                f"**{r.player}** — FALI {r.fali:.0f} ({r.risk_band})  \n"
                f"Decision: {r.decision}\n\n"
            )

if __name__ == "__main__":
    main()
