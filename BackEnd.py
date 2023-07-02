from pytube import YouTube
from PyQt6.QtCore import QThread, pyqtSignal, QObject
import os

vfolder = f"{os.environ['UserProfile']}/Videos/YouTubeSaves"
afolder = f"{os.environ['UserProfile']}/Music/YouTubeSaves"

class Downloader(QObject):
    progress = pyqtSignal(float)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100
        self.progress.emit(progress)

    def download_video(self, link):
        ytv = YouTube(link, on_progress_callback=self.on_progress)
        #File if path = '/Users/dionysialemonaki/python_project' check_file = os.path.isfile(path)
        ytv.streams.get_highest_resolution().download(
            output_path=vfolder)

    def download_audio(self, link):
        ##name = f'{yta.streams[0].title}.mp3'
        yta = YouTube(link, on_progress_callback=self.on_progress)
        #File if path = '/Users/dionysialemonaki/python_project' check_file = os.path.isfile(path)
        yta.streams.filter(only_audio=True).first().download(
                filename=f'{yta.streams[0].title}.mp3',
                output_path=afolder)

def check_folder():
        VisExist = os.path.exists(vfolder)
        AisExist = os.path.exists(afolder)
        if VisExist == False:
            os.mkdir(vfolder)
        elif AisExist == False:
            os.mkdir(afolder)

#chiiil
