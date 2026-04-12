"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv")

    user1 = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.4,
        "tempo": 80,
        "valence": 0.5,
        "acousticness": 0.8,
        "danceability": 0.6
    }

    user2 = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "tempo": 130,
        "valence": 0.8,
        "acousticness": 0.2,
        "danceability": 0.9
    }

    user3 = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "tempo": 150,
        "valence": 0.4,
        "acousticness": 0.1,
        "danceability": 0.6
    }

    profiles = [
        ("Chill Lofi", user1),
        ("High Energy Pop", user2),
        ("Intense Rock", user3),
    ]

    for name, prefs in profiles:
        print(f"\n=== {name} ===\n")
        recommendations = recommend_songs(prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()