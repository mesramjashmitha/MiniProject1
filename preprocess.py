import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ================= PATH =================
dataset_path = r"C:\Users\Jashmitha\OneDrive\Desktop\MiniProject1\DatasetAcne\Acne"

print("Checking path...")

if os.path.exists(dataset_path):
    print("✅ Dataset path found!")
else:
    print("❌ Dataset path NOT found!")

# ================= PARAMETERS =================
img_size = 224
batch_size = 32

# ================= DATA GENERATOR =================
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# ================= TRAIN DATA =================
train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True,
    seed=42
)

# ================= VALIDATION DATA =================
val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    shuffle=False,
    seed=42
)

# ================= PRINT INFO =================
print("\n📂 Class Indices:", train_data.class_indices)
print("📊 Number of Classes:", train_data.num_classes)

print("\n📸 Training Images:", train_data.samples)
print("🧪 Validation Images:", val_data.samples)

# ================= OPTIONAL: CHECK FILE NAMES =================
print("\n🔍 Sample Training Files:")
print(train_data.filenames[:5])

print("\n🔍 Sample Validation Files:")
print(val_data.filenames[:5])