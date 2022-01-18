
from typing import Tuple
import unittest, pytest
from PySide6.QtWidgets import QApplication
from Widget import ValueSelectorWidget
from PySide6 import QtCore
from PySide6.QtCore import QTimer

class test_ValueSelectorWidget(unittest.TestCase):

    app=QApplication([])

    def test_SetBoton1TextColor(self):
       widget = ValueSelectorWidget()
       widget.setBoton1TextColor("black")
       self.assertEqual(widget.b1color,"black")

    def test_SetBoton2TextColor(self):
       widget = ValueSelectorWidget()
       widget.setBoton2TextColor("black")
       self.assertEqual(widget.b2color,"black")
         
    def test_SetBoton1BackgroundColor(self):
        widget = ValueSelectorWidget()
        widget.setBoton1BackgroundColor("red")
        self.assertEqual(widget.b1bgcolor,"red")

    def test_SetBoton2BackgroundColor(self):
        widget = ValueSelectorWidget()
        widget.setBoton2BackgroundColor("red")
        self.assertEqual(widget.b2bgcolor,"red")    
    
    def test_SetBoton1Text(self):
        widget = ValueSelectorWidget()
        widget.setBoton1Text("TextoBoton")
        self.assertEqual(widget.boton.text(),"TextoBoton")

    def test_SetBoton2Text(self):
        widget = ValueSelectorWidget()
        widget.setBoton2Text("TextoBoton")
        self.assertEqual(widget.boton2.text(),"TextoBoton")
    
    def test_SetAnimWidgetBackgroundColor(self):
        widget = ValueSelectorWidget()
        widget.setAnimWidgetBackgroundColor("red")
        self.assertEqual(widget.animWidgColor,"red")

    def test_GetBoton1TextColor(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton1TextColor(),"white")

    def test_GetBoton2TextColor(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton2TextColor(),"white")
    
    def test_GetBoton1BackgroundColor(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton1BackgroundColor(),"white")
    
    def test_GetBoton2BackgroundColor(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton2BackgroundColor(),"white")
    
    def test_GetBoton1Text(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton1Text(),"boton")

    def test_GetBoton2Text(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getBoton2Text(),"boton2")    
    
    def test_getAnimWidgetBackgroundColor(self):
        widget = ValueSelectorWidget()
        self.assertEqual(widget.getAnimWidgetBackgroundColor(),"black")
    
    
def test_animation(qtbot):
    widget = ValueSelectorWidget()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.boton, QtCore.Qt.LeftButton)
    coords = widget.animWidget.geometry().getCoords()
    finalCoords = (0,0,99,99)
    assert coords == finalCoords

def test_animation2(qtbot):
    widget = ValueSelectorWidget()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.boton, QtCore.Qt.LeftButton)
    coords = widget.animWidget.geometry().getCoords()
    finalCoords = (0,0,99,99)
    assert coords == finalCoords     

if __name__ == '__main__':
    unittest.main()