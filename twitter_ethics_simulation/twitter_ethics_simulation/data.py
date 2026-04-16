import random
from typing import List, Dict, Any

TOPICS = ["politics", "politics", "politics", "tech", "sports", "news", "finance"]
POLITICAL_LABELS = ["left", "right", "neutral"]


def generate_tweets(n: int = 20, seed: int = 42) -> List[Dict[str, Any]]:
    """Generate a deterministic set of candidate tweets for the simulation.

    The data is intentionally shaped to create three visible report scenarios:
    1. A highly engaging harmful/misinformation tweet.
    2. Topic over-concentration (echo chamber pressure).
    3. Uneven political label distribution for fairness inspection.
    """
    random.seed(seed)
    tweets: List[Dict[str, Any]] = []

    # Intentionally insert a few fixed cases so screenshots are reliable.
    forced_cases = [
        {
            "id": 1,
            "text": "Breaking political scandal thread everyone is reacting to",
            "engagement_prob": 0.96,
            "in_network": True,
            "topic": "politics",
            "author_id": 101,
            "is_harmful": True,
            "is_misinformation": False,
            "political_label": "right",
        },
        {
            "id": 2,
            "text": "Exclusive claim about election fraud spreading fast",
            "engagement_prob": 0.94,
            "in_network": False,
            "topic": "politics",
            "author_id": 102,
            "is_harmful": False,
            "is_misinformation": True,
            "political_label": "right",
        },
        {
            "id": 3,
            "text": "Balanced explainer on policy changes",
            "engagement_prob": 0.83,
            "in_network": True,
            "topic": "politics",
            "author_id": 103,
            "is_harmful": False,
            "is_misinformation": False,
            "political_label": "neutral",
        },
        {
            "id": 4,
            "text": "Tech product launch summary",
            "engagement_prob": 0.78,
            "in_network": False,
            "topic": "tech",
            "author_id": 104,
            "is_harmful": False,
            "is_misinformation": False,
            "political_label": "neutral",
        },
        {
            "id": 5,
            "text": "Match analysis and sports highlights",
            "engagement_prob": 0.74,
            "in_network": True,
            "topic": "sports",
            "author_id": 105,
            "is_harmful": False,
            "is_misinformation": False,
            "political_label": "neutral",
        },
    ]
    tweets.extend(forced_cases)

    for i in range(6, n + 1):
        topic = random.choice(TOPICS)
        political_label = random.choices(POLITICAL_LABELS, weights=[0.2, 0.5, 0.3], k=1)[0]
        tweet = {
            "id": i,
            "text": f"Synthetic tweet {i} about {topic}",
            "engagement_prob": round(random.uniform(0.45, 0.91), 2),
            "in_network": random.choice([True, False]),
            "topic": topic,
            "author_id": random.randint(100, 110),
            "is_harmful": random.random() < 0.10,
            "is_misinformation": random.random() < 0.12,
            "political_label": political_label,
        }
        tweets.append(tweet)

    return tweets
