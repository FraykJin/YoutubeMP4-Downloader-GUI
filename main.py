from pytube import YouTube
import pytube
# yt = YouTube(url="https://www.youtube.com/watch?v=hCjcgoubkPM")
# print(yt.title)
# print(yt.thumbnail_url)
#
# # Les formats medias disponibles
# stream = yt.streams.filter(file_extension='mp4', only_audio=True).first()
# stream.download()

from tkinter import *
from tkinter.messagebox import showwarning, showinfo
from tkinter.filedialog import askdirectory

class YoutubeDownloader(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Sous forme de grille
        #Logo de notre interface graphique
        self.logo = PhotoImage(file='logo.PNG')
        self.canvas = Canvas(self, width=self.logo.width(), height=self.logo.height())
        self.canvas.create_image(0, 0, anchor=NW, image=self.logo)
        self.canvas.grid()


        #Label pour l'input URL
        self.label_url = Label(self, text='Youtube Video URL')
        self.label_url.grid()

        # Input URL: pour le lien de la video Youtube to Download
        self.url_entry = Entry(self, width=100)
        self.url_entry.grid(padx=10, pady=10)

        #Choisir le dossier dans lequel le fichier va etre telecharger et pouvoir le recuperer
        self.path = Button(self, text='Destination du Fichier')
        self.path['command'] = self.getDirectory
        self.path.grid()

        # Bouton qui va appeler une fonction pour telecharger la video youtube
        self.download_button = Button(self, text='Download MP4')
        self.download_button["command"] = self.download
        self.download_button.grid(padx=10, pady=10)


    #Fonctions callback pour les boutons
    def download(self):
        try:
            print(self.directory)
            yt = YouTube(url=f"{self.url_entry.get()}")
            print(yt.title)
            stream = yt.streams.filter(file_extension='mp4', only_audio=True).first()
            stream.download(self.directory)
        except pytube.exceptions.RegexMatchError:
            showwarning(title='Mauvais URL', message='Veuillez entrer un lien valide.\n(ex: https://www.youtube.com/watch?v=csXYMSHuoFU)')
        except AttributeError:
            showwarning(title='Choisir un repertoire', message='Choisissez la destination du fichier')

    def getDirectory(self):
        self.directory = askdirectory()



root = Tk()
root.title('Frayk Youtube DownloaderMP4')
app = YoutubeDownloader(master=root)
app.mainloop()


