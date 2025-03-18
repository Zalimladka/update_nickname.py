import json
import time
import schedule
from fbchat import Client
from fbchat.models import ThreadType

# Load AppState
with open('appstate.json', 'r') as f:
    appstate = json.load(f)

client = Client.from_session(appstate)

def change_nickname():
    group_id = "1234567890"  # Group ID
    client.changeNickname("Cool Nickname", group_id, thread_type=ThreadType.GROUP)
    print("✅ Nickname changed!")

def change_group_name():
    group_id = "1234567890"  # Group ID
    client.changeThreadTitle("Awesome Group Name", group_id)
    print("✅ Group name changed!")

# Schedule tasks
schedule.every(5).minutes.do(change_nickname)
schedule.every(5).minutes.do(change_group_name)

while True:
    schedule.run_pending()
    time.sleep(1)
