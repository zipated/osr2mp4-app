from Custom.CustomWidgets import PopupLabels

from PyQt5.QtCore import Qt
class PopupWindow(PopupLabels):
    def __init__(self, parent):
        super(PopupWindow, self).__init__(parent)
        self.main_window = parent
        self.img_idle = "images/PopupWindow.png"
        self.setStyleSheet("background-color:transparent;")

        super().setup()

    def resize_(self):
        width, height = 75/100*self.main_window.width(), 75/100*self.main_window.height()
        self.setPixmap(self.pixmap_idle.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        x, y = self.main_window.width() / 2 - self.pixmap().width() / 2, self.main_window.height() / 2 - self.pixmap().height() / 2
        self.setGeometry(x, y, width, height)
        self.main_window.select_osu_folder.resize_()
        self.main_window.select_output_folder.resize_()

