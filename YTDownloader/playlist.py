import pytube
import os

def cls():
    match os_name:
        case "posix": os.system("clear")
        case "nt": os.system("cls")


def setup():
    fold = "YouTube"
    match os_name:
        case "posix":
            loc = "/home/user/Downloads"
            os.chdir(loc)
            if os.path.exists(fold) == False:
                os.mkdir(fold)
            os.chdir(fold)
            
        case "nt":
            if os.path.exists("downloads") is False:
                os.mkdir("downloads")
            os.chdir("downloads")


def main(quality="360p", extension="mp4", prog=False):
    cls()
    link_playlist = []
    breakpoint = 0

    # Input user
    print("Masukkan Link Playlist")
    while True:
        inputU = input("Link: ")
        if len(inputU) == 0:
            breakpoint += 1
            if breakpoint >= 2:
                break
            continue
        
        if len(link_playlist) > 0:
            for i in link_playlist:
                if inputU != i:
                    link_playlist.append(inputU)
                else:
                    print("Tidak bisa memasukkan link yang sama!")
        else:
            link_playlist.append(inputU)


    #pytube module
    for i in link_playlist:
        pl = pytube.Playlist(i)
        print(f"Playlist:{pl.title}")
        try:
            print(f"Video\t: {pl.length}")
        except:
            print("Tidak dapat menampilkan jumlah video")

        errors = []
        j = 0
        for video in pl.videos:
            try:
                print(f"Downloading: {video.title}")
                try:
                    stream = video.streams.filter(only_audio=False, file_extension=extension , res=quality, type="video", progressive=prog)
                except:
                    stream = video.streams.filter(only_audio=False, type="video", res="360p")  
                
                stream.first().download()

            except:
                print("Failed")
                errors.append(j)
                continue
            j += 1


        ###Error###
        linkerror = []
        o = 0
        for link in pl.video_urls:
            for i in errors:
                if o == i:
                    linkerror.append(link)

        if len(errors) == 0:
            print("Yeay")
        else:
            print(f"Gagal di download:")
            for i in linkerror:
                print(i)

    print("Complete!")









if __name__ == "__main__":
    os_name = os.name
    cls()
    setup()
    main(quality="720p")

#Update:
#   Nope