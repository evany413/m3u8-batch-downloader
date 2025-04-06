# m3u8 Batch Downloader

A Python script that batch downloads video courses from m3u8 links using yt-dlp. It reads video URLs and names from a CSV file, sanitizes filenames for cross-platform compatibility, and organizes downloads in a structured manner.

## Features

- Batch download videos from m3u8 links
- Read video information from CSV file
- Automatic filename sanitization for cross-platform compatibility
- Simple and easy to use
- Progress tracking for downloads

## Requirements

- Python 3.6 or higher
- yt-dlp package

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/m3u8-batch-downloader.git
cd m3u8-batch-downloader
```

2. Install the required package:
```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your CSV file (`list.csv`) with the following format:
```csv
"m3u8_url","video_name"
"https://example.com/video1.m3u8","Video Name 1"
"https://example.com/video2.m3u8","Video Name 2"
```

2. Run the script:
```bash
python main.py
```

The script will:
- Create a `downloads` directory if it doesn't exist
- Download each video from the m3u8 links
- Save them with the names specified in the CSV
- Show progress and any errors that occur

## CSV Format

The CSV file should contain two columns:
1. First column: m3u8 URL
2. Second column: Desired video name

Example:
```csv
"https://example.com/video1.m3u8","單元 1 - 程式環境架設"
"https://example.com/video2.m3u8","單元 2 - 程式基本教學"
```

## Notes

- The script automatically sanitizes filenames to be compatible with all operating systems
- Videos are downloaded to a `downloads` directory
- The script uses yt-dlp to handle the actual downloading
- All fields in the CSV should be quoted to handle special characters

## License

This project is licensed under the MIT License - see the LICENSE file for details. 