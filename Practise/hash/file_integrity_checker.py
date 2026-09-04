import os
import json
import hashlib

FOLDER = "Practise"
BASELINE_FILE = "baseline.json"


def calculate_hash(filepath):
    try:
        sha256 = hashlib.sha256()

        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None

    except PermissionError:
        print(f"[ERROR] Permission denied: {filepath}")
        return None

    except OSError as e:
        print(f"[ERROR] Could not read {filepath}: {e}")
        return None


def create_baseline():
    try:
        if not os.path.exists(FOLDER):
            print(f"[ERROR] Folder '{FOLDER}' does not exist.")
            return

        baseline = {}

        for root, dirs, files in os.walk(FOLDER):
            for file in files:
                filepath = os.path.join(root, file)

                file_hash = calculate_hash(filepath)

                if file_hash is not None:
                    baseline[filepath] = file_hash

        with open(BASELINE_FILE, "w") as f:
            json.dump(baseline, f, indent=4)

        print("[+] Baseline created successfully!")
        print(f"[+] Files stored: {len(baseline)}")

    except PermissionError:
        print("[ERROR] Permission denied while creating baseline.")

    except OSError as e:
        print(f"[ERROR] Operating system error: {e}")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")


def check_integrity():
    try:
        # Check whether baseline exists
        if not os.path.exists(BASELINE_FILE):
            print("[ERROR] baseline.json does not exist.")
            print("[INFO] Create a baseline first.")
            return

        # Read baseline
        with open(BASELINE_FILE, "r") as f:
            baseline = json.load(f)

        current_files = {}

        # Scan current files
        if not os.path.exists(FOLDER):
            print(f"[ERROR] Folder '{FOLDER}' does not exist.")
            return

        for root, dirs, files in os.walk(FOLDER):
            for file in files:
                filepath = os.path.join(root, file)

                file_hash = calculate_hash(filepath)

                if file_hash is not None:
                    current_files[filepath] = file_hash

        # Check modified, deleted and unchanged files
        for filepath, old_hash in baseline.items():

            if filepath not in current_files:
                print(f"[DELETED]  {filepath}")

            elif current_files[filepath] != old_hash:
                print(f"[MODIFIED] {filepath}")

            else:
                print(f"[OK]       {filepath}")

        # Check new files
        for filepath in current_files:

            if filepath not in baseline:
                print(f"[NEW]      {filepath}")

    except json.JSONDecodeError:
        print("[ERROR] baseline.json contains invalid JSON.")

    except PermissionError:
        print("[ERROR] Permission denied while reading files.")

    except OSError as e:
        print(f"[ERROR] Operating system error: {e}")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")


# -------------------------
# Main Program
# -------------------------

try:
    while True:

        print("\n===== File Integrity Checker =====")
        print("1. Create Baseline")
        print("2. Check Integrity")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_baseline()

        elif choice == "2":
            check_integrity()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")

except KeyboardInterrupt:
    print("\n[INFO] Program interrupted by user.")

except Exception as e:
    print(f"[ERROR] Unexpected program error: {e}")