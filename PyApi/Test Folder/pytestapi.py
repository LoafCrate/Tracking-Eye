import sys
sys.path.append('..')
from TkApi import TkinterApi as tkapi
from GeneralApi import StringManager as strapi


class testMakeApi:

    def __init__(self):
        self.createPage()
        tkapi.startLoadingPage((tkapi.createLoadingPage(self.page,
            imgLink = 'Self Loathing.png')))
        tkapi.createMainLoop()


    def createPage(self):
        self.page = page = tkapi.createTk(geometry = '500x500', title = 'get fked', background = 'grey21')
       
        self.fillPage()


    def fillPage(self):
        page = self.page

        self.canvas1 = tkapi.createWidget('canvas', page, pos = {'x': 0, 'y': 0}, width = 150, height = 200, bg = 'violet', highlightthickness = 0)
        self.fillCanvas1()
        self.canvas2 = tkapi.createWidget('canvas', page, pos = {'x': 150, 'y': 0},  width = 150, height = 200, bg = 'violet', highlightthickness = 0)
        self.fillCanvas2()


    def fillCanvas1(self):
        for i in range(0, 11):
            lbl = tkapi.createWidget('label', self.canvas1, pos = {'x':0, 'y':(i*20)-10, 'width':100,'height':19}, bg = 'purple')
        for i in range(0, 6):
            lbl = tkapi.createWidget('label', self.canvas1, pos = {'x':100, 'y':(i*40)-10, 'width':50,'height':19}, bg = 'purple')

    def fillCanvas2(self):
        for i in range(0, 11):
            lbl = tkapi.createWidget('label', self.canvas2, pos = {'x':50, 'y':(i*20)-10, 'width':100,'height':19}, bg = 'purple')

        for i in range(0, 6):
            lbl = tkapi.createWidget('label', self.canvas2, pos = {'x':0, 'y':(i*40)+10, 'width':50,'height':19}, bg = 'purple')


test = testMakeApi()
