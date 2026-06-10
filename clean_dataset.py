import os
import shutil
import cv2

source_dir = r"C:\Users\Jashmitha\OneDrive\Desktop\MiniProject1\DatasetAcne\Acne"
dest_dir = r"C:\Users\Jashmitha\OneDrive\Desktop\MiniProject1\Clean_Data_5"

classes = ["blackheads", "whiteheads", "papules", "pustules", "cysts"]

# create folders
for c in classes:
    os.makedirs(os.path.join(dest_dir, c), exist_ok=True)

print("\nKEYS:")
print("0 → blackheads | 1 → whiteheads | 2 → papules | 3 → pustules | 4 → cysts")
print("s → skip | d → delete | q → quit\n")

# ---------------- SAFE LOOP ----------------
for folder in os.listdir(source_dir):

    folder_path = os.path.join(source_dir, folder)

    # ❌ skip if not folder (VERY IMPORTANT)
    if not os.path.isdir(folder_path):
        continue

    for img_name in os.listdir(folder_path):

        img_path = os.path.join(folder_path, img_name)

        # ❌ skip non-images
        if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img = cv2.imread(img_path)

        if img is None:
            continue

        img = cv2.resize(img, (400, 400))

        cv2.imshow("Classify Image", img)

        key = cv2.waitKey(0) & 0xFF

        label = None

        if key == ord('0'):
            label = "blackheads"
        elif key == ord('1'):
            label = "whiteheads"
        elif key == ord('2'):
            label = "papules"
        elif key == ord('3'):
            label = "pustules"
        elif key == ord('4'):
            label = "cysts"

        elif key == ord('s'):
            print("⏭ Skipped")
            cv2.destroyAllWindows()
            continue

        elif key == ord('d'):
            os.remove(img_path)
            print("🗑 Deleted")
            cv2.destroyAllWindows()
            continue

        elif key == ord('q'):
            print("🚪 Exiting...")
            cv2.destroyAllWindows()
            exit()

        else:
            print("❌ Invalid key")
            cv2.destroyAllWindows()
            continue

        if label:
            shutil.copy(
                img_path,
                os.path.join(dest_dir, label, img_name)
            )
            print(f"✔ Moved to {label}")

        cv2.destroyAllWindows()

print("\n✅ DATASET CLEANED SUCCESSFULLY!")