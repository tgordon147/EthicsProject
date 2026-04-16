"""Simplified ethical validation pipeline inspired by twitter/the-algorithm.

Reference architecture:
https://github.com/twitter/the-algorithm

This is not a reproduction of the real X/Twitter system. It is a compact local
simulation for an AI ethics reflective report. The script demonstrates:
- candidate generation
- engagement-based ranking
- safety filtering
- diversity constraints
- fairness inspection
"""

from data import generate_tweets
from ranking import rank_tweets
from ethics import apply_safety_filter, apply_diversity_constraint, check_fairness
from utils import print_feed, print_summary, print_fairness



def main() -> None:
    tweets = generate_tweets(n=20, seed=42)

    ranked = rank_tweets(tweets)
    print_feed("RANKED (BEFORE ETHICS)", ranked)
    print_summary("RANKED FEED", ranked)
    print_fairness("FAIRNESS BEFORE", check_fairness(ranked))

    safe = apply_safety_filter(ranked)
    print_feed("AFTER SAFETY FILTER", safe)
    print_summary("POST-SAFETY FEED", safe)
    print_fairness("FAIRNESS AFTER SAFETY", check_fairness(safe))

    diverse = apply_diversity_constraint(safe, max_per_topic=3)
    print_feed("AFTER DIVERSITY CONSTRAINT", diverse)
    print_summary("FINAL FEED", diverse)
    print_fairness("FAIRNESS AFTER DIVERSITY", check_fairness(diverse))

    print("\n=== INTERPRETATION NOTES ===")
    print("1. A high-scoring harmful or misinformation tweet should appear before filtering.")
    print("2. Safety filtering removes harmful/misinformation tweets from the final candidate set.")
    print("3. Diversity constraints reduce topic dominance, especially around politics.")
    print("4. Fairness counts provide an auditable distribution of political labels.")



if __name__ == "__main__":
    main()
