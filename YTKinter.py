import tkinter as tk
from pytubeyt import download_youtube_from_url
import os

def create_window():
    
    window = tk.Tk()
    window.title("Download YouTube Video")
    window.geometry('600x400')
    window.resizable(width=0, height=0)
    
    url_label = tk.Label(window, text ="URL of YouTube Video",padx=10)
    url_label.grid(row=1, column=1)
    
    url_stringvar = tk.StringVar()
    url_entry = tk.Entry(window , textvariable = url_stringvar,bd = 5,width=40)
    url_entry.grid(row=1,column=2,padx=5)


    downlad_dest_label = tk.Label(window, text ="os path : ",padx=10)
    downlad_dest_label.grid(row=2, column=1)
    
    path_set = os.path.expanduser("~") +"\download\\"
    downlad_dest_stringvar = tk.StringVar()
    downlad_dest_entry = tk.Entry(window , textvariable = downlad_dest_stringvar,bd = 5,width=40)
    downlad_dest_stringvar.set(path_set)
    downlad_dest_entry.grid(row=2,column=2,padx=5)


    quality_intvar =  tk.IntVar()
    video_720P_radio = tk.Radiobutton(window, text='MP4, 720P',variable=quality_intvar, value=0) 
    video_360P_radio = tk.Radiobutton(window, text='MP4, 360P',variable=quality_intvar, value=1)

    video_720P_radio.grid(column=1, row=3)
    video_360P_radio.grid(column=2, row=3)
    download_button = tk.Button(window, text= "download" , command = lambda: download_button_click(url_stringvar,downlad_dest_stringvar,quality_intvar))
    download_button.grid(row=5,column=2, padx=5)


    window.mainloop()


def download_button_click(url_stringvar,os_stringvar,quality_intvar):
    download_youtube_from_url(url_stringvar.get(),os_stringvar.get(),quality_intvar)
    #print(os_stringvar.get())

    


if __name__ == "__main__":
    create_window()

