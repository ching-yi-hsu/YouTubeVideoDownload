from pytube import YouTube
import tkinter


def download_youtube_from_url(link,os_path,tp):
    
    yt = YouTube(link)
    if tp == 1:
        video =  yt.streams.filter(file_extension = 'mp4', res ='720p').first()
    else :
        video =  yt.streams.filter(file_extension = 'mp4', res ='360p').first()
    video.download(os_path)

