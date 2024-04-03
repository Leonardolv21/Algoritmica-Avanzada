import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class ReproductorMusica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reproductor de Música")
        self.setGeometry(200, 200, 600, 650)

        self.boton_playlist = QPushButton("Playlist", self)
        self.boton_playlist.setGeometry(50, 50, 200, 30)
        self.boton_playlist.clicked.connect(self.mostrar_playlist)

        self.boton_canciones = QPushButton("Canciones", self)
        self.boton_canciones.setGeometry(50, 100, 200, 30)
        self.boton_canciones.clicked.connect(self.mostrar_interfaz_canciones)

        self.boton_albumes = QPushButton("Álbumes", self)
        self.boton_albumes.setGeometry(50, 150, 200, 30)
        self.boton_albumes.clicked.connect(self.mostrar_albumes)

        self.boton_agregar_musica = QPushButton("Agregar música", self)
        self.boton_agregar_musica.setGeometry(50, 200, 200, 30)
        self.boton_agregar_musica.clicked.connect(self.agregar_musica)

        self.etiqueta_estado = QLabel(self)
        self.etiqueta_estado.setGeometry(50, 310, 300, 30)

        self.media_player = QMediaPlayer()

        self.interfaz_canciones = None

    def mostrar_playlist(self):
        self.mostrar_estado("Mostrando Playlist")

    def mostrar_interfaz_canciones(self):
        if not self.interfaz_canciones:
            self.interfaz_canciones = InterfazCanciones(self)
            self.boton_playlist.hide()
            self.boton_canciones.hide()
            self.boton_albumes.hide()
        self.interfaz_canciones.show()

    def mostrar_albumes(self):
        self.mostrar_estado("Mostrando Álbumes")

    def agregar_musica(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            for file_path in file_paths:
                if file_path.endswith('.mp3'):
                    if not self.interfaz_canciones:
                        self.interfaz_canciones = InterfazCanciones(self)
                        self.boton_playlist.hide()
                        self.boton_canciones.hide()
                        self.boton_albumes.hide()
                    self.interfaz_canciones.lista_canciones.addItem(file_path)
                    self.mostrar_estado(f"Agregando música: {file_path}")
                    self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
                    self.media_player.play()
                else:
                    self.mostrar_estado("Solo se admiten archivos MP3.")

    def mostrar_estado(self, mensaje):
        self.etiqueta_estado.setText(mensaje)

class InterfazCanciones(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Lista de Canciones")
        self.setGeometry(50, 50, 300, 300)

        self.lista_canciones = QListWidget(self)
        self.lista_canciones.setGeometry(50, 50, 200, 150)
        
        self.boton_reproducir = QPushButton("Reproducir", self)
        self.boton_reproducir.setGeometry(50, 220, 80, 30)
        self.boton_reproducir.clicked.connect(self.reproducir)

        self.boton_pausa = QPushButton("Pausa", self)
        self.boton_pausa.setGeometry(140, 220, 80, 30)
        self.boton_pausa.clicked.connect(self.pausar)

        self.boton_detener = QPushButton("Detener", self)
        self.boton_detener.setGeometry(230, 220, 80, 30)
        self.boton_detener.clicked.connect(self.detener)

        self.boton_atras = QPushButton("Atrás", self)
        self.boton_atras.setGeometry(50, 260, 260, 30)
        self.boton_atras.clicked.connect(self.volver_atras)

        self.media_player = QMediaPlayer()

    def reproducir(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            return
        self.media_player.play()

    def pausar(self):
        if self.media_player.state() == QMediaPlayer.PausedState:
            return
        self.media_player.pause()

    def detener(self):
        if self.media_player.state() == QMediaPlayer.StoppedState:
            return
        self.media_player.stop()

    def volver_atras(self):
        self.parent().boton_playlist.show()
        self.parent().boton_canciones.show()
        self.parent().boton_albumes.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ReproductorMusica()
    
ventana.show()
sys.exit(app.exec_())