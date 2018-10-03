from qgis.core import *

def pointGDA94(point, crs):
    """
    crs is the renderer crs
    """
    print("in  ProjectGDA.py  in pointGDA94")
    t=QgsCoordinateReferenceSystem()
    t.createFromSrid(4283) 
    f=crs 

    trans = QgsCoordinateTransform(f, t, QgsProject.instance())
    pt = trans.transform(QgsPointXY(point))


    return pt
