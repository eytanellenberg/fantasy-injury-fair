import os
from src.ingest import load_data
from src.features import build_features
from src.scoring import compute_fali
from src.decision import make_decision

def main():
    os.makedirs("outputs", exist_ok=True)

    # --- RUN PIPELINE ---
    df = load_data()
    df = build_features(df)
    df = compute_fali(df)
    df = make_decision(df)

    # --- SAVE TABLE ---
    df.to_csv("outputs/weekly_table.csv", index=False)

    # --- BUILD NEWSLETTER REPORT ---
    bench = df[df.decision == "Bench"]
    risky = df[df.decision == "Risky start"]
    start = df[df.decision == "Start"]

    with open("outputs/report.md", "w") as f:
        f.write(
            "**NBA Fantasy Injury Intelligence — Weekly Decision Brief (Pilot)**\n\n"
            "This report focuses on **availability and short-term risk**, not injury labels.\n"
            "Goal: help with **start / bench decisions** this week.\n\n"
            "---\n\n"
        )

        # ⚠️ BENCH
        f.write("### ⚠️ High DNP / Bench Risk\n")
        if bench.empty:
            f.write("- No major bench risks detected this week.\n\n")
        else:
            for _, r in bench.iterrows():
                f.write(
                    f"- **{r.player}** — {r.risk_band}  \n"
                    f"  Decision: **Bench**\n\n"
                )

        # 🟡 RISKY
        f.write("### 🟡 Active but Limited (Risky Starts)\n")
        if risky.empty:
            f.write("- No major risky starts detected.\n\n")
        else:
            for _, r in risky.iterrows():
                f.write(
                    f"- **{r.player}** — workload / availability risk  \n"
                    f"  Decision: **Risky start**\n\n"
                )

        # 🟢 START
        f.write("### 🟢 Cleared / Stable\n")
        if start.empty:
            f.write("- No clear stable starts flagged.\n\n")
        else:
            for _, r in start.iterrows():
                f.write(
                    f"- **{r.player}** — low availability risk  \n"
                    f"  Decision: **Start**\n\n"
                )

        # FOOTER
        f.write(
            "---\n"
            "*This is a pilot report. The focus is on decision clarity rather than volume.*\n"
        )

if __name__ == "__main__":
    main()
