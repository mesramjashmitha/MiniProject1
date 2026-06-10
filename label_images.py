import os
import shutil
import cv2

# ==============================
# PATH (your folder)
# ==============================
base_path = r"C:\Users\Jashmitha\OneDrive\Desktop\MiniProject1\DatasetAcne\Acne"

# ==============================
# CREATE FOLDERS
# ==============================
folders = ["blackheads", "whiteheads", "papules", "pustules", "cysts"]

for f in folders:
    os.makedirs(os.path.join(base_path, f), exist_ok=True)

# ==============================
# COLLECT ALL IMAGES (inside all folders)
# ==============================
image_paths = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_paths.append(os.path.join(root, file))

print("Total images found:", len(image_paths))

# ==============================
# LABEL IMAGES
# ==============================
for img_path in image_paths:

    img_name = os.path.basename(img_path)

    # skip if already inside category folder
    if any(folder in img_path for folder in folders):
        continue

    img = cv2.imread(img_path)
    if img is None:
        continue

    cv2.imshow("Image", img)

    print("\nImage:", img_name)
    print("Press key:")
    print("1 = blackheads")
    print("2 = whiteheads")
    print("3 = papules")
    print("4 = pustules")
    print("5 = cysts")
    print("Any other key = skip")

    # 🔥 KEY FIX (important)
    key = cv2.waitKey(0) & 0xFF

    # ==============================
    # MOVE IMAGE BASED ON KEY
    # ==============================
    if key == ord('1'):
        dest = os.path.join(base_path, "blackheads", img_name)
        shutil.move(img_path, dest)
        print("✅ moved to blackheads")

    elif key == ord('2'):
        dest = os.path.join(base_path, "whiteheads", img_name)
        shutil.move(img_path, dest)
        print("✅ moved to whiteheads")

    elif key == ord('3'):
        dest = os.path.join(base_path, "papules", img_name)
        shutil.move(img_path, dest)
        print("✅ moved to papules")

    elif key == ord('4'):
        dest = os.path.join(base_path, "pustules", img_name)
        shutil.move(img_path, dest)
        print("✅ moved to pustules")

    elif key == ord('5'):
        dest = os.path.join(base_path, "cysts", img_name)
        shutil.move(img_path, dest)
        print("✅ moved to cysts")

    else:
        print("⏭ skipped")

    # close image before next
    cv2.destroyAllWindows()

print("🎉 DONE LABELING!")