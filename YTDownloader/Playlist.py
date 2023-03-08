import pytube

def playlist(link):
    pl = pytube.Playlist(link)
    print(f'Playlist: {pl.title}'); print()

    errors = []
    j = 0
    for video in pl.videos:
        try:
            print(f"Downloading: {video.title}")
            video.streams[1].download()
            print(f"{video.title} downloaded successfully!")
        except:
            errors.append(video.title)
            print(f"Error downloading {video.title}")
        j += 1


    if len(errors) == 0:
        print("Download Complete!")
    else:
        print("Errors occurred while downloading the following videos:")
        for title in errors:
            print(f"- {title}")




if __name__ == "__main__":
    
    playlist("https://youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf")
