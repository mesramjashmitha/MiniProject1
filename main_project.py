import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.models import load_model

# ================= MODEL LOAD =================

MODEL_PATH = "acne_cnn_best_model.h5"

model = load_model(MODEL_PATH)

input_height = model.input_shape[1]
input_width = model.input_shape[2]

classes = ["Mild Acne", "Moderate Acne", "Severe Acne"]

# ================= PREPROCESS =================

def preprocess_image(path):

    img = Image.open(path).convert("RGB")
    img = img.resize((input_width, input_height))

    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    return arr, img

# ================= REPRESENTATIVE IMAGE =================

def get_dataset_image(label):

    mapping = {
        "Mild Acne": "DatasetAcne/mild/sample_mild.jpg",
        "Moderate Acne": "DatasetAcne/moderate/sample_moderate.jpg",
        "Severe Acne": "DatasetAcne/severe/sample_severe.jpg"
    }

    return mapping[label]

# ================= DISPLAY =================

def show_output(user_img, dataset_img, label):

    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.imshow(user_img)
    plt.title("User Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(dataset_img)
    plt.title("Matched Dataset Image")
    plt.axis("off")

    plt.suptitle("Prediction Result : " + label)

    plt.show()

# ================= MAIN =================

print("\nSMART ACNE DIAGNOSIS SYSTEM")

name = input("Enter Name: ")

image_path = input("Enter image path: ")

if not os.path.exists(image_path):
    print("Image not found!")
    exit()

# Prediction
image_array, user_img = preprocess_image(image_path)

pred = model.predict(image_array)
pred_class = np.argmax(pred)

label = classes[pred_class]

# Dataset matched image
dataset_path = get_dataset_image(label)

dataset_img = Image.open(dataset_path).convert("RGB")
dataset_img = dataset_img.resize((224,224))

print("\n===== AI REPORT =====")
print("User Name :", name)
print("Prediction Result :", label)

# Show output images
show_output(user_img, dataset_img, label)

print("\nSystem Finished Successfully")