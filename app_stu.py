from flask import  Flask, jsonify

app = Flask(__name__)

justice_people = \
[{"superhero": "Aquaman", "real_name":	"Arthur Curry"},
{"superhero": "Batman", "real_name":		"Bruce Wayne"},
{"superhero": "Cyborg", "real_name":		"Victor Stone"},
{"superhero": "Flash", "real_name":		"Barry Allen"},
{"superhero": "Green Lantern", "real_name":		"Hal Jordan"},
{"superhero": "Superman", "real_name":		"Kal-El/Clark Kent"},
{"superhero": "Wonder Woman", "real_name":		"Princess Diana/Diana Prince"}]

@app.route("/")
def home():
    return "Welcome to my internal server"

@app.route("/about")
def about():
    return "About us..."

@app.route("/contact")
def contact():
    return "Please contact our team..."

@app.route("/api/v1.0/justice-leage")
def justice():
    return jsonify(justice_people)

@app.route("/api/v1.0/justice-leage/<real_name>")
def justice_leage_character(real_name):
    canonicalized = real_name.replace(" ", "").lower()
    for hero in justice_people:
        canonicalized_hero = hero["real_name"].replace(" ", "").lower()

        if canonicalized_hero == canonicalized:
            return jsonify(hero)

    return jsonify({"error": f"Hero real name {real_name} not found"}, 404)


if __name__ == "__main__" : 
    app.run(debug=True)