import sys
import math
import time
from PIL import Image
from threading import Thread
sys.path.append('PyApi')
from PyApi.TkApi import TkinterApi as tkapi



class TrackingEye:

    def __init__(self, page, canvas, eyeMidCoords, eyeRadius, pupilSize, outlineSize):
        self.alive = True # Sets the while loop to on

        self.page = page # Saves the Tk
        self.canvas = canvas # Saves the Canvas
        self.eyeMidCoords = eyeMidCoords # saves the middle of the eye area
        self.eyeRadius = eyeRadius # Saves the radius for the eye
        self.pupilSize = pupilSize # Saves the size for the pupil

        self.makeEye(outlineSize)


    def getPupilPos(self):
        self.offset = (self.pupilSize / 2) # Offset is one half the pupil size (This could also have been the radius)

        # Uses offset to create the full pupil size
        x1, x2 = (self.eyeMidCoords[0] - self.offset), (self.eyeMidCoords[0] + self.offset)
        y1, y2 = (self.eyeMidCoords[1] - self.offset), (self.eyeMidCoords[1] + self.offset)

        return [x1, y1, x2, y2] # Returns the coords in a clean usable way


    def getEyePosition(self):
        # Uses the center of the circle and the circles rad to create the circle
        x1, x2 = self.eyeMidCoords[0] - self.eyeRadius, self.eyeMidCoords[0] + self.eyeRadius
        y1, y2 = self.eyeMidCoords[1] - self.eyeRadius, self.eyeMidCoords[1] + self.eyeRadius

        return [x1, y1, x2, y2] # Returns the coords in a clean usable way


    def makeEye(self, outlineSize):
        # Retrieves the coordinates for the eyes outline and writes it to the canvas
        eyePosition = self.getEyePosition()
        self.eye = self.canvas.create_oval(eyePosition, outline = 'black', width = outlineSize)

        # Retrieves the coordinates for the pupil and places it into the canvas
        pupilPos = self.getPupilPos()
        self.pupil = self.canvas.create_oval(pupilPos, outline = 'black', fill = 'black', width = 0)

        # Creates a thread to run the function that makes the eyes follow the cursor
        Thread(target = self.addTracking, daemon = True).start()


    def getRadiansFromCenter(self, circleCenter, outsidePos):
        # Uses the center of the circle and the position outside (in this specific case the mouses position) to find the change
        # using the atan2 formula and the change in x and y to get the angle between the two points
        # Adds pi to add 180 degrees (b/c 1 pi is 180 degrees when in radians)

        deltaX = circleCenter[0] - outsidePos[0]
        deltaY = circleCenter[1] - outsidePos[1]

        return math.atan2(deltaX, deltaY) + math.pi


    def findPosOnCircle(self, radian):
        # Uses an angle in radians to determine where on the border of the circle the point of that angle is

        # Uses the midpoint of the eye, the radius of the eye - the pupils offset (radius) (to keep the pupil in the eye), and the sin/cos of the radian
        x = self.eyeMidCoords[0] + ((self.eyeRadius - self.offset) * math.sin(radian))
        y = self.eyeMidCoords[1] + ((self.eyeRadius - self.offset) * math.cos(radian))

        return [x, y]


    def checkIfInCircle(self, mousePosition):
        # Uses the distance formula (x - xoffset)^2 + (y - yoffset)^2 >/</= r^2
        # x is the midpoint x of the circle, y is the midpoint y, radius is the radius of the circle - the radius of the pupil
        if((self.eyeMidCoords[0] - mousePosition[0]) ** 2 + (self.eyeMidCoords[1] - mousePosition[1]) **2 <= (self.eyeRadius - self.offset) ** 2):
            return True

        else:
            return False


    def addTracking(self):

        while self.alive:
            mousePosition = tkapi.getMousePos(self.page)

            if(self.checkIfInCircle(mousePosition)): # Checks if the cursor is inside of the eye
                newPupilPos = [mousePosition[0] - self.offset, mousePosition[1] - self.offset, mousePosition[0] + self.offset, mousePosition[1] + self.offset]
                self.canvas.coords(self.pupil, newPupilPos)

            else: # If not in the eye, it is presumably outside of the eye
                radian = self.getRadiansFromCenter(self.eyeMidCoords, mousePosition) # Checks the radians comapred to the mouse from the center of the circle
                posOnCircle = self.findPosOnCircle(radian) # Finds what position on the circle the pupil should be

                # Creates the pupil position using the coordinates given
                newPupilPos = [posOnCircle[0] - self.offset, posOnCircle[1] - self.offset, posOnCircle[0] + self.offset, posOnCircle[1] + self.offset]
                self.canvas.coords(self.pupil, newPupilPos) # Moves the pupil to that position

            time.sleep(0.015) # pauses the program for a little bit










if __name__ == '__main__':
    class MakeGUI:

        def __init__(self):
            self.makeTk()
            self.makeCanvas()


        def makeTk(self):
            tkGeo = '100x100'

            self.page = tkapi.createTk(geometry = tkGeo + "-20-40", title = 'Eyes')


        def makeCanvas(self):
            self.page.update()
            pageHeight, pageWidth = self.page.winfo_height(), self.page.winfo_width()
            canvasPos = {'x':0,'y':0}

            self.canvas = tkapi.createWidget('canvas', self.page, canvasPos, width = pageWidth, height = pageHeight,
            background = 'white', highlightthickness = 0)
    
    eyeInstances = []
    firstGUI = MakeGUI()

    eyeInstances.append(TrackingEye(firstGUI.page, firstGUI.canvas, [50, 50], 50, 50, 3))
    firstGUI.page.wm_attributes('-topmost', 1)

    tkapi.createMainLoop()