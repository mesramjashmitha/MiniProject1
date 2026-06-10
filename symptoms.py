from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "Symptom Analyzer API is running!"
# ================= QUESTIONS =================
questions = [
    {
        "q": "How often do you get pimples?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very frequently"]
    },
    {
        "q": "Do you have oily skin?",
        "options": ["Not at all", "Slightly", "Moderate", "Oily", "Very oily"]
    },
    {
        "q": "Do you notice blackheads?",
        "options": ["None", "Very few", "Occasionally", "Many", "Severe"]
    },
    {
        "q": "Do you have painful pimples?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very often"]
    },
    {
        "q": "Do you get whiteheads?",
        "options": ["None", "Few", "Sometimes", "Many", "Severe"]
    },
    {
        "q": "Do pimples leave marks?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    {
        "q": "How is your skin texture?",
        "options": ["Very smooth", "Smooth", "Normal", "Rough", "Very rough"]
    },
    {
        "q": "Do you experience itching on skin?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very often"]
    },
    {
        "q": "Do pimples spread quickly?",
        "options": ["Never", "Slow", "Moderate", "Fast", "Very fast"]
    },
    {
        "q": "Do you touch your face frequently?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very often"]
    },
    {
        "q": "How often do you wash your face?",
        "options": ["3+ times/day", "2 times/day", "Once/day", "Occasionally", "Rarely"]
    },
    {
        "q": "Do you use skincare products?",
        "options": ["Regularly", "Often", "Sometimes", "Rarely", "Never"]
    },
    {
        "q": "Do you eat oily/junk food often?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Daily"]
    },
    {
        "q": "Do you experience stress?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very high"]
    },
    {
        "q": "Do you get pimples on cheeks?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very often"]
    },
    {
        "q": "Do you get pimples on forehead?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Very often"]
    },
    {
        "q": "Do you have red inflamed pimples?",
        "options": ["None", "Few", "Sometimes", "Many", "Severe"]
    },
    {
        "q": "Do you pop pimples?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    },
    {
        "q": "Do you sleep less than 6 hours?",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Daily"]
    },
    {
        "q": "Overall skin condition?",
        "options": ["Excellent", "Good", "Average", "Bad", "Very bad"]
    }
]

# ================= SCORE SYSTEM =================
def analyze_score(score):
    if score <= 25:
        return {
            "level": "Mild",
            "advice": [
                "Keep your skin clean with a gentle face wash twice daily",
                "Drink more water and maintain healthy diet",
                "Avoid touching your face frequently",
                "Use non-comedogenic skincare products"
            ]
        }

    elif score <= 55:
        return {
            "level": "Moderate",
            "advice": [
                "Use gentle cleanser twice daily",
                "Consider salicylic acid or benzoyl peroxide based face wash (OTC)",
                "Avoid oily/junk food frequently",
                "Do not pop pimples (prevents scars)"
            ]
        }

    else:
        return {
            "level": "Severe",
            "advice": [
                "You should consult a dermatologist",
                "Avoid self-medication or harsh products",
                "Maintain strict skin hygiene routine",
                "Reduce stress and improve sleep quality"
            ]
        }

# ================= API =================
@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    answers = data.get("answers", [])

    score = 0
    for a in answers:
        score += int(a)  # each option gives 0-4 points

    result = analyze_score(score)

    return jsonify({
        "total_score": score,
        "result": result
    })

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)