from flask import Flask, request, jsonify, send_from_directory
import random
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your app


# Define a list of football players and their fun facts
football_players = [
    {
        "name": "Cristiano Ronaldo",
        "facts": [
            "He is known for his incredible work ethic and reportedly sleeps in hyperbaric chambers to aid recovery.",
            "He once worked as a ball boy at his local club Sporting CP before making it as a professional footballer.",
            "He is the first player to score 100 international goals.",
            "He has his own line of fragrances and clothing."
        ]
    },
    {
        "name": "Lionel Messi",
        "facts": [
            "He's first contract was written on a napkin when he was just 13 years old.",
            "He is a philanthropist and has funded the construction of healthcare centers in his hometown, Rosario.",
            "He has won the Ballon d'Or award a record number of times.",
            "He has a passion for collecting jerseys from other footballers and has a substantial collection."
        ]
    },
    {
        "name": "Neymar Jr.",
        "facts": [
            "He once appeared in a cameo role in the popular Netflix series 'Money Heist.'",
            "He played poker professionally and won a poker tournament in 2015.",
            "He has a fondness for tattoos and has several inked on his body.",
            "He donated a significant sum to a children's hospital in Brazil."
        ]
    },
    {
        "name": "Kylian Mbappé",
        "facts": [
            "He is a huge fan of anime and the Dragon Ball series.",
            "He pledged to donate his entire World Cup earnings to charity.",
            "He's speed is often compared to that of Olympic sprinters.",
            "He became the youngest French player to score in a World Cup."
        ]
    },
    {
        "name": "Sergio Ramos",
        "facts": [
            "He has a famous habit of scoring crucial goals in stoppage time.",
            "He has a collection of over 40 tattoos on his body.",
            "He is known for his intense workout routines, including boxing.",
            "He holds the record for most red cards received in La Liga history."
        ]
    },
    {
        "name": "Robert Lewandowski",
        "facts": [
            "He is an accomplished pianist and can play the piano.",
            "He scored five goals in nine minutes during a Bundesliga match in 2015.",
            "He holds a black belt in karate.",
            "He and his wife, Anna, have a line of clothing and accessories."
        ]
    },
    {
        "name": "Mohamed Salah",
        "facts": [
            "He has a strong interest in table tennis and is a skilled player.",
            "He starred in an Egyptian movie called 'Mawhub.'",
            "He is a prominent advocate for women's rights in the Middle East.",
            "He is known for his trademark goal celebration, the 'Egyptian King' pose."
        ]
    },
    {
        "name": "Antoine Griezmann",
        "facts": [
            "He is an avid gamer and has his own esports organization.",
            "He often celebrates goals with dances from popular video games.",
            "He is a fan of the NBA and is friends with several basketball players.",
            "He has a collection of superhero-themed cleats."
        ]
    },
    {
        "name": "Eden Hazard",
        "facts": [
            "He is known for his love of chocolate and has been nicknamed 'The Chocolatier.'",
            "He has three brothers who are also professional footballers.",
            "He has appeared in a Belgian comedy film.",
            "He enjoys playing basketball in his free time."
        ]
    },
    {
        "name": "Harry Kane",
        "facts": [
            "He has a degree in sports science and has aspirations to become a professional golfer after retiring from football.",
            "He is the first English player to win the Golden Boot at a World Cup since 1986.",
            "He is known for his humorous social media presence.",
            "He is a big fan of American football and supports the New England Patriots."
        ]
    },
    # Add more players and facts here
]


# Shuffle the list of football players
random.shuffle(football_players)

# Current game state variables
current_player = None
guesses_remaining = 0

# Function to start a new game
def start_new_game():
    global current_player, guesses_remaining
    if not football_players:
        return jsonify({"message": "No players available for a new game."}), 404

    current_player = football_players.pop()
    guesses_remaining = 4

    response_data = {
        "message": "New game started!",
        "player_name": current_player["name"],
        "guesses_remaining": guesses_remaining,
    }
    return jsonify(response_data)

# Function to get fun facts
def get_fun_facts():
    if not current_player:
        return jsonify({"message": "No active game. Start a new game to get facts."}), 400

    facts = current_player["facts"]
    return jsonify({"facts": facts})

# Function to make a guess
def make_guess():
    global guesses_remaining
    if not current_player:
        return jsonify({"message": "No active game. Start a new game to make a guess."}), 400

    data = request.get_json()
    user_guess = data.get("user_guess", "").strip().lower()
    player_name = current_player["name"].lower()

    if not user_guess:
        return jsonify({"message": "Invalid input."}), 400

    if any(part in user_guess for part in player_name.split()):
        return jsonify({"message": "Correct guess!", "player_name": current_player["name"]}), 200
    else:
        guesses_remaining -= 1
        if guesses_remaining > 0:
            return jsonify({"message": f"Incorrect guess! You have {guesses_remaining} guesses remaining."}), 200
        else:
            return jsonify({"message": f"Sorry, you're out of guesses. The correct answer is {current_player['name']}."}), 200

# API routes
@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

@app.route('/api/game/start', methods=['POST'])
def start_game():
    return start_new_game()

@app.route('/api/game/facts', methods=['GET'])
def get_player_facts():
    return get_fun_facts()

@app.route('/api/game/guess', methods=['POST'])
def guess_player_name():
    return make_guess()

if __name__ == '__main__':
    app.run(app.run(host="127.0.0.1", port=5000, debug=True))
