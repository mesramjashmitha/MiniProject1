# ===============================
# SMART ACNE DIAGNOSIS SYSTEM
# ===============================

print("===== SMART ACNE DIAGNOSIS SYSTEM =====")

# -------------------------------
# QUESTIONS SECTION
# -------------------------------

risk_score = 0

print("\n1. What is your skin type?")
print("1) Oily")
print("2) Dry")
print("3) Combination")
skin_type = int(input("Select: "))
risk_score += skin_type * 5


print("\n2. How long have you had acne?")
print("1) Few days")
print("2) Few weeks")
print("3) Months")
duration = int(input("Select: "))
risk_score += duration * 10


print("\n3. Pain or irritation level?")
print("1) Mild")
print("2) Moderate")
print("3) Severe")
pain = int(input("Select: "))
risk_score += pain * 15


print("\n4. Do you have redness/swelling?")
print("1) No")
print("2) Little")
print("3) Severe")
redness = int(input("Select: "))
risk_score += redness * 10


print("\n5. Are pimples painful to touch?")
print("1) No")
print("2) Sometimes")
print("3) Yes")
touch = int(input("Select: "))
risk_score += touch * 10


print("\n6. Do you use oily cosmetics?")
print("1) No")
print("2) Sometimes")
print("3) Yes")
cosmetics = int(input("Select: "))
risk_score += cosmetics * 8


print("\n7. Do you consume junk/oily food frequently?")
print("1) No")
print("2) Sometimes")
print("3) Yes")
food = int(input("Select: "))
risk_score += food * 8


print("\n8. Do you have stress/sleep issues?")
print("1) No")
print("2) Sometimes")
print("3) Yes")
stress = int(input("Select: "))
risk_score += stress * 7


print("\n9. Have you used acne medicine before?")
print("1) No")
print("2) Yes (worked)")
print("3) Yes (not worked)")
medicine_history = int(input("Select: "))
risk_score += medicine_history * 5


print("\n10. Do you see pus-filled or cyst-like acne?")
print("1) No")
print("2) Few")
print("3) Many")
cyst = int(input("Select: "))
risk_score += cyst * 20


# -------------------------------
# SEVERITY DETECTION
# -------------------------------

print("\nTotal Risk Score:", risk_score)

if risk_score < 50:
    severity = "MILD"
elif risk_score < 100:
    severity = "MODERATE"
else:
    severity = "SEVERE"

print("\n===== FINAL DIAGNOSIS =====")
print("Severity:", severity, "ACNE")


# -------------------------------
# MEDICINE SUGGESTION FUNCTION
# -------------------------------

def suggest_medicine(severity, skin_type):

    print("\n===== MEDICINE SUGGESTION =====")

    if severity == "MILD":
        print("• Benzoyl Peroxide 2.5% gel (Morning)")
        print("• Adapalene 0.1% gel (Night)")
        print("• Salicylic Acid face wash")

    elif severity == "MODERATE":
        print("• Benzoyl Peroxide 5% gel")
        print("• Adapalene + Clindamycin gel")
        print("• Doxycycline tablet (if inflammation present)")

    elif severity == "SEVERE":
        print("• Adapalene + Clindamycin gel")
        print("• Benzoyl Peroxide 5% gel")
        print("• Oral Doxycycline")
        print("• Isotretinoin (Doctor supervision only)")

    print("\n===== SKIN CARE ADVICE =====")

    if skin_type == 1:
        print("• Oily Skin → Use oil-free moisturizer")
    elif skin_type == 2:
        print("• Dry Skin → Use moisturizer before medication")
    elif skin_type == 3:
        print("• Combination Skin → Apply only on affected area")

    print("\n===== LIFESTYLE RECOMMENDATIONS =====")
    print("• Drink 2-3 liters water daily")
    print("• Avoid junk food")
    print("• Do not squeeze pimples")
    print("• Change pillow cover twice a week")

    print("\n⚠ AI-based suggestion. For academic project use only.")


# CALL FUNCTION
suggest_medicine(severity, skin_type)