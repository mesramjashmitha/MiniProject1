from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask import send_from_directory
import numpy as np
from datetime import datetime
import json
import webbrowser
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)
CORS(app)

# ================= LOAD MODEL =================
model = load_model("acne_model.keras")

classes = np.load("class_names.npy", allow_pickle=True)
def calculate_accuracy(pred_array):
    """
    Simple accuracy = highest probability (confidence)
    """
    return float(np.max(pred_array) * 100)
# ================= LEVEL FUNCTION =================
def get_level(conf):
    if conf <= 10:
        return "Very Low"
    elif conf <= 20:
        return "Low"
    elif conf <= 40:
        return "Medium"
    elif conf <= 60:
        return "High"
    else:
        return "Severe"

# ================= DATA =================
data = {

# ================= BLACKHEADS =================
"blackheads": {

"Very Low": {
"reason": "There is a very mild buildup of oil and dead skin in the pores, which has just started to oxidize slightly.",
"medicine": [
"Use a gentle foaming face cleanser twice daily",
"Apply aloe vera gel for soothing effect",
"Use light oil-free moisturizer",
"Clean face regularly with mild soap",
"Avoid heavy makeup products"
],
"advice": "Maintain basic hygiene and wash your face regularly to prevent buildup."
},

"Low": {
"reason": "Oil and dirt have started clogging the pores, leading to early-stage blackhead formation.",
"medicine": [
"Use salicylic acid face wash",
"Apply niacinamide serum for oil control",
"Use a clay mask once a week",
"Apply toner to tighten pores",
"Use light moisturizer"
],
"advice": "Avoid oily skincare products and keep pores clean."
},

"Medium": {
"reason": "Moderate accumulation of oil and dead skin is blocking pores, forming visible blackheads.",
"medicine": [
"Use salicylic acid cleanser daily",
"Apply charcoal mask twice weekly",
"Use adapalene gel at night",
"Apply niacinamide serum",
"Use oil-free moisturizer"
],
"advice": "Exfoliate regularly and maintain a strict skincare routine."
},

"High": {
"reason": "Heavy oil buildup is causing deep pore blockage and prominent blackheads.",
"medicine": [
"Apply adapalene cream",
"Use salicylic acid gel",
"Apply charcoal face mask",
"Use retinoid cream",
"Apply oil control serum"
],
"advice": "Avoid touching your face and follow a strict cleansing routine."
},

"Severe": {
"reason": "Severe and long-term blockage of pores has resulted in persistent blackheads.",
"medicine": [
"Use strong retinoid creams",
"Go for chemical peel treatment",
"Use dermatologist-grade salicylic therapy",
"Apply deep cleansing masks",
"Consult a dermatologist"
],
"advice": "Seek professional treatment for effective removal."
}
},

# ================= WHITEHEADS =================
"whiteheads": {

"Very Low": {
"reason": "Very small closed pores are trapping minimal oil beneath the skin.",
"medicine": [
"Use gentle cleanser",
"Apply aloe vera gel",
"Use light moisturizer",
"Clean face regularly",
"Avoid thick creams"
],
"advice": "Keep your skin clean and avoid pore-clogging products."
},

"Low": {
"reason": "Closed pores are trapping oil and bacteria, forming early whiteheads.",
"medicine": [
"Use salicylic acid gel",
"Apply niacinamide serum",
"Use light moisturizer",
"Wash face twice daily",
"Use toner"
],
"advice": "Avoid heavy skincare products and maintain hygiene."
},

"Medium": {
"reason": "Oil and bacteria buildup inside pores is causing visible whiteheads.",
"medicine": [
"Apply benzoyl peroxide cream",
"Use salicylic acid",
"Apply retinoid cream",
"Use niacinamide serum",
"Use oil-free moisturizer"
],
"advice": "Use non-comedogenic skincare products only."
},

"High": {
"reason": "Significant pore blockage has resulted in multiple whiteheads across the skin.",
"medicine": [
"Apply retinoid cream regularly",
"Use benzoyl peroxide",
"Use salicylic acid cleanser",
"Apply niacinamide serum",
"Use oil-free moisturizer"
],
"advice": "Do not squeeze pimples to avoid worsening."
},

"Severe": {
"reason": "Severe blockage and bacterial growth are causing persistent whiteheads.",
"medicine": [
"Consult dermatologist",
"Use oral medications",
"Apply strong retinoids",
"Use antibiotics",
"Follow medical therapy"
],
"advice": "Immediate medical attention is recommended."
}
},

# ================= PAPULES =================
"papules": {

"Very Low": {
"reason": "Minor inflammation has started due to slight irritation in the skin.",
"medicine": [
"Apply aloe vera gel",
"Use gentle cleanser",
"Apply niacinamide serum",
"Use moisturizer",
"Use soothing toner"
],
"advice": "Avoid touching your face frequently."
},

"Low": {
"reason": "Mild irritation has caused small red bumps on the skin.",
"medicine": [
"Use niacinamide serum",
"Apply azelaic acid",
"Use mild cream",
"Use cleanser",
"Apply moisturizer"
],
"advice": "Reduce irritation and avoid harsh products."
},

"Medium": {
"reason": "Inflammation of clogged pores is forming noticeable red papules.",
"medicine": [
"Apply clindamycin gel",
"Use niacinamide serum",
"Apply azelaic acid",
"Use anti-inflammatory cream",
"Apply moisturizer"
],
"advice": "Do not squeeze pimples to prevent infection."
},

"High": {
"reason": "Strong inflammation due to bacterial growth is causing painful papules.",
"medicine": [
"Use topical antibiotics",
"Apply anti-inflammatory creams",
"Use clindamycin",
"Apply niacinamide",
"Use moisturizer"
],
"advice": "Follow proper medication and avoid touching skin."
},

"Severe": {
"reason": "Severe inflammatory acne is affecting deeper layers of skin.",
"medicine": [
"Use oral antibiotics",
"Apply strong creams",
"Consult dermatologist",
"Use medical therapy",
"Follow advanced treatment"
],
"advice": "Seek immediate medical help."
}
},

# ================= PUSTULES =================
"pustules": {

"Very Low": {
"reason": "Minor bacterial infection has caused small pus-filled pimples.",
"medicine": [
"Use gentle cleanser",
"Apply aloe vera",
"Use moisturizer",
"Apply mild cream",
"Keep skin clean"
],
"advice": "Maintain hygiene."
},

"Low": {
"reason": "Small infection is causing visible pus formation in pimples.",
"medicine": [
"Use benzoyl peroxide",
"Apply antibacterial cream",
"Use cleanser",
"Apply moisturizer",
"Wash face regularly"
],
"advice": "Avoid touching pimples."
},

"Medium": {
"reason": "Bacterial infection is spreading in clogged pores causing pustules.",
"medicine": [
"Use topical antibiotics",
"Apply benzoyl peroxide",
"Use sulfur cream",
"Apply cleanser",
"Use moisturizer"
],
"advice": "Do not pop pimples."
},

"High": {
"reason": "Severe infection is causing multiple pustules on the skin.",
"medicine": [
"Use antibiotic cream",
"Apply benzoyl peroxide",
"Use sulfur ointment",
"Use cleanser",
"Apply moisturizer"
],
"advice": "Maintain strict hygiene routine."
},

"Severe": {
"reason": "Deep infection is causing severe pus-filled acne.",
"medicine": [
"Use oral antibiotics",
"Consult doctor",
"Use strong medication",
"Follow medical therapy",
"Seek dermatologist care"
],
"advice": "Immediate medical consultation is required."
}
},

# ================= CYSTS =================
"cysts": {

"Very Low": {
"reason": "Early stage of deep acne is forming beneath the skin.",
"medicine": [
"Use mild cream",
"Apply cleanser",
"Use moisturizer",
"Apply aloe vera",
"Maintain hygiene"
],
"advice": "Monitor condition regularly."
},

"Low": {
"reason": "Deep inflammation is starting under the skin surface.",
"medicine": [
"Use anti-inflammatory cream",
"Apply cleanser",
"Use moisturizer",
"Apply gel",
"Maintain skincare"
],
"advice": "Avoid pressure on affected area."
},

"Medium": {
"reason": "Deep infection is forming painful acne under the skin.",
"medicine": [
"Use antibiotic cream",
"Apply strong gel",
"Use cleanser",
"Apply moisturizer",
"Follow routine"
],
"advice": "Use medical creams consistently."
},

"High": {
"reason": "Severe cyst formation is occurring under deeper skin layers.",
"medicine": [
"Use oral antibiotics",
"Take steroid injections",
"Use strong creams",
"Follow medical therapy",
"Consult doctor"
],
"advice": "Seek medical help immediately."
},

"Severe": {
"reason": "Very deep and severe infection is causing painful cystic acne.",
"medicine": [
"Use isotretinoin (doctor prescribed)",
"Consult dermatologist immediately",
"Take steroid injections",
"Follow medical therapy",
"Use advanced treatment"
],
"advice": "Immediate dermatologist consultation is necessary."
}
}

}
# ================= SAVE HISTORY =================
def save_record(data_record):
    file = "records.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            records = json.load(f)
    else:
        records = []

    records.append(data_record)

    with open(file, "w") as f:
        json.dump(records, f, indent=4)

# ================= STATIC FILES =================
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# ================= HOME =================
@app.route("/")
def home():
    return "✅ Acne Diagnosis API Running"

# ================= PREDICT =================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files.get("image")

        if not file:
            return jsonify({"error": "No image uploaded"})

        if not os.path.exists("static"):
            os.makedirs("static")

        path = "static/upload.jpg"
        file.save(path)

        # User data from form
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")

        # Preprocess image
        img = image.load_img(path, target_size=(224,224))
        img_array = image.img_to_array(img)/255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediction
        pred = model.predict(img_array)[0]

        index = np.argmax(pred)
        disease = classes[index]
        confidence = float(pred[index] * 100)

        level = get_level(confidence)

        result_data = data[disease][level]
        current_date = datetime.now().strftime("%Y-%m-%d")
        print("Prediction array:", pred)
        print("Predicted index:", index)
        print("Predicted class:", classes[index])
        # Final response
        response = {
            "name": name,
            "age": age,
            "gender": gender,
            "disease": disease,
            "confidence": round(confidence, 2),
            "level": level,
          
            "reason": result_data["reason"],
            "medicine": result_data["medicine"],
            "advice": result_data["advice"],
            "image": "/static/upload.jpg"
        }


        # ✅ SAVE HISTORY
        save_record(response)

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})

# ================= HISTORY API =================
@app.route("/history/<name>")
def get_history(name):

    if not os.path.exists("records.json"):
        return jsonify([])

    with open("records.json", "r") as f:
        records = json.load(f)

    search_name = str(name).strip().lower()

    user_records = []

    for r in records:
        stored_name = str(r.get("name", "")).strip().lower()

        if stored_name == search_name:
            user_records.append(r)

    return jsonify(user_records)



# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)

