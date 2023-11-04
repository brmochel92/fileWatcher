# Movies Folder Watcher for Plex Update

This Python script uses the `watchdog` library to monitor a specified directory (`X:/Movies-4k` in this case) for any changes. Upon detecting a modification (file change), it triggers a partial scan in Plex to update the movies library.

## Overview

This utility allows Plex users to automatically update their movie library when changes are detected in the specified directory. The updates are initiated by watching for file modifications and calling the Plex API to refresh the library.

## Features

- Monitors the specified directory for file modifications.
- Utilizes a cooldown mechanism to prevent frequent updates.
- Triggers a Plex library partial scan upon detecting changes in the movie directory.

## Usage

### Prerequisites
- Python 3.x installed
- `watchdog` library installed (`pip install watchdog`)

### Instructions
1. Modify the `path` variable in the script to specify the directory to be monitored.
2. Ensure the Plex URL, Plex token, and library section ID are set correctly in the `trigger_plex_update()` function.
3. Run the Python script.

## Script Details

The Python script uses the `watchdog` library to track modifications within the defined directory. It includes a cooldown timer to prevent too frequent updates in Plex. When a modification (file change) occurs, it triggers a partial scan in the specified Plex library section.

## Additional Notes

Feel free to adjust the cooldown duration, path, and other parameters to fit your preferences.

**Note:** Ensure the Plex URL, token, and library section ID are correct for your setup.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Pull requests and suggestions for improvement are welcomed!
