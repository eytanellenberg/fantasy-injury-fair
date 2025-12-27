from src.injury_scrape import get_injuries
from src.minutes_scrape import get_minutes
from src.schedule_scrape import get_schedule

def load_data():
    return {
        "injuries": get_injuries(),
        "minutes": get_minutes(),
        "schedule": get_schedule()
    }
