import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivy.clock import Clock
#from kivy_garden.zbarcam import ZBarCam
#from pyzbar.pyzbar import ZBarSymbol


class MainWindow(Screen):
     pass
     
class SecondWindow(Screen):
     dialog=None
     def warning(self,title,text):
         print("cscs")
         if not self.dialog:
             self.dialog=MDDialog(
                 title=title,
                 text=text,
                 buttons=[
                 
                    MDFlatButton(text="Cancle",on_release=self.dismiss),
                    MDRectangleFlatButton(text="ok",on_release=self.logger)
                 ]
             )
         self.dialog.open()        
     def warning2(self,title,text):
         if not self.dialog:
             self.dialog=MDDialog(
                 title=title,
                 text=text,
                 buttons=[
                    MDRectangleFlatButton(text="ok",on_release=self.dismiss)
                 ]
             )        
         self.dialog.open()        
           
     def logger(self,screenname):
          self.dialog.dismiss()
          self.manager.current="Main"
     def dismiss(self,screenname):
          self.dialog.dismiss()
           
class ThirdWindow(Screen):
     def wait(self):
          Clock.schedule_once(self.change_screen,5)
          print("launcg")
     def change_screen(self,dt):
          print("ccdcsd")
          self.manager.transition.direction="down"
          self.manager.current="Main"
          
     
class WindowManager(ScreenManager):
     pass
class MyApp(MDApp):
     
     
     def build(self):
        #create table
        #conn=sqlite3.connect("dcdcmcmdmcdmcd.db")
        

        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Yellow"
        
        return Builder.load_file("my.kv")
     
     
MyApp().run()