from datetime import datetime
from flask import request, jsonify
import os
import numpy as np
from tensorflow.keras.preprocessing import image

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data safely
        name = request.form.get("name", "")
        age = request.form.get("age", "")
        gender = request.form.get("gender", "")
        date = request.form.get("date") or datetime.now().strftime("%Y-%m-%d")

        file = request.files.get("image")

        # Validate image
        if file is None or file.filename == "":
            return jsonify({"error": "No image uploaded"}), 400

        # Create static folder if not exists
        os.makedirs("static", exist_ok=True)

        # Save image
        filename = f"{int(datetime.now().timestamp())}.jpg"
        path = os.path.join("static", filename)
        file.save(path)

        # Preprocess image
        img = image.load_img(path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediction
        pred = model.predict(img_array)[0]

        # Top class only
        index = int(np.argmax(pred))

        # ✅ FIX 1: Ensure proper string
        disease = str(classes[index]).strip()

        confidence = float(pred[index] * 100)

        # Get level
        level = get_level(confidence)

        # ✅ FIX 2: Debug print (helps you confirm issue)
        print("Predicted:", disease)
        print("Available:", list(data.keys()))

        # ✅ FIX 3: Prevent crash if mismatch
        if disease not in data:
            return jsonify({
                "error": f"Invalid class predicted: {disease}"
            }), 500

        if level not in data[disease]:
            return jsonify({
                "error": f"Invalid level: {level}"
            }), 500

        result_data = data[disease][level]

        # Final response
        final = {
            "name": name,
            "age": age,
            "gender": gender,
            "date": date,

            "disease": disease,
            "confidence": round(confidence, 2),
            "level": level,
            "reason": result_data.get("reason", ""),
            "medicine": result_data.get("medicine", ""),
            "advice": result_data.get("advice", ""),
            "image": f"/static/{filename}"
        }

        # ✅ FIX 4: Safe save_record call
        try:
            save_record(final)
        except Exception as e:
            print("Save error:", e)

        return jsonify(final), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500