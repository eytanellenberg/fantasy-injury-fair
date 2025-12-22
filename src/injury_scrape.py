import requests
from bs4 import BeautifulSoup
import pandas as pd

def normalize_status(s):
    s = s.lower()
    if "out" in s:
        return "out"
    if "doubt" in s:
        return "doubtful"
    if "quest" in s:
        return "questionable"
    if "prob" in s:
        return "probable"
    return "unknown"

def scrape_injuries():
    url = "https://www.espn.com/nba/injuries"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    rows = []
    for table in soup.find_all("table"):
        for row in table.find_all("tr")[1:]:
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cols) >= 4:
                player = cols[0]
                status = normalize_status(cols[2])
                injury = cols[3].lower()

                injury_type = "muscle" if any(x in injury for x in ["hamstring", "calf", "quad"]) else "joint"
                rows.append([player, status, injury_type, 3])

    return pd.DataFrame(rows, columns=[
        "player", "status", "injury_type", "return_days"
    ])
