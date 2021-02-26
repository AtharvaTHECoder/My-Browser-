import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        navbar = QToolBar()
        self.addToolBar(navbar)
        backButn = QAction('<', self)
        backButn.triggered.connect(self.browser.back)
        navbar.addAction(backButn)

        forwButn = QAction('>', self)
        forwButn.triggered.connect(self.browser.forward)
        navbar.addAction(forwButn)

        reloButn = QAction('@', self)
        reloButn.triggered.connect(self.browser.reload)
        navbar.addAction(reloButn)

        youBtn = QAction('Youtube', self)
        youBtn.triggered.connect(self.youtube)
        navbar.addAction(youBtn)

        homeButn = QAction('Home', self)
        homeButn.triggered.connect(self.navigate_home)
        navbar.addAction(homeButn)

        gitButn = QAction('GitHub', self)
        gitButn.triggered.connect(self.github)
        navbar.addAction(gitButn)

        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.UrlBar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def youtube(self):
        self.browser.setUrl(QUrl('http://youtube.com'))

    def github(self):
        self.browser.setUrl(QUrl('http://github.com'))

    def navigate_to_url(self):
        url = self.UrlBar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, urL):
        self.UrlBar.setText(urL.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Atharva Browser')
window = MainWindow()
app.exec_()