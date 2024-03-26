from microbit import *

while True:
    if button_a.was_pressed():
        

        weather = int(temperature()) 
        display.scroll(weather)
        sleep(2000)

        if weather < 10: 

            display.scroll('Muista lämpimän takin!') 

        elif weather > 10 and weather < 20: 

            display.scroll('Muista puseron!') 

        elif weather > 20 and weather < 28:

            display.scroll('Muista T-paidan!')

        elif weather > 28:
            display.scroll('Mene uimaan!')

   