import yt_dlp  #This library let's you download anyhin from YouTube we use it for audio only

def download_youtube_audio_as_mp3(url): #Parameters for the download
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s', 
        'noplaylist': True,
        'verbose': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',   # Convert to audio only
            'preferredcodec': 'mp3',       # Convert to mp3
            'preferredquality': '192',     # Bitrate 192 kbps
        }],
    }

    try:  
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading and converting: {url}")
            ydl.download([url])  #<<-- This is the download function
            print("Audio saved as MP3 in the current folder!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("YouTube URL: ").strip()
    if url:
        download_youtube_audio_as_mp3(url)
    else:
        print("Invalid URL! Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ") #This is Rickroll be aware
