import pyautogui

#https://support.google.com/youtube/answer/7631406?hl=pt
#https://canaltech.com.br/software/melhores-atalhos-para-controlar-netflix-no-navegador/

class Default:

    def pause(self):
        pyautogui.press(' ')
    
    def fullScreen(self):
        pyautogui.press('f')

    def aumentarVolume(self):
        pyautogui.press('up')

    def diminuirVolume(self):
        pyautogui.press('down')

    def mute(self):
        pyautogui.press('m')