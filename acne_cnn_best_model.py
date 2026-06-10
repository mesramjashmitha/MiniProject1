import os
import base64
import io
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# ==========================================
# MODEL PATH (CHANGE IF NEEDED)
# ==========================================
MODEL_PATH = r"acne_cnn_best_model.h5"

if not os.path.exists(MODEL_PATH):
    print("❌ Model file not found!")
    print("Make sure acne_cnn_best_model.h5 is in same folder.")
    exit()

print("✅ Loading AI Model...")
model = load_model(MODEL_PATH)

input_height = model.input_shape[1]
input_width = model.input_shape[2]

print("✅ Model Loaded Successfully!")


# ==========================================
# IMAGE PROCESSING
# ==========================================
def preprocess_image(img):
    img = img.resize((input_width, input_height))
    img_array = np.array(img) / 255.0

    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)

    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def get_image():
    print("\nPaste image path OR base64 string:")
    data = input(">> ").strip()

    try:
        if os.path.exists(data):
            img = Image.open(data).convert("RGB")
        else:
            if data.startswith("data:image"):
                data = data.split(",")[1]
            img = Image.open(io.BytesIO(base64.b64decode(data))).convert("RGB")

        return preprocess_image(img)

    except Exception as e:
        print("❌ Invalid image input.")
        print(e)
        exit()


# ==========================================
# QUESTIONNAIRE
# ==========================================
def ask_questions():

    score = 0

    print("\n===== ACNE SYMPTOM ANALYSIS =====")

    print("\n1. Skin type?")
    print("1) Oily")
    print("2) Dry")
    print("3) Combination")
    skin = int(input("Select: "))

    print("\n2. Duration of acne?")
    print("1) <1 week")
    print("2) 1-4 weeks")
    print("3) >1 month")
    score += int(input("Select: ")) * 5

    print("\n3. Pain level (1-10):")
    score += int(input("Enter: ")) * 2

    print("\n4. Type of acne?")
    print("1) Whiteheads/Blackheads")
    print("2) Red inflamed pimples")
    print("3) Large painful cysts")
    score += int(input("Select: ")) * 8

    print("\n5. Swelling level?")
    print("1) None")
    print("2) Mild")
    print("3) Severe")
    score += int(input("Select: ")) * 6

    print("\n6. Pus discharge?")
    print("1) No")
    print("2) Sometimes")
    print("3) Frequently")
    score += int(input("Select: ")) * 7

    print("\n7. Scars or dark spots?")
    print("1) No")
    print("2) Dark spots")
    print("3) Deep scars")
    score += int(input("Select: ")) * 6

    print("\n8. Acne spreading?")
    print("1) No")
    print("2) Yes")
    score += int(input("Select: ")) * 6

    print("\n9. Have you used any acne medicine? (Type name or 'no')")
    medicine = input("Answer: ").lower().strip()

    if medicine != "no":
        score += 10

    return score, skin, medicine


# ==========================================
# SEVERITY LOGIC
# ==========================================
def determine_severity(score):
    if score < 50:
        return "MILD"
    elif score < 100:
        return "MODERATE"
    else:
        return "SEVERE"


# ==========================================
# FINAL REPORT
# ==========================================
def generate_report(severity, skin, medicine):

    print("\n========================================")
    print("        AI DERMATOLOGY REPORT")
    print("========================================")

    print(f"\nDetected Severity Level: {severity}")

    # Severity Explanation
    if severity == "MILD":
        print("Superficial acne detected.")
    elif severity == "MODERATE":
        print("Inflammatory acne with possible scarring risk.")
    else:
        print("Severe inflammatory or cystic acne.")

    # Medicine logic
    if medicine != "no":

        print("\n----- Previous Medicine Review -----")
        print(f"You used: {medicine}")

        if "benzoyl" in medicine:
            print("Benzoyl peroxide kills acne bacteria.")
            print("Consider combining with adapalene for better results.")

        elif "adapalene" in medicine:
            print("Adapalene unclogs pores.")
            print("Combine with benzoyl peroxide if needed.")

        elif "clindamycin" in medicine:
            print("Topical antibiotic reduces bacteria.")
            print("Avoid using alone long-term.")

        elif "doxycycline" in medicine:
            print("Oral antibiotic for moderate-severe acne.")
            print("Needs medical supervision.")

        elif "isotretinoin" in medicine:
            print("Strong systemic retinoid.")
            print("Must be monitored by dermatologist.")

        else:
            print("Unknown medication detected.")

        print("\nRecommended Next Step:")
        print("Consider combination therapy or escalation.")

    else:

        print("\n----- Suggested Treatment -----")

        if severity == "MILD":
            print("• Benzoyl Peroxide 2.5% (Morning)")
            print("• Salicylic Acid Face Wash")

        elif severity == "MODERATE":
            print("• Adapalene + Benzoyl Peroxide")
            print("• Consider Oral Doxycycline if needed")

        else:
            print("• Oral Doxycycline")
            print("• Consider Isotretinoin (Doctor supervision)")

    print("\n----- Skincare Advice -----")

    if skin == 1:
        print("Use oil-free moisturizer and gentle cleanser.")
    elif skin == 2:
        print("Use hydrating cleanser and barrier cream.")
    else:
        print("Balance oil control and hydration.")

    print("\n⚠ Educational AI guidance only.")


# ==========================================
# MAIN PROGRAM
# ==========================================
print("\n===== SMART ACNE DIAGNOSIS SYSTEM =====")

image = get_image()

# Image prediction (no printing result)
prediction = model.predict(image)

score, skin, medicine = ask_questions()

severity = determine_severity(score)

generate_report(severity, skin, medicine)