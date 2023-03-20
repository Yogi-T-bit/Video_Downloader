# Video Downloader
This script downloads a list of videos from specified links and saves them to a directory on your computer.

## Introduction
I created this project as a way to improve my productivity and save time when I need to download multiple videos from different sources. I also wanted to learn more about Python and how to work with requests module.

This script allows you to download videos from any website that provides direct links to video files. 
It also supports downloading multiple videos at once by reading links from a text file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## Installation
To use this script, you need Python 3.x installed on your computer. You also need requests module which you can install using pip:

```bash
pip install requests
```

To run the script, clone this repository or download it as zip file:

```bash
git clone https://github.com/Yogi-T-bit/video-downloader.git
```

Then navigate to the directory where you downloaded the script:

```bash
cd video-downloader
```

## Usage
Before running the script, you need to prepare a text file with links of videos you want to download. Each link should be on a separate line.

For example:

```
https://example.com/video1.mp4
https://example.com/video2.mp4
https://example.com/video3.mp4
https://example.com/video4.mp4
```

Save this file in any location on your computer.

Next, open the script in any text editor and update two variables: `text_file` and `directory`.

The `text_file` variable should contain the path to your text file with links.

The `directory` variable should contain the path to the directory where you want to save the downloaded videos.

For example:

```python
text_file = "C:/Users/YourName/Desktop/links.txt"
directory = "C:/Users/YourName/Desktop/Videos"
```

Make sure both paths are valid and exist on your computer.

Finally, run the script using Python:

```bash
python video_downloader.py
```

The script will download each video from the links in your text file and save them in the specified directory with their original names.

When all files have been downloaded, it will display a message box saying "All files have been downloaded!" and play a sound.

![img.png](message_box.png)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contributing
I welcome any contributions or suggestions for improvement
