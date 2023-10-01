from flask import Flask, request, jsonify, send_from_directory
import random
import os
from flask_cors import CORS  # Import CORS from flask_cors
from flask_compress import Compress


app = Flask(__name__)
 # Add this line to enable CORS for your app
CORS(app, resources={r"/api/*": {"origins": "https://foota.onrender.com"}})
compress = Compress(app)
# Connect to MongoDB using the MONGO_URI environment variable
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
        "name": "Kylian Mbappe",
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
    {
    "name": "N'Golo Kante",
    "facts": [
        "He is known for his exceptional work rate and ability to cover a large portion of the pitch during matches.",
        "He won back-to-back Premier League titles with Leicester City and Chelsea, earning the nickname 'The Engine.'",
        "Despite his success, he maintains a humble and low-profile lifestyle off the field.",
        "He was a crucial part of the French national team's 2018 FIFA World Cup victory."
    ]
},
{
    "name": "Kevin De Bruyne",
    "facts": [
        "He is regarded as one of the best midfielders in the world due to his passing accuracy and playmaking abilities.",
        "He initially struggled to establish himself in the Premier League but later became a key player for Manchester City.",
        "He is known for his versatility, being able to play in multiple midfield positions.",
        "He has a passion for music and once composed a song for his former club, Genk."
    ]
},
{
    "name": "Virgil van Dijk",
    "facts": [
        "He is considered one of the best defenders in the world, known for his composure and leadership on the field.",
        "He played a crucial role in Liverpool's UEFA Champions League victory in 2019.",
        "He is also known for his aerial ability and threat during set-pieces.",
        "He started his career as a midfielder before transitioning to a central defender."
    ]
},
{
    "name": "Luka Modrić",
    "facts": [
        "He won the Ballon d'Or in 2018, breaking the Cristiano Ronaldo-Lionel Messi dominance.",
        "He played a pivotal role in Croatia's journey to the 2018 FIFA World Cup final.",
        "He is known for his exceptional vision and passing accuracy in midfield.",
        "He started his professional career at Dinamo Zagreb before moving to top European clubs."
    ]
},
{
    "name": "Joshua Kimmich",
    "facts": [
        "He is known for his versatility, being able to play as a right-back, central midfielder, or defensive midfielder.",
        "He is a key player for Bayern Munich and played a crucial role in their UEFA Champions League victories.",
        "He is known for his incredible work rate and ability to cover large distances during matches.",
        "He started his career at RB Leipzig before joining Bayern Munich."
    ]
},
{
    "name": "Karim Benzema",
    "facts": [
        "He is known for his clinical finishing and ability to score crucial goals for Real Madrid.",
        "He has won numerous La Liga and UEFA Champions League titles with Real Madrid.",
        "He faced controversy in his international career but made a return to the French national team.",
        "He is often praised for his link-up play and ability to assist teammates."
    ]
},
{
    "name": "Sadio Mane",
    "facts": [
        "He is known for his incredible speed and dribbling abilities, making him a threat on the wing.",
        "He has played a crucial role in Liverpool's Premier League and UEFA Champions League successes.",
        "He comes from a humble background in Senegal and has invested in building schools and a hospital in his hometown.",
        "He won the Premier League Golden Boot for the 2018-2019 season."
    ]
},
{
    "name": "Toni Kroos",
    "facts": [
        "He is renowned for his exceptional passing ability and vision on the field.",
        "He has won multiple UEFA Champions League titles with Real Madrid and the FIFA World Cup with Germany.",
        "He began his career at Bayern Munich and later moved to Real Madrid.",
        "He is known for his calm and composed style of play."
    ]
},
{
    "name": "Romelu Lukaku",
    "facts": [
        "He is known for his physical strength and goal-scoring prowess as a striker.",
        "He has played for top clubs like Chelsea, Manchester United, and Inter Milan.",
        "He is of Congolese descent and represents Belgium at the international level.",
        "He is passionate about music and released a rap song in 2018."
    ]
},
{
    "name": "Gareth Bale",
    "facts": [
        "He is known for his blistering pace and ability to score spectacular goals.",
        "He achieved great success with Real Madrid, winning multiple UEFA Champions League titles.",
        "He has represented Wales in international competitions and is their all-time leading goal scorer.",
        "He has a strong interest in golf and has competed in charity golf events."
    ]
},
{
    "name": "Marcinho",
    "facts": [
        "He is a Brazilian attacking midfielder known for his creativity and dribbling skills.",
        "He has played for top European clubs like Paris Saint-Germain and Chelsea.",
        "He is famous for his no-look passes, which add flair to his style of play.",
        "He is part of the Brazilian national team and has represented them in international competitions."
    ]
},
{
    "name": "Son Heung-min",
    "facts": [
        "He is a South Korean forward known for his versatility and goal-scoring ability.",
        "He has been a key player for Tottenham Hotspur in the English Premier League.",
        "He is also known for his sportsmanship and fair play on the field.",
        "He represented South Korea in the 2018 FIFA World Cup."
    ]
},
{
    "name": "Luka Modric",
    "facts": [
        "He is a Croatian midfielder known for his exceptional passing and playmaking abilities.",
        "He won the Golden Ball as the best player of the 2018 FIFA World Cup.",
        "He has played a vital role in Real Madrid's success, winning multiple UEFA Champions League titles.",
        "He grew up during the Croatian War of Independence and faced many challenges during his early years."
    ]
},
{
    "name": "N'Golo Kante",
    "facts": [
        "He is a French midfielder known for his incredible work rate and ball-winning abilities.",
        "He played a key role in France's victory at the 2018 FIFA World Cup.",
        "He started his professional career at smaller clubs in France before joining Leicester City and then Chelsea.",
        "He is known for his humble and down-to-earth personality."
    ]
},
{
    "name": "Mohamed Salah",
    "facts": [
        "He is an Egyptian forward known for his speed and goal-scoring prowess.",
        "He has been a star player for Liverpool in the English Premier League.",
        "He is deeply committed to charity work and has funded hospitals and schools in Egypt.",
        "He is often referred to as the 'Egyptian King' by his fans."
    ]
},
{
    "name": "Andrés Iniesta",
    "facts": [
        "He is a Spanish midfielder known for his precise passing and vision.",
        "He played a crucial role in Spain's triumph at the 2010 FIFA World Cup.",
        "He spent the majority of his club career at Barcelona, winning numerous titles with the club.",
        "He is considered one of the greatest midfielders in the history of football."
    ]
},
{
    "name": "Eden Hazard",
    "facts": [
        "He is a Belgian forward known for his dribbling skills and creativity.",
        "He joined Real Madrid from Chelsea as one of the most expensive transfers in history.",
        "He comes from a football-loving family, with his younger brothers also pursuing professional football careers.",
        "He has a sweet tooth and is nicknamed 'The Chocolatier' by his fans."
    ]
},

{
    "name": "Manuel Neuer",
    "facts": [
        "He is a German goalkeeper recognized for his exceptional shot-stopping abilities and ball-playing skills.",
        "He was instrumental in Germany's victory at the 2014 FIFA World Cup.",
        "He is known for his 'sweeper-keeper' style of play, often leaving his goal to act as an extra defender.",
        "He has won numerous domestic and international titles with Bayern Munich and the German national team."
    ]
},
{
    "name": "Zlatan Ibrahimović",
    "facts": [
        "A charismatic and talented striker known for his incredible goal-scoring ability.",
        "He has played for top clubs across Europe, including Barcelona, PSG, and Manchester United.",
        "He is known for his witty and confident personality in interviews.",
        "He has won league titles in multiple countries."
    ]
},{
    "name": "Paul Pogba",
    "facts": [
        "Known for his skillful dribbling and ability to control the midfield.",
        "He returned to Manchester United from Juventus for a then-world record transfer fee.",
        "He has won the FIFA World Cup with the French national team.",
        "He is known for his unique hairstyles and fashion sense."
    ]
},
{
    "name": "Edinson Cavani",
    "facts": [
        "A prolific Uruguayan striker with a strong aerial presence and goal-scoring ability.",
        "He has played for top clubs like Napoli, Paris Saint-Germain, and Manchester United.",
        "He is known for his tireless work ethic and commitment on the field.",
        "He is one of Uruguay's all-time leading goal scorers."
    ]
},
{
    "name": "Hakim Ziyech",
    "facts": [
        "A creative Moroccan midfielder known for his dribbling skills and playmaking abilities.",
        "He joined Chelsea in the Premier League and quickly became a key player for the club.",
        "He is known for his precise set-piece deliveries and ability to unlock defenses.",
        "He has represented Morocco in international competitions."
    ]
},
{
    "name": "Thomas Muller",
    "facts": [
        "A versatile German forward known for his intelligence and positioning on the field.",
        "He has won numerous Bundesliga titles and the FIFA World Cup with the German national team.",
        "He is known for his unique playing style and ability to contribute both as a scorer and playmaker.",
        "He has a great sense of humor and is often seen joking with teammates."
    ]
},
{
    "name": "Bruno Fernandes",
    "facts": [
        "A Portuguese midfielder known for his vision, passing ability, and goal-scoring prowess.",
        "He joined Manchester United in the Premier League and quickly became a fan favorite.",
        "He is known for his free-kick taking skills and his leadership on the pitch.",
        "He has represented Portugal in international competitions."
    ]
},
{
    "name": "Erling Haaland",
    "facts": [
        "A young Norwegian striker known for his incredible speed and goal-scoring record.",
        "He made a name for himself at RB Salzburg before moving to Borussia Dortmund.",
        "He is known for his humility and dedication to his craft.",
        "He has a reputation for scoring in almost every game he plays."
    ]
},
{
    "name": "Keylor Navas",
    "facts": [
        "A Costa Rican goalkeeper known for his exceptional reflexes and shot-stopping ability.",
        "He gained recognition during his time at Real Madrid, where he won multiple Champions League titles.",
        "He is known for his humble personality and dedication to his position.",
        "He is considered one of the best goalkeepers in the world."
    ]
},
{
    "name": "Raheem Sterling",
    "facts": [
        "An English forward known for his dribbling skills, pace, and goal-scoring ability.",
        "He has been a key player for Manchester City and the English national team.",
        "He is known for his activism and efforts to combat racism in football.",
        "He is one of the top English talents in world football."
    ]
},
{
    "name": "Sadio Mané",
    "facts": [
        "A Senegalese forward known for his pace, dribbling, and goal-scoring ability.",
        "He has been a key player for Liverpool and played a crucial role in their Premier League and Champions League victories.",
        "He is known for his philanthropic efforts, including funding the construction of a school in Senegal.",
        "He is considered one of the best African players in the world."
    ]
},
{
    "name": "Sergio Aguero",
    "facts": [
        "An Argentine striker known for his goal-scoring ability and agility.",
        "He spent several successful seasons at Manchester City in the Premier League.",
        "He holds the record for the most hat-tricks in Premier League history.",
        "He has represented the Argentine national team in multiple World Cups."
    ]
},
{
    "name": "Thiago Alcantara",
    "facts": [
        "A Spanish midfielder known for his passing accuracy and technique.",
        "He has played for top clubs like Barcelona, Bayern Munich, and Liverpool.",
        "He is known for his ability to control the tempo of the game from midfield.",
        "He has won numerous domestic and international titles."
    ]
},
{
    "name": "Karim Benzema",
    "facts": [
        "A French striker known for his technical skills and goal-scoring ability.",
        "He has had a long and successful career at Real Madrid in La Liga.",
        "He is known for his link-up play and assists in addition to scoring goals.",
        "He has won numerous titles with Real Madrid."
    ]
},
{
    "name": "Frenkie de Jong",
    "facts": [
        "A Dutch midfielder known for his dribbling and versatility in midfield.",
        "He gained recognition at Ajax before moving to Barcelona in La Liga.",
        "He is known for his ability to control the ball in tight spaces.",
        "He has represented the Netherlands in international competitions."
    ]
},
{
    "name": "Marquinhos",
    "facts": [
        "A Brazilian defender known for his versatility and leadership on the field.",
        "He has been a consistent performer for Paris Saint-Germain (PSG) in Ligue 1.",
        "He is known for his ability to play as a center-back or defensive midfielder.",
        "He has won numerous domestic titles with PSG."
    ]
},
{
    "name": "Kai Havertz",
    "facts": [
        "A young German midfielder known for his technical skills and versatility.",
        "He plays for Chelsea in the Premier League and has a promising future.",
        "He is known for his composure in front of goal and ability to create chances.",
        "He has already represented Germany in international competitions."
    ]
},
{
    "name": "Jadon Sancho",
    "facts": [
        "An English winger known for his dribbling skills and pace.",
        "He transferred from Borussia Dortmund to Manchester United in the Premier League.",
        "He is known for his versatility in attack and creative playmaking.",
        "He has earned caps for the England national team."
    ]
},
{
    "name": "Luis Suarez",
    "facts": [
        "A Uruguayan striker known for his goal-scoring instincts and tenacity.",
        "He has played for clubs like Barcelona and now plays for Atlético Madrid in La Liga.",
        "He is known for his passion on the field and his fierce competitiveness.",
        "He has represented Uruguay in multiple World Cups."
    ]
},
{
    "name": "Lautaro Martínez",
    "facts": [
        "An Argentine forward known for his goal-scoring ability and work ethic.",
        "He plays for Inter Milan in Serie A and the Argentina national team.",
        "He is known for his partnership with Lionel Messi in the national team.",
        "He has represented Argentina in Copa America and World Cup tournaments."
    ]
},
{
    "name": "Joao Cancelo",
    "facts": [
        "A Portuguese right-back known for his defensive skills and attacking contributions.",
        "He plays for Manchester City in the Premier League and the Portugal national team.",
        "He is known for his ability to deliver accurate crosses and set up goals.",
        "He has won domestic league titles and the UEFA European Championship with Portugal."
    ]
},
{
    "name": "Paulo Dybala",
    "facts": [
        "An Argentine forward known for his dribbling skills and creativity.",
        "He plays for Juventus in Serie A and the Argentina national team.",
        "He is known for his ability to score from free-kicks and long-range shots.",
        "He has won domestic league titles and played alongside some of the best players in the world."
    ]
},
{
    "name": "Leon Goretzka",
    "facts": [
        "A German midfielder known for his box-to-box playing style and physicality.",
        "He plays for Bayern Munich in the Bundesliga and the Germany national team.",
        "He is known for his goal-scoring ability from midfield and strong presence in both attack and defense.",
        "He has won domestic league titles and represented Germany in international competitions."
    ]
},
{
    "name": "Christian Pulisic",
    "facts": [
        "An American winger known for his speed and dribbling skills.",
        "He plays for Chelsea in the Premier League and the United States national team.",
        "He is known for breaking barriers as a top American talent in European football.",
        "He has a bright future ahead and is regarded as a rising star."
    ]
},
{
    "name": "Riyad Mahrez",
    "facts": [
        "An Algerian winger known for his pace and ability to cut inside and score goals.",
        "He plays for Manchester City in the Premier League and the Algeria national team.",
        "He is known for his dribbling and set-piece expertise.",
        "He played a key role in Leicester City's historic Premier League title win."
    ]
},
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
        "message": "New game started! Click on the <strong> Get Fun Facts Button</strong> to get started.",
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
