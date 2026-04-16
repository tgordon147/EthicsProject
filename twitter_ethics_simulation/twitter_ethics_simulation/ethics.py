from collections import Counter
from typing import List, Dict, Any


def apply_safety_filter(tweets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Remove tweets flagged as harmful or misinformation."""
    return [
        tweet for tweet in tweets
        if not tweet["is_harmful"] and not tweet["is_misinformation"]
    ]



def check_fairness(tweets: List[Dict[str, Any]]) -> Dict[str, int]:
    """Report political label distribution for auditing purposes."""
    counts = Counter(tweet["political_label"] for tweet in tweets)
    return {
        "left": counts.get("left", 0),
        "right": counts.get("right", 0),
        "neutral": counts.get("neutral", 0),
    }



def apply_diversity_constraint(tweets: List[Dict[str, Any]], max_per_topic: int = 3) -> List[Dict[str, Any]]:
    """Limit topic dominance in the final feed."""
    topic_counts: Dict[str, int] = {}
    diverse_feed: List[Dict[str, Any]] = []

    for tweet in tweets:
        topic = tweet["topic"]
        if topic_counts.get(topic, 0) < max_per_topic:
            diverse_feed.append(tweet)
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

    return diverse_feed
