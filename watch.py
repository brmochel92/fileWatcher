from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import time

file_last_modified = {}  # Store last modified time for each file

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            current_time = time.time()
            if file_path not in file_last_modified or (current_time - file_last_modified[file_path]) >= 60:
                file_last_modified[file_path] = current_time
                print(f"File modified: {file_path}")
                trigger_plex_update(file_path)

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            print(f"File created: {file_path}")
            trigger_plex_update(file_path)

def trigger_plex_update(file_path):
    print(f"Triggering Plex update for: {file_path}")
    plex_url = 'PLEX-URL-HERE' # REPLACE WITH YOUR OWN PLEX URL
    plex_token = 'PLEX-TOKEN-HERE' # REPLACE WITH YOUR OWN PLEX TOKEN, OBTAINED BY VIEWING XML ON ANY MEDIA FILE ON YOUR PLEX SERVER (URL AT END SHOULD BE PLEX-TOKEN)
    library_section_id = 'PLEX-LIBRARY=SECTION-HERE' # REPLACE WITH THE PLEX LIBRARY ID # (http://[plex_url_here]/library/sections/?X-Plex-Token=plex-token-here)

    headers = {'X-Plex-Token': plex_token}
    params = {'type': '13'}  # '13' triggers a partial scan in Plex
    url = f"{plex_url}/library/sections/{library_section_id}/refresh"

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print("Plex library partial scan triggered.")
    else:
        print(f"Failed to trigger Plex library scan: {response.status_code}")

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path="PATH-OF-CONTENT", recursive=True) # path is where you are storing your movies or tv shows or whatever you are monitoring for file changes
    observer.start()

    try:
        while True:
            print("Watching for changes...")
            time.sleep(10)  # To avoid high CPU usage during the loop - may not need this if you have a decent server
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
