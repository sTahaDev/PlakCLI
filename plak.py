import source.API.api as Api
import os
import config
import time
from playsound import playsound
import source.PlakScript.plakscript as pk
import pygame
import source.banner as banner

class Plak:
    def __init__(self) -> None:
        self.banner = banner.banner_string
        self.youtube = Api.Youtube()
        self.musicPlakPath = "./source/PlakBase/Musics.plak"
        self.plakScriptMusic = pk.PlakScript(self.musicPlakPath)
        self.plakScriptPlayList = pk.PlakScript("./source/PlakBase/PlayLists")

        self.options = [
            {'id':1, 'title':'Şarkı indir.','func':self.option_download_music},
            {'id':2, 'title':'Şarkı Çal.','func':self.option_play_music},
            {'id':3, 'title':'Şarkı Sil.','func':self.option_delete_music},
            {'id':4, 'title':'Playlist oluştur.','func':self.option_create_playlist},
            {'id':5, 'title':'Playlist şarkı ekle.','func':self.option_add_music_to_playlist},
            {'id':6, 'title':'Playlist Görüntüle.','func':self.option_view_playlist},
            {'id':7, 'title':'Playlist şarkı sil.','func':self.delete_music_from_playlist},
            {'id':8, 'title':'Playlist sil.','func':self.delete_playlist},
            {'id':9, 'title':'Playlist Çal.','func':self.play_playlist},
            {'id':10, 'title':'Yardım','func': self.help}
            
        ]
        pass

    def run(self):
        self.clear_cli()
        print(self.banner)
        self.print_menu()
        choice = self.get_user_choice('')
        if(choice == "exit"):
            exit()
        for item in self.options:
            if int(choice) == item['id']:
                self.clear_cli()
                item['func']()
        pass
    def help(self):
        self.clear_cli()
        print(f"Version: {config.version}")
        print("Geri Gelme: exit")
        print("Uygulamayı Kapatma: quit")
        print("Şarkıyı Durdurma: pause")
        print("Şarkıyı Başlatma: play")

        self.get_user_choice("Çıkmak için ENTER'a tıkla")
        self.run()
        pass
    def clear_cli(self):
        if(config.os == "macos" or config.os == "linux"):
            os.system("clear")
        elif(config.os == "windows"):
            os.system("cls")
        else:
            print("Config File 'OS' error! Edit config.py")
        pass
    def delete_playlist(self):
        self.clear_cli()
        playListPath = "./source/PlakBase/PlayLists"
        playLists = os.listdir(playListPath)
        
        

        i = 1
        for item in playLists:
            item = item.replace(".plak","")
            print(f"{i}-{item}")
            i+=1
            pass

        choosedPlayList = self.get_user_choice("Playlist seç")
        if(choosedPlayList == "exit"):
            self.run()
        path = playListPath + "/" + playLists[int(choosedPlayList)-1]
        os.remove(path)

        self.clear_cli()
        print("Başarıyla Silindi !")
        time.sleep(1)
        self.run()

        
        pass
    def delete_music_from_playlist(self):
        self.clear_cli()
        playListPath = "./source/PlakBase/PlayLists"
        playLists = os.listdir(playListPath)
        
        

        i = 1
        for item in playLists:
            item = item.replace(".plak","")
            print(f"{i}-{item}")
            i+=1
            pass

        choosedPlayList = self.get_user_choice("Playlist seç")
        if(choosedPlayList == "exit"):
            self.run()
        self.plakScriptMusic.FilePath = playListPath + "/" + playLists[int(choosedPlayList)-1]

        original,unicoded = self.plakScriptMusic.read()
        
        self.clear_cli()
        i = 1
        for item in original:
            print(f"{i}-{item}")
            i+=1

        self.plakScriptMusic.FilePath = self.musicPlakPath

        choosedMusic = self.get_user_choice("Şarkı sil")
        if(choosedMusic == "exit"):
            self.delete_music_from_playlist()
        self.plakScriptPlayList.FilePath = playListPath + "/" + playLists[int(choosedPlayList)-1]
        self.plakScriptPlayList.delete(int(choosedMusic)-1)

        print("Başarıyla Silindi!")
        time.sleep(0.5)
        self.run()

        pass

    def play_playlist(self):
        self.clear_cli()
        playListPath = "./source/PlakBase/PlayLists"
        playLists = os.listdir(playListPath)
        
        

        i = 1
        for item in playLists:
            item = item.replace(".plak","")
            print(f"{i}-{item}")
            i+=1
            pass

        choosedPlayList = self.get_user_choice("Playlist seç")

        self.plakScriptMusic.FilePath = playListPath + "/" + playLists[int(choosedPlayList)-1]
        original,unicoded = self.plakScriptMusic.read()
        self.plakScriptMusic.FilePath = self.musicPlakPath

        i = 0
        for item in unicoded:
            self.playMusicForPlaylist("./source/PlakBase/Musics/"+item + ".wav" , original[i])
            i+= 1
       
        pass

    def option_delete_music(self):
        self.clear_cli()
        self.plakScriptMusic.FilePath = self.musicPlakPath
        originalNames,unicodedNames = self.plakScriptMusic.read()
        self.print_all_musics()

        choice = self.get_user_choice("Şarkı Silmek için numara gir (çıkmak için 'exit')")
        if(choice == "exit"):
            self.run()
        
        choice = int(choice) - 1

        self.plakScriptMusic.delete(choice)
        os.remove("./source/PlakBase/Musics/" + unicodedNames[choice] + ".wav")
        self.clear_cli()
        print("Başarıyla Silindi!")
        time.sleep(1.5)

        self.run()

        pass

    def option_view_playlist(self):
        self.clear_cli()
        playListPath = "./source/PlakBase/PlayLists"
        playLists = os.listdir(playListPath)
        
        

        i = 1
        for item in playLists:
            item = item.replace(".plak","")
            print(f"{i}-{item}")
            i+=1
            pass

        choosedPlayList = self.get_user_choice("Playlist seç")
        if(choosedPlayList == "exit"):
            self.run()
        self.plakScriptMusic.FilePath = playListPath + "/" + playLists[int(choosedPlayList)-1]

        original,unicoded = self.plakScriptMusic.read()
        
        self.clear_cli()
        i = 1
        for item in original:
            print(f"{i}-{item}")
            i+=1

        self.plakScriptMusic.FilePath = self.musicPlakPath

        self.get_user_choice("Çıkmak için ENTER'a tıkla")
        self.run()
        pass

    def option_add_music_to_playlist(self):
        self.clear_cli()
        playListPath = "./source/PlakBase/PlayLists"
        musicsOrginal,musicsUnicoded = self.plakScriptMusic.read()
        playLists = os.listdir(playListPath)

        i = 1
        for item in playLists:
            item = item.replace(".plak","")
            print(f"{i}-{item}")
            i += 1
            pass

        choosedPlayListIndex = self.get_user_choice("Playlist seç")
        self.plakScriptPlayList.FilePath = playListPath + "/" + playLists[int(choosedPlayListIndex)-1]

        self.print_all_musics()

        musicsOrginal,musicsUnicoded = self.plakScriptMusic.read()
        while True:
            self.clear_cli()
            self.print_all_musics()
            choosedMusic = self.get_user_choice("Şarkı Seç (Çıkmak için 'exit' yaz) ")
            if(choosedMusic == "exit"):
                break
            
            playListMusicOrginal,playListMusicUnicoded = self.plakScriptPlayList.read()
            isMusicAlreadyAded = False
            for item in playListMusicUnicoded:
                if item == musicsUnicoded[int(choosedMusic)-1]:
                    isMusicAlreadyAded = True
                    
            if isMusicAlreadyAded:
                self.clear_cli()
                print("Bu şarkı zaten ekli !")
                time.sleep(1.5)
                continue
            self.plakScriptPlayList.write(musicsOrginal[int(choosedMusic)-1],musicsUnicoded[int(choosedMusic)-1])
            self.clear_cli()
            print("Başarıyla Eklendi!")
            time.sleep(0.5)
            pass
        
        self.run()
        pass

    def option_create_playlist(self):
        self.clear_cli()
        playlistName = self.get_user_choice("Playlist ismi")

        playListPath = "./source/PlakBase/PlayLists"

        open(playListPath + "/" + playlistName + ".plak","w")

        print("Başarıyla Oluşturuldu !")
        self.run()
        pass

    def option_download_music(self):
        self.clear_cli()
        url = self.get_user_choice('Url Girin')
        print("İndirme Başladı!")
        self.download_music(url)
        print("İndirme Başarılı!")
        time.sleep(1)
        self.run()
        pass
    
    def print_all_musics(self):
        musicsOrginal,musicsUnicoded = self.plakScriptMusic.read()
        print("----Şarkılar----")
        print("----------------\n")


        i = 1
        for music in musicsOrginal:
            print(f"{i}-{music}")
            i += 1
            pass
        pass

    def playMusic(self,path,name):
        self.clear_cli()
        pygame.init()

        pygame.mixer.music.load(path)

        pygame.mixer.music.play(-1)

        while True:
            self.clear_cli()
            print(f"-----{name}-----")
            print("")
            print("Durdurmak için: pause")
            print("Başlatmak için: play")
            print("Çıkmak için: exit")

            choice = self.get_user_choice("")
            print(choice)
            if choice == "pause":
                pygame.mixer.music.pause()
            elif(choice == "play"):
                pygame.mixer.music.unpause()
            elif choice == "exit":
                break

        pygame.quit()
        self.option_play_music()

        pass

    def playMusicForPlaylist(self,path,name):
        self.clear_cli()
        pygame.init()

        pygame.mixer.music.load(path)

        pygame.mixer.music.play(-1)

        while True:
            self.clear_cli()
            print(f"-----{name}-----")
            print("")
            print("Durdurmak için: pause")
            print("Başlatmak için: play")
            print("Sıradaki Şarkı: next")
            print("Çıkmak için: exit")

            choice = self.get_user_choice("")
            print(choice)
            if choice == "pause":
                pygame.mixer.music.pause()
            elif(choice == "play"):
                pygame.mixer.music.unpause()
            elif(choice == "next"):
                break
            elif choice == "exit":
                pygame.quit()
                self.run()
                break

        pygame.quit()
        

        pass

    def option_play_music(self):
        self.clear_cli()
        folder_path = "./source/PlakBase/Musics"

        
        musicsOrginal,musicsUnicoded = self.plakScriptMusic.read()
        self.print_all_musics()

        choice = self.get_user_choice("Şarkı Numarası Seç (Çıkmak için 'exit' yaz)")
        if(choice == "exit"):
            self.run()
        choice = int(choice) - 1
        
        self.playMusic(folder_path +"/"+ musicsUnicoded[choice] + ".wav",musicsOrginal[choice])
        pass

    def download_music(self,url):
        self.youtube.download(url)
        pass

    def get_user_choice(self,info):
        print('')
        if(info):
            print(info)
        user_choice = input(": ")
        if(user_choice == "quit"):
            exit()
        
        return user_choice

    def print_menu(self):
        
        for item in self.options:
            print(f'{item["id"]}-{item["title"]}')
        pass



