from pytube import Playlist

playlist_url = "https://youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY"
py = Playlist(playlist_url)

print(f'Downloading: {py.title}')

for video in py.videos:
    print(f'Downloading {video.title}...')
    # select the highest resolution progressive stream
    stream = video.streams.filter(progressive=True).order_by(
        'resolution').desc().first()
    # download the stream
    stream.download()

print('All videos have been downloaded.')
