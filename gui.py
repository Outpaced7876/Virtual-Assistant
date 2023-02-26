import webbrowser
import tkinter as tk
import speech_recognition as sr
import speedtest

import pywhatkit
import tkinter.messagebox

#make ai repeat the same thing as me
#make a pop up menu showing internet speed

class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("guibot")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.root.resizable(width=False, height=False)
        self.root.geometry('700x600')
        self.buttons()
        self.draw('Welcome to Bibby 1.01.\n\nInstructions\n\nPress the talk button to initiate the guibot.\n\ncommands keywords are\n\nOpen (the website you would like to open)\n\n'
                  'Internet speed\n\nPlay(the artist you would like to listen to on youtube)')

        self.root.mainloop()

    def draw(self, msg):
        self.frameText = tk.Frame(self.root, height=19, width=50)
        self.textBox = tk.Text(self.frameText, height=19, width=50, relief='flat', bg='light blue',
                               font='Monospace 18')
        self.textBox.insert(1.0, msg)
        self.textBox.config(state='disabled')
        self.frameText.pack()
        self.textBox.pack(padx=3, pady=3)

    def buttons(self):
        self.button = tk.Button(self.frame, text='Talk', command=self.tasks,width=7,height=1)
        self.button.pack(side=tk.LEFT)
        self.exit = tk.Button(self.frame, text='Exit', command=self.root.destroy,width=7,height=1)
        self.exit.pack(side=tk.LEFT)

    def tasks(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Pass a command.")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            if 'open' in text.lower():
                website_name = text.replace('open', '').strip()
                website = "https://www." + website_name + ".com"
                try:
                    webbrowser.open(website)
                    print('Opening "{}"'.format(website_name))
                except webbrowser.Error as e:
                    print(f"Error: {e}")
                    print(f"Could not open website: {website}")

            elif text.lower() == 'internet speed':
                s = speedtest.Speedtest()
                download_speed = s.download() / 10 ** 6
                upload_speed = s.upload() / 10 ** 6
                tkinter.messagebox.showinfo('Download speed', 'Download speed is {:.2f} Mbps\nUpload speed is {:.2f} Mbps'.format(download_speed,upload_speed))


            elif 'play' in text.lower():
                song = text.replace('play', '').strip()
                print('Playing "{}"'.format(song))
                pywhatkit.playonyt(song)
            elif 'watch' in text.lower():
                video_name = text.replace('watch', '').strip()
                print('Watching "{}"'.format(video_name))
                video_url = "https://www.youtube.com/results?search_query=" + video_name.replace(' ', '+')
                webbrowser.open(video_url)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")

        

if __name__ == '__main__':
    MainWindow()





