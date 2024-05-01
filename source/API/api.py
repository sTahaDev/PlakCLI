from pytube import YouTube
from moviepy.editor import *
from pydub import AudioSegment
from unidecode import unidecode
import source.PlakScript.plakscript as PlakScript

class Youtube:
    def __init__(self) -> None:
        self.musicsFolder = "./source/PlakBase/Musics"
        self.plakScript = PlakScript.PlakScript("./source/PlakBase/Musics.plak")
        pass
    
    def download(self,url):

        yt = YouTube(url)
        video = yt.streams.get_audio_only() 
        video.download(output_path=self.musicsFolder)

        audio = AudioSegment.from_file(self.musicsFolder + "/"+yt.title + ".mp4", format="mp4")
        musicName = unidecode(yt.title).replace(" ","")
        audio.export(self.musicsFolder + "/" + musicName + ".wav", format="wav")

        os.remove(self.musicsFolder + "/" + yt.title + ".mp4")

        self.plakScript.write(yt.title,musicName)

        
        pass


    
