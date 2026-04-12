# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0

---

## 2. Intended Use  

This recommender suggests songs based on a user's preferences such as genre, mood, and energy. It is designed for classroom exploration to demonstrate how recommendation systems work.
It assumes that users have simple, clearly defined preferences and does not account for complex or changing tastes. It is not intended for real-world use.  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

This recommender system is inspired by how platforms like Spotify and YouTube suggest music.
There are two main approaches. Collaborative filtering recommends songs based on what similar users enjoy. For example, if many users who like one song also listen to another, that second song may be recommended. Content-based filtering focuses on the characteristics of songs, such as genre, tempo, and mood. If a user likes calm acoustic songs, the system suggests similar tracks with those features.
These systems use different types of data, including user interactions like plays, skips, likes, and playlist additions. They also use song attributes such as genre, energy, and tempo to understand music characteristics.
Most real systems combine both approaches to build a taste profile and recommend songs that best match a user’s preferences. 
From the songs.csv dataset, the available features include genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.
For a simple vibe-based recommender, the most useful features are mood, energy, valence, and tempo. Mood gives a direct idea of how a song feels, while energy and tempo describe how intense or fast it is. Valence helps capture whether a song sounds more positive or negative.
Genre is also helpful for grouping similar types of music, while features like danceability and acousticness can add extra detail to the overall vibe.
These features make sense because people often choose music based on how it feels, rather than just the artist or title.
To recommend songs, the system gives each song a score based on how closely it matches the user’s preferences.
For genre and mood, the scoring is simple. If the song matches the user’s preferred genre or mood, it earns more points.
For numerical features like energy and tempo, the system checks how close the song is to the user’s preferred value. Songs with values closer to the preference receive higher scores, while songs that are farther away receive lower scores.
The final score is a weighted combination of genre, mood, energy, and tempo. For example, mood and genre may have slightly higher weights because they strongly shape the overall vibe, while energy and tempo help fine-tune the match.
After every song receives a score, the system ranks all songs from highest to lowest and recommends the top matches.
In this implementation, the scoring system uses specific weights. A song gets +2.0 points if its genre matches the user’s preferred genre and +1.0 point if its mood matches. For numerical features like energy and tempo, the system gives higher scores when the song’s values are closer to the user’s preferences. Smaller similarity scores are also added for valence, danceability, and acousticness. After calculating a total score for each song, the system sorts them from highest to lowest and recommends the top results.

---

## 4. Data  

The dataset contains 17 songs with features such as genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.

The dataset includes a mix of genres like pop, lofi, rock, jazz, and ambient. However, it is very small and does not represent the full diversity of music tastes. 

---

## 5. Strengths  

The system works well for users with clear preferences, such as Chill Lofi or High Energy Pop. In these cases, the recommendations matched the expected vibe and included songs that felt appropriate.

The scoring system successfully captures patterns like matching genre and mood, and it uses numerical features to fine-tune recommendations.

---

## 6. Limitations and Bias 

This recommender system has some biases because of how the scoring logic is designed. It gives strong importance to genre and mood, which can cause it to favor songs with exact label matches over songs that might still fit the user’s taste in other ways.

During testing, I removed the mood feature and noticed that the rankings changed, especially for the Chill Lofi profile. A song like *Focus Flow* moved above songs that better matched the original vibe, showing that numerical similarity alone does not always capture how music feels to a listener.

The dataset is also very small, which limits diversity and can make the system repeat similar results. Because of this, the recommender may create a small “filter bubble” and may not represent the full range of musical taste.

---

## 7. Evaluation

I tested the recommender using three different user profiles: Chill Lofi, High Energy Pop, and Intense Rock. Each profile produced different recommendations that generally matched the intended preferences.

For the Chill Lofi profile, the system recommended songs like *Midnight Coding* and *Library Rain*, which fit the relaxed and low-energy vibe. For the High Energy Pop profile, songs like *Sunrise City* and *Gym Hero* appeared at the top because they matched both the genre and high energy levels. For the Intense Rock profile, *Storm Runner* consistently ranked highest due to its strong match in genre, mood, and high energy.

One interesting observation was that songs like *Gym Hero* appeared in multiple profiles. This is because it has high energy and strong numerical similarity to different user preferences, even when the genre or mood is not a perfect match.

When I removed the mood feature in an experiment, the rankings changed noticeably. Songs that matched the emotional vibe dropped, while songs with similar numerical features (like energy and tempo) moved up. This showed that mood is an important factor in making recommendations feel accurate.

Overall, the system behaved as expected, but it also showed that different features (like genre vs. numerical similarity) can strongly influence the final recommendations.

---

## 8. Future Work  

In the future, the model could be improved by using a larger and more diverse dataset. It could also include user listening history to make recommendations more personalized.

Another improvement would be to balance diversity so the system does not always recommend very similar songs. Adding features like lyrics or artist similarity could also improve accuracy.
---

## 9. Personal Reflection  

## 9. Personal Reflection

My biggest learning moment in this project was understanding how simple rules can turn into meaningful recommendations. By assigning points to features like genre and energy, I was able to create a system that produced results that actually felt reasonable.

Using AI tools helped me move faster, especially when implementing functions and debugging errors. However, I still had to carefully check the logic to make sure the scoring matched my intended design, since small mistakes could change the recommendations a lot.

One thing that surprised me was how even a simple algorithm could feel realistic. Even without complex machine learning, the system was able to capture the “vibe” of music fairly well using just a few features.

If I were to extend this project, I would use a larger dataset and include user listening history to make the recommendations more personalized. I would also try to improve diversity so the system does not always recommend very similar songs.