import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def retrieve_songs(user_prefs: Dict, songs: List[Dict]) -> List[Dict]:
    """Retrieve a smaller set of relevant songs before scoring."""

    retrieved = []

    for song in songs:
        genre_match = song["genre"] == user_prefs["genre"]
        mood_match = song["mood"] == user_prefs["mood"]

        if genre_match or mood_match:
            retrieved.append(song)

    if not retrieved:
        print("[Retriever] No exact genre or mood match found. Using full catalog.")
        return songs

    print(f"[Retriever] Retrieved {len(retrieved)} candidate songs.")
    return retrieved

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a score and explanation reasons for a song."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = max(0, 1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_score
    reasons.append(f"energy close match (+{energy_score:.2f})")

    tempo_score = max(0, 1 - abs(song["tempo_bpm"] - user_prefs["tempo"]) / 100)
    score += tempo_score
    reasons.append(f"tempo close match (+{tempo_score:.2f})")

    valence_score = max(0, 1 - abs(song["valence"] - user_prefs["valence"]))
    score += valence_score
    reasons.append(f"valence close match (+{valence_score:.2f})")

    danceability_score = max(0, 1 - abs(song["danceability"] - user_prefs["danceability"]))
    score += danceability_score
    reasons.append(f"danceability close match (+{danceability_score:.2f})")

    acousticness_score = max(0, 1 - abs(song["acousticness"] - user_prefs["acousticness"]))
    score += acousticness_score
    reasons.append(f"acousticness close match (+{acousticness_score:.2f})")

    valence_score = max(0, 1 - abs(song.get("valence", 0) - user_prefs.get("valence", 0)))

    return score, reasons    


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return top k scored songs with explanations."""
    scored_songs = []

    candidate_songs = retrieve_songs(user_prefs, songs)

    for song in candidate_songs:
        score, reasons = score_song(user_prefs, song)

        confidence = min(score / 8.0, 1.0)

        explanation = ", ".join(reasons)
        explanation += f", confidence: {confidence:.2f}"

        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    print(f"[Recommender] Scored {len(candidate_songs)} songs and returning top {k}.")
    return scored_songs[:k]    
