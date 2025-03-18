import requests
import time
import json

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

ACCESS_TOKEN = config["access_token"]  # Your token from config.json
GROUP_IDS = config["group_ids"]       # List of group IDs
UPDATE_INTERVAL = config["update_interval"]  # Time interval (in seconds)

# Function to update group name
def update_group_name(group_id, new_name):
    url = f"https://graph.facebook.com/{group_id}"
    data = {
        "access_token": ACCESS_TOKEN,
        "name": new_name
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"Group {group_id} updated successfully: {response.json()}")
        else:
            print(f"Failed to update group {group_id}: {response.json()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main loop to update groups periodically
def main():
    while True:
        for group_id in GROUP_IDS:
            new_name = f"Updated Group {int(time.time())}"  # Example: Dynamic name
            update_group_name(group_id, new_name)
        print(f"Waiting for {UPDATE_INTERVAL} seconds before the next update...")
        time.sleep(UPDATE_INTERVAL)

# Start the script
if __name__ == "__main__":
    main()
