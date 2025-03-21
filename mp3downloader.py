import os
import subprocess

def print_ascii_art():
    print("""
  __  __ ____ _____   ____                      _                 _
 |  \/  |  _ \___ /  |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __
 | |\/| | |_) ||_ \  | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |  | |  __/___) | | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
 |_|  |_|_|  |____/  |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
 Powered by: yt-dlp
 Can be found on: https://www.github.com/yt-dlp/yt-dlp
    """)

def update_yt_dlp():
    try:
        subprocess.run(["yt-dlp", "-U"], check=True)
    except subprocess.CalledProcessError:
        print("\nWarning: Failed to update yt-dlp. Continuing with the current version.\n")

def list_formats(url):
    print("\nListing available formats...\n")
    try:
        subprocess.run(["yt-dlp", "--list-formats", url], check=True)
    except subprocess.CalledProcessError:
        print("\nFailed to retrieve format list. Check the URL and try again.\n")

def download_mp3(url, save_path):
    output_template = os.path.join(save_path, "%(title)s.%(ext)s")
    command = [
        "yt-dlp", "-f", "bestaudio",
        "--extract-audio", "--audio-format", "mp3",
        "--embed-thumbnail", "--add-metadata",
        "-o", output_template,
        url
    ]

    try:
        subprocess.run(command, check=True)
        print("\nDownload completed!\n")
    except subprocess.CalledProcessError:
        print("\nError downloading the file. Checking available formats...\n")
        list_formats(url)

def main():
    print_ascii_art()
    update_yt_dlp()
    save_path = None

    while True:
        youtube_url = input("\nPaste the link of the mp3 you want to download: ").strip()
        if not youtube_url:
            print("Invalid input. Please enter a valid URL.")
            continue

        if save_path is None:
            save_path = input("Enter the path where the file should be saved: ").strip()
            if not os.path.isdir(save_path):
                print("Invalid path. Please enter a valid directory.")
                save_path = None
                continue

        print("\nDownloading... Please wait.\n")
        download_mp3(youtube_url, save_path)
        print(f"\nDownload was successfully completed and saved to {save_path}\n")

if __name__ == "__main__":
    main()
