import kagglehub
import os
import shutil

print("Downloading GTD dataset from Kaggle...")
path = kagglehub.dataset_download("START-UMD/gtd")
print(f"Dataset downloaded to: {path}")

# Find the CSV file in the downloaded path
csv_file = None
for file in os.listdir(path):
    if file.endswith(".csv"):
        csv_file = os.path.join(path, file)
        break

if csv_file:
    os.makedirs("data", exist_ok=True)
    dest_path = "data/globalterrorism.csv"
    print(f"Copying {csv_file} to {dest_path}")
    shutil.copy(csv_file, dest_path)
    print("Done! The real Kaggle data is now ready.")
else:
    print("Error: Could not find the CSV file in the downloaded dataset.")
