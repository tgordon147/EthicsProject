from typing import List, Dict, Any


def rank_tweets(tweets: List[Dict[str, Any]], in_network_bonus: float = 0.05) -> List[Dict[str, Any]]:
    """Rank tweets by a simple engagement-first score.

    This loosely mirrors the idea from the twitter/the-algorithm repository that
    candidate items are scored and ordered using engagement-oriented signals.
    """
    ranked = []
    for tweet in tweets:
        scored = dict(tweet)
        score = scored["engagement_prob"] + (in_network_bonus if scored["in_network"] else 0.0)
        scored["score"] = round(score, 3)
        ranked.append(scored)

    ranked.sort(key=lambda t: t["score"], reverse=True)
    return ranked
