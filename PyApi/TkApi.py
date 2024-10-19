import time
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from .GeneralApi import StringManager as strApi

class TkinterApi:



    # Places the loading page on the Tk and adds all its items
    def createLoadingPage(
        page,
        frameBg = 'white',
        framePos = {'x':0, 'y':0, 'width':225, 'height':400},
        imgLink = '',
        imgPos = {'x':37, 'y':25, 'width':150, 'height':150},
        addLoadingBar = True,
        loadOrient = 'horizontal',
        loadPos = {'x':30, 'y':200, 'width':171},
        addLoadingBarLBL = True,
        loadLBLPos = {'x':85, 'y':230, 'width':50, 'height':20},
        barUpdateSpeed = 0.025
        ):

        # Makes the loadingscreen frame
        loadingScreenPage = tk.Frame(page, bg = frameBg)
        loadingScreenPage.place(x = framePos['x'], y = framePos['y'],
            width = framePos['width'], height = framePos['height'])

        if imgLink != '':
            # Makes the loadingscreen Img
            loadingScreenImg = Image.open(imgLink)
            loadingScreenImg = loadingScreenImg.resize(
                (imgPos['width'], imgPos['height']), Image.ANTIALIAS)
            loadingScreenImg = ImageTk.PhotoImage(loadingScreenImg)

            imageLabel = tk.Label(loadingScreenPage, image = loadingScreenImg)
            imageLabel.place(x = imgPos['x'], y = imgPos['y'])
        else:
            loadingScreenImg = None

        if addLoadingBar == True:
            # Makes the loading bar for the page
            loadingBar = ttk.Progressbar(loadingScreenPage, orient = loadOrient,
                length = loadPos['width'], mode = 'determinate', value = 0)
            loadingBar.place(x = loadPos['x'], y = loadPos['y'])
        else:
            loadingBar = None

        if addLoadingBarLBL == True:
            # Makes a label to tell the bars percentage
            loadingBarLBL = tk.Label(loadingScreenPage, text = 0,
                justify = 'center')
            loadingBarLBL.place(x = loadLBLPos['x'], y = loadLBLPos['y'],
                width = loadLBLPos['width'], height = loadLBLPos['height'])
        else:
            loadingBarLBL = None


        return page, loadingScreenPage, loadingBar, loadingBarLBL, barUpdateSpeed, (loadingScreenImg)



    # Starts the loading page process
    def startLoadingPage(loadingPageInfo):
        # Sets variables to save the required page info
        page = loadingPageInfo[0]
        loadingScreenPage = loadingPageInfo[1]
        loadingBar = loadingPageInfo[2]
        loadingBarLBL = loadingPageInfo[3]
        barUpdateSpeed = loadingPageInfo[4]

        page.update()
        loadingScreenPage.lift()

        # makes both loading bar and label updates
        if loadingBar != None and loadingBarLBL != None:
            # Loops through the percentages to move the loop and update it
            for loadPercent in range(1, 100):
                loadingBar['value'] = loadPercent
                loadingBarLBL['text'] = loadPercent

                page.update()
                time.sleep(barUpdateSpeed)

        # makes only loading bar updates
        elif loadingBar != None:
            # Loops through the percentages to move the loop and update it
            for loadPercent in range(1, 100):
                loadingBar['value'] = loadPercent

                page.update()
                time.sleep(barUpdateSpeed)

       # makes only label updates
        elif loadingBarLBL != None:
            # Loops through the percentages to move the loop and update it
            for loadPercent in range(1, 100):
                loadingBarLBL['text'] = loadPercent

                page.update()
                time.sleep(barUpdateSpeed)

        loadingScreenPage.destroy()



    # Makes a page with a color chosing wheel and returns the selected color
    def colorPicker():
        # Imports the tkinter color choser class
        from tkinter.colorchooser import askcolor

        # Opens the color picker
        colors = askcolor(title="Tkinter Color Chooser")

        # Choses the hex color from the returned rgb/hex option
        selectedHexColor = colors[1]

        return selectedHexColor



    # Returns the x and y position of the mouse cursor
    def getMousePos(element):
        # winfo_pointer<x/y> finds mouse pos on element compared to monitor area
        mouseMonitorXPos = element.winfo_pointerx()
        mouseMonitorYPos = element.winfo_pointery()

        # winfdo_root<x/y> returns the elements canvas <x/y> position
        elementXPos = element.winfo_rootx()
        elementYPos = element.winfo_rooty()

        # subtracts the element position from the mouse position
        mouseXPos = mouseMonitorXPos - elementXPos
        mouseYPos = mouseMonitorYPos - elementYPos

        # Returns the x and y pos in a tupple
        return (mouseXPos, mouseYPos)



    # Delets the children widget of a specified widget (area)
    def clearArea(area, types = []):
        # gets the children elements of the area
        areaWidget = area.winfo_children()

        # Checks if a full wipe was requrested or only specific elements
        if types != []:
            for widgetType in types:
                for widget in areaWidget:
                    if strApi.filterAlpha(widget) == widgetType:
                        widget.destroy()

        else:
            for widget in areaWidget:
                widget.destroy()



    # Returns a list with all the keys for a specific widget
    def getElementAttribs(widget):
        return widget.keys()



    # Takes sent configure values and runs them through a loop
    def editWidget(widget, **confargs):
        if confargs != {}:
            # Gets all of the arguments sent to confargs
            for arg, value in confargs.items():
                widget[arg] = value



    # Makes a Tkinter page
    def createTk(geometry = None, title = None, **confargs):
        # Creates the tk page
        page = tk.Tk()

        if geometry != None:
            page.geometry(geometry)

        if title != None:
            page.title(title)

        if confargs != {}:
            # Gets all of the arguments sent to confargs
            for arg, value in confargs.items():
                page[arg] = value


        # returns the tk page variable so it can be used wherever it is called
        return page



    # Makes various widgets from tkinter
    def createWidget(elementType, area, pos = {}, **confargs):
        elementTypes = {
        'label': tk.Label, 'button': tk.Button,
        'canvas': tk.Canvas, 'frame': tk.Frame,
        'optionmenu': tk.OptionMenu, 'entry': tk.Entry,
        'menu': tk.Menu, 'toplevel': tk.Toplevel,
        'scrollbar': tk.Scrollbar, 'listbox': tk.Listbox
        }

        element = elementTypes[elementType](area)

        if pos != {}:
            if elementType == 'canvas':
                element.place(x = pos['x'], y = pos['y'])

            else:
                element.place(x = pos['x'], y = pos['y'],
                    width = pos['width'], height = pos['height'])

        # Gets all of the arguments sent to confargs
        for arg, value in confargs.items():
            element[arg] = value

        # returns the newly created element variable
        return element



    # Makes a tkinter mainloop
    def createMainLoop():
        tk.mainloop()
