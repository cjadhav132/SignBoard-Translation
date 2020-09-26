import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from image_example import imk
from tra import var
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '780')
Config.set('graphics', 'resizable', False)

lan=""
ls=1

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    #filechooser = ObjectProperty(None)

    def __init__(self,load,cancel):
        super(LoadDialog, self).__init__()
        self.load = load
        self.cancel = cancel
        path = os.path.join(os.getcwd(),'images')
        self.filechooser.path = path





class LangDialog(FloatLayout):
    lang = ObjectProperty(None)

    #text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class TraLangDialog(FloatLayout):
    lang = ObjectProperty(None)
    #text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ImageKv(FloatLayout):
    pass




class dot(FloatLayout):

    def __int__(self):
        self.a = None
        self.scr_lan = 'hin'
        self.des_lan = 'en'
        #self.awe = "ok"


    textinput1 = ObjectProperty(None)
    btn_scr = ObjectProperty(None)
    btn_des = ObjectProperty(None)

    def ocr_lang(self,code,lan):
        sor='Source: '
        sor_t=sor+lan
        self.scr_lan=code
        self.btn_scr.text=sor_t
        #print(self.scr_lan)
        self.dismiss_popup()

    def trans_lang(self,code,lan):
        sor = 'Destination: '
        sor_t = sor + lan
        self.btn_des.text = sor_t
        self.des_lan=code
        #print(self.des_lan)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):

        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def select_lang_ocr(self):
        content = LangDialog(lang=self.ocr_lang, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Language", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def select_lang_trans(self):
        content = TraLangDialog(lang=self.trans_lang, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Language", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def Trans_act(self):
        try:
            c = imk.img(self.a,self.scr_lan,self.des_lan)
            self.text_out.text = c
        except BaseException as e:
            print("error",e)
            print(type(e))
        #print(c)


    def only_text(self):
        vr1 = var.trann(self.textinput1.text, self.des_lan)
        print(vr1)
        self.text_out.text = vr1



    def load(self, filename):
        a=filename[0]
        print(a)
        self.dismiss_popup()
        self.image_tag.source = a
        self.a=a
        #print(a)



class nsc(App):
    pass

Factory.register('dot', cls=dot)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('LangDialog', cls=LangDialog)


if __name__ == '__main__':
    nsc().run()