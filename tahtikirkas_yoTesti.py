import turtle as t
from random import randint, random
import unittest


runtest = 0

def draw_star (points, size, col, x, y):
    t.speed('slow')
    t.penup()
    t.goto(x, y)
    t.pendown
    if points == 4:
        angle = 90
    else:
        angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    print(x, y)
    for i in range (points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
    

# Paaohjelma
def tahtikirkasyo():
    t.Screen ().bgcolor('dark blue')

    ranPts = 4
    ranSize = 50
    ranCol = (random(), random(), random())
    ranX = 0
    ranY = 0
    draw_star (4, ranSize*10, ranCol, -225, 225)

    while True:
        ranPts = randint(2, 5) * 2 + 1
        ranSize = randint (10, 50)
        ranSizeMax = 50
        ranCol = (random(), random(), random())
        ranX = randint(-200, 200)
        ranY = randint(-200, 200)
        draw_star(ranPts, ranSize, ranCol, ranX, ranY)

        if runtest == 1:
            output = [ranX.real+ranSizeMax, ranY.real+ranSizeMax]
            return output
        
if runtest == 0:
    tahtikirkasyo()

# -m unittest tahtikirkas_yoTest
class test_tahtikirkasyo(unittest.TestCase):
    def test_tahtikirkas_yo_succsess(self):
        actual = tahtikirkasyo()
        expected_x = range(-250, 250)
        expected_y = range(-250, 250)
        try:
            print('actual = ', actual)
            self.assertIn(actual[0], expected_x)
            self.assertIn(actual[1], expected_y)
        except:
            print('testin kuloksessa virhe! x-koordinaatti ei sallittu ' + actual[0] + 'sallitut raja-arvot =' + expected_x)
            print('testin kuloksessa virhe! y-koordinaatti ei sallittu ' + actual[1] + 'sallitut raja-arvot =' + expected_y)
    