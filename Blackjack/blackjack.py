import random, copy, turtle
from time import sleep
import sys, os
import functools
from controller import initializeBoard, getDeck, ReturnClick

def main():
    
    imagePath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images/'))
    os.chdir(imagePath)

    odeck = getDeck()
    pdeck = copy.copy(odeck)

    wn = turtle.Screen()
    t = turtle.Turtle()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    t6 = turtle.Turtle()
    t7 = turtle.Turtle()

    t.hideturtle()
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t5.hideturtle()
    t6.hideturtle()
    t7.hideturtle()
    t.hideturtle()

    card_1 = turtle.Turtle()
    card_2 = turtle.Turtle()
    card_3 = turtle.Turtle()
    card_4 = turtle.Turtle()
    card_5 = turtle.Turtle()
    card_6 = turtle.Turtle()
    card_7 = turtle.Turtle()
    card_8 = turtle.Turtle()
    card_9 = turtle.Turtle()
    card_10 = turtle.Turtle()

    card_1.speed(0)
    card_2.speed(0)
    card_3.speed(0)
    card_4.speed(0)
    card_5.speed(0)
    card_6.speed(0)
    card_7.speed(0)
    card_8.speed(0)
    card_9.speed(0)
    card_10.speed(0)

    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    winstreak = 0
    cards_on_table = []
    card_turtles = [card_1, card_2, card_3, card_4, card_5,]
    card_turtles1 = [card_6, card_7, card_8, card_9, card_10]
    in_game = True
    player_wins = None
    turtles = [t, t1, t2, t3, t4, t5, t6, t7]
    cards = [card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10]

    initializeBoard(wn, turtles)
    wn.onkeypress(functools.partial(ReturnClick, wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                              pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak), 'Return')
    wn.listen()


if __name__ == "__main__":
    
    main()
