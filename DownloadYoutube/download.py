from pytube import YouTube, streams
from pytube.cli import on_progress

link = input("Insira o link: ")

yt = YouTube(link, on_progress_callback= on_progress)

print("Título = ", yt.title)

print("baixando...")

ys = yt.streams.get_highest_resolution()
ys.download()