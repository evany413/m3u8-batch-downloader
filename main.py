import csv
import os
import re
from yt_dlp import YoutubeDL

def sanitize_filename(filename):
    # Replace or remove characters that are not allowed in filenames
    # Windows: \ / : * ? " < > |
    # Unix-like: / 
    # Common replacements
    filename = re.sub(r'[\\/*?:"<>|]', '_', filename)  # Replace problematic characters with underscore
    filename = filename.strip()  # Remove leading/trailing whitespace
    filename = re.sub(r'\s+', ' ', filename)  # Replace multiple spaces with single space
    
    # Remove any existing file extension to avoid double extensions
    filename = os.path.splitext(filename)[0]
    return filename

def download_videos(csv_file):
    # Create downloads directory if it doesn't exist
    downloads_dir = "downloads"
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download best quality
        'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),
    }

    # Read CSV file and download videos
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL)
        for row in reader:
            if len(row) >= 2:
                m3u8_url = row[0].strip()
                video_name = sanitize_filename(row[1])
                
                # Configure output template for this specific video
                ydl_opts['outtmpl'] = os.path.join(downloads_dir, f'{video_name}.%(ext)s')
                
                try:
                    with YoutubeDL(ydl_opts) as ydl:
                        print(f"Downloading: {video_name}")
                        ydl.download([m3u8_url])
                        print(f"Successfully downloaded: {video_name}")
                except Exception as e:
                    print(f"Error downloading {video_name}: {str(e)}")


if __name__ == "__main__":
    download_videos("list.csv")
