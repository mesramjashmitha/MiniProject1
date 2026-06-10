import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# ================= LOAD MODEL =================
model = tf.keras.models.load_model("acne_model.keras")

# ================= LOAD CLASS NAMES =================
class_names = np.load("class_names.npy", allow_pickle=True)

# ================= LOAD IMAGE =================
img_path = "test.jpg"   # 👈 put your test image path here

img = image.load_img(img_path, target_size=(224,224))
img = image.img_to_array(img)
img = img / 255.0
img = np.expand_dims(img, axis=0)

# ================= PREDICT =================
pred = model.predict(img)

# ================= OUTPUT =================
predicted_class = class_names[np.argmax(pred)]
confidence = np.max(pred)

print("Prediction:", predicted_class)
print("Confidence:", confidence)