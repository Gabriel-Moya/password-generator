import PySimpleGUI as sg
import random


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlack')

        layout = [
            [sg.Text('Qtd. dígitos:', size=(10, 0)), sg.Input(size=(20, 0), key='length')],
            [sg.Checkbox('ABC', key='upper_check'), sg.Checkbox('abc', key='lower_check'),
             sg.Checkbox('123', key='number_check'), sg.Checkbox('!@#', key='simbols_check')],
            [sg.Output(size=(30, 0))],
            [sg.Button('Gerar senha')]
        ]

        self.janela = sg.Window('Gerador de senhas').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            password = ""
            print(password)

            length = int(self.values['length'])
            upper_check = self.values['upper_check']
            lower_check = self.values['lower_check']
            number_check = self.values['number_check']
            simbols_check = self.values['simbols_check']

            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower = "abcdefghijklmnopqrstuvwxyz"
            numbers = "0123456789"
            simbols = "[]{}()<>;:/?,.-=_+!@#$%¨&*~^"

            all = ""
            if upper_check:
                all += upper
            if lower_check:
                all += lower
            if number_check:
                all += numbers
            if simbols_check:
                all += simbols

            password = "".join(random.sample(all, length))
            print(password)


TelaPython().Iniciar()
