import os  # import the os module for interacting with the file system
import requests  # import the requests module for making HTTP requests
import ctypes  # import the ctypes module for displaying a message box
import winsound  # import the winsound module for playing a sound

# Replace this with the path to your text file
text_file = r"C:\Users\yogev\PycharmProjects\video_downloader\links.txt"

# Read the links from the text file and split them into a list
with open(text_file) as f:
    links = f.read().splitlines()

# Create the directory if it doesn't exist
directory = r"D:\OneDrive - ac.sce.ac.il\שולחן העבודה"
subdirectory = os.path.join(directory, "Name of the course- Compilation lectures")
if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)

# Download each video file from the links and save them to the directory
for i, link in enumerate(links):
    print(f"Processing link {i + 1} of {len(links)}: {link}")
    response = requests.get(link)  # Send a GET request to the link
    print(f"Response status code: {response.status_code}")  # Print the status code of the response
    filename = os.path.join(subdirectory, f"{i + 1}.mp4")  # Create a filename for the video file
    with open(filename, "wb") as f:  # Open the file in binary mode and write the response content to it
        f.write(response.content)

# Change the sound file path to the desired file
sound_file = r"C:\Windows\Media\tada.wav"

# Set the system volume to the maximum value (1)
# You can adjust the volume to a lower value if desired (0 till 1)
volume = int(0.99 * 0xFFFF)
ctypes.windll.winmm.waveOutSetVolume(0, volume, volume)

# Play the sound asynchronously and increase the volume
winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

# Display a message box to indicate that all files have been downloaded
ctypes.windll.user32.MessageBoxW(0, "All files have been downloaded!", "Download Complete", 0)
