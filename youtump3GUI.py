import PySimpleGUI as sg
import os
import filtering
import downloads

layout = [ [sg.Text("Insert a link or search term")],
            [sg.Input(key='-INPUT-')],
            [sg.Radio('Single Song', 'user_radio',key='Single', enable_events=True, default=True), sg.Radio('Playlist', 'user_radio', key='Playlist', enable_events=True)],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Quit') ]]

window = sg.Window('YouTuMp3', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    if event == 'Ok':
        link = filtering.search(values['-INPUT-'])
        filtering.create_and_set_dir()
        if values['Single'] == True:
            window['-OUTPUT-'].update('Downloading Song')
            downloads.download_song(link, True)
            sg.popup(f'Finished downloading song\nYou can find it on {os.getcwd()}')
            
        if values['Playlist'] == True:
            window['-OUTPUT-'].update('Downloading Playlist')
            downloads.download_playlist(link, True)
            sg.popup(f'Finished downloading Playlist\nYou can find it on {os.getcwd()}')
        
        window.close()
            

window.close()