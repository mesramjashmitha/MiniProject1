print("\n========== PATIENT INFORMATION ==========\n")

name = input("Enter Patient Name: ")
age = input("Enter Age: ")

print("\n========== SYMPTOM QUESTIONS ==========\n")

score = 0

score += int(input("Acne duration (1= <1week, 2=1-4weeks, 3=>1month): ")) * 5
score += int(input("Pain level (1-10): ")) * 2
score += int(input("Swelling (1=None, 2=Mild, 3=Severe): ")) * 6
score += int(input("Pus formation (1=No, 2=Sometimes, 3=Frequent): ")) * 7

medicine_used = input("Used acne medicine before? (yes/no): ").lower()

if medicine_used == "yes":
    score += 10

print("\n========== IMAGE INPUT ==========\n")

input_path = input("Enter input image path: ")

if not os.path.exists(input_path):
    print("❌ Image not found")
    exit()

matched_image_path = find_most_similar(input_path, dataset_path)

print("\n✅ Matched Image:", matched_image_path)

# Show images
import matplotlib.pyplot as plt
import cv2

input_img = cv2.cvtColor(cv2.imread(input_path), cv2.COLOR_BGR2RGB)
matched_img = cv2.cvtColor(cv2.imread(matched_image_path), cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(input_img)
plt.title("Input Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(matched_img)
plt.title("Matched Dataset Image")
plt.axis("off")

plt.show()

# Result Section

predicted_class = os.path.basename(os.path.dirname(matched_image_path))

medicine_map = {
    "whitehead": ["Salicylic Acid 2%", "Adapalene 0.1%"],
    "blackhead": ["Salicylic Acid Cleanser", "Retinoid Cream"],
    "papule": ["Benzoyl Peroxide 2.5%", "Topical antibiotic gel"],
    "pustule": ["Benzoyl Peroxide 5%", "Clindamycin gel"],
    "cyst": ["Consult dermatologist immediately"],
    "scar": ["Vitamin C serum", "Sunscreen SPF50"],
    "pigmentation": ["Niacinamide serum", "Sunscreen SPF50"]
}

print("\n========== FINAL RESULT ==========\n")

print("Name:", name)
print("Age:", age)
print("Predicted Acne Type:", predicted_class)
print("Symptom Score:", score)

print("\n💊 Suggested Skincare:")

if predicted_class in medicine_map:
    for med in medicine_map[predicted_class]:
        print("-", med)

print("\n⚠️ Disclaimer: This is only a supportive guidance system.")