from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import time

file_ids = {}  # Dictionary to store file IDs and last modification time
cooldown_duration = 300  # 300 seconds = 5 minutes

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            file_id = event.src_path  # Use the file path as an ID

            current_time = time.time()
            if file_id not in file_ids or current_time - file_ids[file_id] >= cooldown_duration:
                file_ids[file_id] = current_time
                print(f"File modified: {event.src_path}")
                trigger_plex_update()  # Call the function to trigger Plex update

def trigger_plex_update():
    plex_url = 'URL-HERE'
    plex_token = 'PLEX-TOKEN-HERE'
    library_section_id = 'PLEX-LIBRARY-SECTION-HERE'

    headers = {'X-Plex-Token': plex_token}
    params = {'type': '13'}  # '13' supposedly triggers a partial scan in Plex but I haven't got this working correctly and it does a full scan
    url = f"{plex_url}/library/sections/{library_section_id}/refresh"

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print("Plex library partial scan triggered.")
    else:
        print(f"Failed to trigger Plex library scan: {response.status_code}")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="X:/Movies-4k", recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
