
from pytube import YouTube
from sys import argv

# link = argv[1]
link = ''
youtube_object = YouTube(link)


print("Title: ", youtube_object.title)

print("View: ", youtube_object.views)

yd = youtube_object.streams.get_highest_resolution()

yd.download('./youtube_objectfolder')