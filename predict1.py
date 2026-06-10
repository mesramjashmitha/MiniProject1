import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ================= LOAD MODEL =================
print("🔄 Loading model...")
model = load_model("acne_model.h5")
print("✅ Model loaded successfully!\n")

# ================= CLASSES =================
classes = ['blackheads', 'whiteheads', 'papules', 'pustules', 'cysts']

# ================= INPUT =================
img_path = input("Enter image path: ")

# ================= CHECK FILE =================
if not os.path.exists(img_path):
    print("❌ ERROR: Image not found!")
    print("👉 Make sure the image is inside the folder or give correct path")
    exit()

# ================= IMAGE PREPROCESS =================
# 🔥 IMPORTANT: Use 224x224 (your model expects this)
img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# ================= PREDICT =================
prediction = model.predict(img_array)

index = np.argmax(prediction)
confidence = prediction[0][index] * 100

# ================= OUTPUT =================
print("\n========== RESULT ==========")
print("Predicted Disease:", classes[index])
print("Confidence:", round(confidence, 2), "%")

# ================= SUGGESTIONS =================
suggestions = {
    "blackheads": "Use salicylic acid face wash",
    "whiteheads": "Use benzoyl peroxide cream",
    "papules": "Use mild acne creams",
    "pustules": "Use antibiotic cream (consult doctor)",
    "cysts": "Consult dermatologist immediately"
}

print("Suggestion:", suggestions[classes[index]])

print("\n✔ Done Successfully!")