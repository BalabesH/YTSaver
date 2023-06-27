from pytube import YouTube
 
link = "https://www.youtube.com/watch?v=jDC5VOvU0As&list=RDjDC5VOvU0As&start_radio=1"
yt = YouTube(link)
yt.streams.first().download()
print("Видео успешно загружено")