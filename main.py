from random import randint as rand
import pygame as pg

Screen = pg.display.set_mode((1080, 720))

Dice = 20
Data = [0] * (6 * Dice)
BinWidth = 1080//(Dice*6-Dice+1)

while True:
    for event in pg.event.get():
        pass
    for i in range(1):
        Rolls = []

        [Rolls.append(rand(1, 6)) for a in range(Dice)]

        Data[sum(Rolls) - (Dice - 1)] += 1

    for x in range(Dice, Dice * 6 + 1):
        Percent = (Data[x - (Dice - 1)] / sum(Data))
        pg.draw.rect(Screen, [255]*3, [(x-Dice)*BinWidth, 720-(Percent * 720*5), BinWidth, (Percent * 720 * 5)])

    pg.display.flip()
    Screen.fill([0]*3)