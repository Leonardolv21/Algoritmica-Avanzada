import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Reproductor de Música")
        self.master.geometry("300x200")

        self.playlist = []
        self.current_index = 0

        self.play_button = tk.Button(self.master, text="▶️", command=self.play_music)
        self.play_button.grid(row=0, column=0, padx=10, pady=10)

        self.pause_button = tk.Button(self.master, text="⏸️", command=self.pause_music)
        self.pause_button.grid(row=0, column=1, padx=10, pady=10)
        self.pause_button.config(state=tk.DISABLED)

        self.stop_button = tk.Button(self.master, text="⏹️", command=self.stop_music)
        self.stop_button.grid(row=0, column=2, padx=10, pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.add_button = tk.Button(self.master, text="Agregar Música", command=self.add_music)
        self.add_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.favorite_button = tk.Button(self.master, text="Marcar como Favorita", command=self.mark_as_favorite)
        self.favorite_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.favorite_button.config(state=tk.DISABLED)

    def add_music(self):
        file_path = filedialog.askopenfilename(title="Selecciona archivos de música", filetypes=[("Archivos MP3", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)

    def play_music(self):
        if self.playlist:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(self.playlist[self.current_index])
                pygame.mixer.music.play()
                self.play_button.config(state=tk.DISABLED)
                self.pause_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.NORMAL)
                self.favorite_button.config(state=tk.NORMAL)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        self.favorite_button.config(state=tk.DISABLED)

    def mark_as_favorite(self):
        print("Canción marcada como favorita.")

def main():
    pygame.init()
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
    pygame.quit()

if __name__ == "__main__":
    main()
