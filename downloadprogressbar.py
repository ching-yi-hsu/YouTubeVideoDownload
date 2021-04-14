import tkinter as tk
import threading
from tkinter.ttk import Progressbar
from pytube import YouTube

class Download_win:
    def __init__ (self, url,file_os,quality):
        self.url = url
        self.file_os = file_os
        self.quality = quality
        self.download_win = tk.Tk()
        self.progress = Progressbar(self.download_win,orient= "horizontal",length=100,mode='determinate')
        self.progress.grid(row = 3, column = 1)
        self.start_download()
        self.download_win.mainloop()

    def start_download(self):
        self.yt = YouTube(self.url, on_progress_callback= self.call_back_progress, on_complete_callback= self.download_finish)
        if self.quality == 0:
            self.video =  self.yt.streams.filter(file_extension = 'mp4', res ='720p').first()
        elif self.quality == 1 :
            self.video =  self.yt.streams.filter(file_extension = 'mp4', res ='360p').first()
        else:
            self.video =  self.yt.streams.filter(file_extension = 'mp4', res ='1080p').first()
        download_fun = lambda: self.video.download(self.file_os)
        threading.Thread(target=download_fun).start()

    def call_back_progress(self, stream, chunk, bytes_remaining):
        current_percentage = 100 - int(bytes_remaining / self.video.filesize * 100)
        self.progress["value"] = current_percentage
        
    def download_finish(self, _, __):
        self.download_win.destroy()



