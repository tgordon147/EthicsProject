from collections import Counter
from typing import List, Dict, Any



def print_feed(title: str, tweets: List[Dict[str, Any]]) -> None:
    print(f"\n=== {title} ===")
    print(
        f"{'ID':<4} {'Score':<6} {'Net':<4} {'Topic':<10} {'Political':<8} "
        f"{'Harmful':<8} {'Misinfo':<8} Text"
    )
    print("-" * 100)

    for tweet in tweets:
        score = tweet.get("score", tweet.get("engagement_prob", 0.0))
        print(
            f"{tweet['id']:<4} {score:<6.2f} "
            f"{str(tweet['in_network']):<4} {tweet['topic']:<10} {tweet['political_label']:<8} "
            f"{str(tweet['is_harmful']):<8} {str(tweet['is_misinformation']):<8} {tweet['text']}"
        )



def print_summary(label: str, tweets: List[Dict[str, Any]]) -> None:
    topic_counts = Counter(tweet["topic"] for tweet in tweets)
    in_network_count = sum(1 for tweet in tweets if tweet["in_network"])
    out_network_count = len(tweets) - in_network_count
    print(f"\n--- {label} SUMMARY ---")
    print(f"Total tweets: {len(tweets)}")
    print(f"In-network: {in_network_count}")
    print(f"Out-of-network: {out_network_count}")
    print(f"Topic distribution: {dict(topic_counts)}")



def print_fairness(label: str, fairness_stats: Dict[str, int]) -> None:
    print(f"\n--- {label} ---")
    print(fairness_stats)
