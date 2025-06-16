from flask import Flask, render_template
import random
import os

app = Flask(__name__)

WORDS = [
    "Buffalo Nickel", "Digging a Hole", "Big John’s Place", "Dead Crow", "Fill a Void",
    "Different Kind of Feeling", "Good Mood Guy", "Final Cut", "Out of Tune", "Orange Julius",
    "Same Old Dream", "I’m Going To Die", "I’m Lost", "No One Else", "Little Alien",
    "I Saw The Light", "New Hell", "Somewhere", "Another Sad Song", "Dead Man’s Drums",
    "Satellite Radio DJ", "Italian Cream", "Sometimes Sometime", "Happy Birthday JFK"
]

@app.route("/")
def bingo():
    selected_words = random.sample(WORDS, 24)
    card = [selected_words[i:i+5] for i in range(0, 24, 5)]
    card.insert(2, card[2][:2] + ["FREE"] + card[2][2:])
    return render_template("bingo.html", card=card)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
