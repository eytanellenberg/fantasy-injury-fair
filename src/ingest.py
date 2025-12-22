import pandas as pd

def load_demo_data():
    data = {
        "player": ["Player A", "Player B", "Player C"],
        "status": ["questionable", "probable", "out"],
        "return_days": [3, 14, 0],
        "minutes_last": [22, 34, 0],
        "minutes_avg": [34, 36, 30],
        "b2b": [1, 0, 0],
        "injury_type": ["muscle", "joint", "muscle"]
    }
    return pd.DataFrame(data)
