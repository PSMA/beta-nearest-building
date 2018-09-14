print("in  ClickManagement  start of program")
#this code controls the interaction with the map canvas via mouse.
from qgis.core import *

from qgis.gui import *


class GetClick(QgsMapTool):
    print("in class click tool")
    def __init__(self,iface, callback):
        print("in ClickManagement.py class getClick in def __init__")
        QgsMapTool.__init__(self,iface.mapCanvas())
        self.iface      = iface
        self.callback   = callback
        self.canvas     = iface.mapCanvas()

        return None


    def canvasReleaseEvent(self,e):
        #Mouse release event for overriding. Default implementation does nothing. 
        #https://qgis.org/api/classQgsMapTool.html#ab8a832825badb4b170c0e0c18e1f6c79
        print("in function canvasReleaseEvent")
        point = self.canvas.getCoordinateTransform().toMapPoint(e.pos().x(),e.pos().y())
        print(point)
        self.callback(point)
        return None

