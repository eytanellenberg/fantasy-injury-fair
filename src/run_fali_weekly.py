import os
import datetime
import pandas as pd

# ---------------------------
# Setup
# ---------------------------
os.makedirs("outputs", exist_ok=True)

today = datetime.date.today().isoformat()
week_id = datetime.date.today().isocalendar().week

# ---------------------------
# Mock FAIR / PAI data
# (remplaçable plus tard par ton vrai moteur)
# ---------------------------
data = [
    {
        "player": "Anthony Davis",
        "team": "LAL",
        "availability_risk": "Volatile",
        "pai_signal": "Managed availability",
        "classification": "High ceiling / hedge zeros"
    },
    {
        "player": "Joel Embiid",
        "team": "PHI",
        "availability_risk": "Structural shutdown risk",
        "pai_signal": "Threshold-based collapse",
        "classification": "Elite but timing-sensitive"
    },
    {
        "player": "Damian Lillard",
        "team": "MIL",
        "availability_risk": "Low",
        "pai_signal": "Late-usage readiness collapse",
        "classification": "Plays but outcome risk"
    }
]

df = pd.DataFrame(data)

# ---------------------------
# Write CSV output
# ---------------------------
csv_path = "outputs/fali_weekly_players.csv"
df.to_csv(csv_path, index=False)

# ---------------------------
# Write Markdown editorial
# ---------------------------
md_path = "outputs/fali_weekly.md"

with open(md_path, "w") as f:
    f.write(f"# FALI Weekly — Week {week_id}\n\n")
    f.write(f"_Run date: {today}_\n\n")
    f.write("## What this is\n")
    f.write(
        "This is a weekly **FAIR / PAI** fantasy intelligence brief.\n"
        "It is not an injury report.\n"
        "It explains **why fantasy value is limited**, even when players are available.\n\n"
    )

    f.write("## Key profiles this week\n\n")

    for _, row in df.iterrows():
        f.write(f"### {row['player']} ({row['team']})\n")
        f.write(f"- Availability risk: **{row['availability_risk']}**\n")
        f.write(f"- PAI signal: **{row['pai_signal']}**\n")
        f.write(f"- Fantasy read: {row['classification']}\n\n")

    f.write("---\n")
    f.write(
        "_Method: FAIR (Factor Attribution for Impact & Risk) / "
        "PAI (Performance Attribution Index), proprietary framework._\n"
    )

print("FALI weekly run completed successfully.")
