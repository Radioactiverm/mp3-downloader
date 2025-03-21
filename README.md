# 🎵 | MP3 Downloader
> Powered by: [yt-dlp](https://www.github.com/yt-dlp/yt-dlp)
## ℹ️ | Introduction
This is a custom python program made specificly for downloading a lot of MP3s  
It uses [yt-dlp](https://www.github.com/yt-dlp/yt-dlp) which is an open source project here on GitHub  
This program just makes downloading music more efficient and conviniently downloads the metadata with it,  
for an example: Thumbnail, Song name, Artist etc..
## ✅ | Instalation and ussage
> [!NOTE]
> Before doing anything ensure you have installed the latest version of **yt-dlp** on your machine.
> You can do so by executing "sudo apt install yt-dlp" in your Terminal Emulator
### Downloading:

    sudo git clone https://github.com/Radioactiverm/mp3-downloader && cd mp3-downloader
    chmod +x mp3downloader.py

### Ussage:

    sudo python3 mp3downloader.py

> [!WARNING]
> Make sure that you have installed:  
> yt-dlp , python3

## ✴️ | System integration
If you want the program to be easily executed in the terminal just by wiritng "mp3downloader" folow these steps:  

    nano ~/.bashrc

And add this line at the end of the file:

    alias mp3downloader="python3 /path/to/your/mp3downloader.py"

Example path:  
/home/tobias/Downloads/mp3-downloader/mp3downloader.py  
Now execute this to reload the config file:

    source ~/.bashrc

Test by writing:

    mp3downloader
