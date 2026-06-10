import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model( r"C:\Users\Jashmitha\OneDrive\Desktop\MiniProject1\acne_model.keras")

# Image path (change this when testing)
img_path = input("Enter image path: ")

img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Prediction
prediction = model.predict(img_array)

classes = ["acne", "no_acne"]

print("Prediction:", classes[np.argmax(prediction)])