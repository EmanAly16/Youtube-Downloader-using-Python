from pytube import YouTube
from pytube import Playlist
link = "https://www.youtube.com/watch?v=2vEEa1IKV1M"
#link = input("please enter the video url: ")

video = YouTube(link)

print(f"The video title is:\n{video.title}\n")
print(f"The video description is:\n{video.description}\n")
print(f"The video duration is:\n{video.length/60} minutes\n")

# for Quality
#progressive = True mean photo and audio
#video with resolation greater than 720p must has progressive = False (it will be video without audio)
for stream in video.streams:
    print(stream)

# filtering can has multi parametar
for stream in video.streams.filter(progressive=True):
    print(stream)

#progressive = True with high res
print(video.streams.get_highest_resolution())

def finish():
    print("Download Done")

# can add pram filename = "name to download with"
video.streams.get_lowest_resolution().download(output_path="C:/Users/user/Downloads")
# to check video download done or not 
video.register_on_complete_callback(finish())

#to download PlayList
playlist_link =""
playlist = Playlist(playlist_link)

for video in playlist.videos:
    video.streams.get_lowest_resolution().download(output_path="")


#doc : https://pytube.io/en/latest/