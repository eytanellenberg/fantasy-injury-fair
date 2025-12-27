from src.ingest import load_data
from src.features import build_features
from src.scoring import score_availability
from src.decision import build_decision_frame

def run():
    raw = load_data()
    features = build_features(raw)
    scores = score_availability(features)
    decisions = build_decision_frame(scores)
    return decisions

if __name__ == "__main__":
    run()
