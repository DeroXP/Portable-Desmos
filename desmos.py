import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import webview

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Desmos')
        self.setWindowOpacity(0.2)

def on_shown():
    app = QApplication.instance()
    window.setWindowFlags(Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec_())

def on_focus():
    window.setWindowOpacity(1.0)

def on_lost_focus():
    window.setWindowOpacity(0.2)

def create_webview_window():
    webview.create_window('Desmos', url='https://www.desmos.com/calculator', html=None, js_api=None, width=800, height=600, x=None, y=None, resizable=True, fullscreen=False, minimized=False, on_top=True, confirm_close=False, text_select=False)
    webview.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.on_shown = on_shown
    window.on_focus = on_focus
    window.on_lost_focus = on_lost_focus

    create_webview_window()
    sys.exit(app.exec_())
