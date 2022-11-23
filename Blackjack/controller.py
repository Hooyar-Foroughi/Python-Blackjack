import random, copy, turtle
from time import sleep
import functools
import sys, os

def initializeBoard(wn, turtles):
    
    wn.setup(width=1400, height=960)
    turtle.bgcolor("dark green")
    turtles[0].color("black")
    turtles[0].speed(0)
    turtles[0].penup()
    turtles[0].sety(280)
    turtles[0].pendown()
    turtles[0].write("BLACK JACK", align="center", font=("Felix Titling", 80, "bold"))
    turtles[0].penup()
    turtles[0].width(2)
    turtles[0].sety(290)
    turtles[0].setx(-285)
    turtles[0].pendown()
    turtles[0].forward(570)
    turtles[4].penup()
    turtles[4].sety(210)
    turtles[4].setx(-505)
    turtles[4].width(75)
    turtles[4].color("navy")
    turtles[4].speed(0)
    turtles[4].pendown()
    turtles[4].forward(1000)
    turtles[4].right(90)
    turtles[4].forward(360)
    turtles[4].right(90)
    turtles[4].forward(1000)
    turtles[4].right(90)
    turtles[4].forward(360)
    turtles[4].right(135)
    turtles[4].forward(50)
    turtles[4].left(45)
    turtles[4].color("maroon")
    turtles[4].fillcolor("maroon")
    turtles[4].begin_fill()
    turtles[4].forward(930)
    turtles[4].right(90)
    turtles[4].forward(285)
    turtles[4].right(90)
    turtles[4].forward(930)
    turtles[4].right(90)
    turtles[4].forward(285)
    turtles[4].end_fill()
    turtles[1].color("white")
    turtles[1].speed(0)
    turtles[1].penup()
    turtles[1].sety(-20)
    turtles[1].pendown()
    turtles[1].write("Press enter to begin", align="center", font=("Monotype Corsiva", 75))
    turtles[3].speed(0)
    turtles[5].speed(0)
    turtles[6].speed(0)
    turtles[7].speed(0)
    wn.addshape("CB.gif")

def getDeck():
    
    return [("Ace of Hearts", 11, "AH.gif"), ("2 of Hearts", 2, "2H.gif"), \
         ("3 of Hearts", 3, "3H.gif"), ("4 of Hearts", 4, "4H.gif"), \
         ("5 of Hearts", 5, "5H.gif"), ("6 of Hearts", 6, "6H.gif"), \
         ("7 of Hearts", 7, "7H.gif"), ("8 of Hearts", 8, "8H.gif"), \
         ("9 of Hearts", 9, "9H.gif"), ("10 of Hearts", 10, "10H.gif"), \
         ("Jack of Hearts", 10, "JH.gif"), ("Queen of Hearts", 10, "QH.gif"), \
         ("King of Hearts", 10, "KH.gif"), ("Ace of Spades", 11, "AS.gif"), \
         ("2 of Spades", 2, "2S.gif"), ("3 of Spades", 3, "3S.gif"), \
         ("4 of Spades", 4, "4S.gif"), ("5 of Spades", 5, "5S.gif"), \
         ("6 of Spades", 6, "6S.gif"), ("7 of Spades", 7, "7S.gif"), \
         ("8 of Spades", 8, "8S.gif"), ("9 of Spades", 9, "9S.gif"), \
         ("10 of Spades", 10, "10S.gif"), ("Jack of Spades", 10, "JS.gif"), \
         ("Queen of Spades", 10, "QS.gif"), ("King of Spades", 10, "KS.gif"), \
         ("Ace of Diamonds", 11, "AD.gif"), ("2 of Diamonds", 2, "2D.gif"), \
         ("3 of Diamonds", 3, "3D.gif"), ("4 of Diamonds", 4, "4D.gif"), \
         ("5 of Diamonds", 5, "5D.gif"), ("6 of Diamonds", 6, "6D.gif"), \
         ("7 of Diamonds", 7, "7D.gif"), ("8 of Diamonds", 8, "8D.gif"), \
         ("9 of Diamonds", 9, "9D.gif"), ("10 of Diamonds", 10, "10D.gif"), \
         ("Jack of Diamonds", 10, "JD.gif"), ("Queen of Diamonds", 10, "QD.gif"), \
         ("King of Diamonds", 10, "KD.gif"), ("Ace of Clubs", 11, "AC.gif"), \
         ("2 of Clubs", 2, "2C.gif"), ("3 of Clubs", 3, "3C.gif"), \
         ("4 of Clubs", 4, "4C.gif"), ("5 of Clubs", 5, "5C.gif"), \
         ("6 of Clubs", 6, "6C.gif"), ("7 of Clubs", 7, "7C.gif"), \
         ("8 of Clubs", 8, "8C.gif"), ("9 of Clubs", 9, "9C.gif"), \
         ("10 of Clubs", 10, "10C.gif"), ("Jack of Clubs", 10, "JC.gif"), \
         ("Queen of Clubs", 10, "QC.gif"), ("King of Clubs", 10, "KC.gif")]


def exitGame(wn):
    
    wn.bye()
    sys.exit()

def ReturnClick(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):
    
    wn.onkeypress(None, 'Return')
    turtles[1].clear()
    start(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)


def reset_turtles(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):
    
    turtles[1].clear()
    turtles[2].clear()
    turtles[3].clear()
    turtles[5].clear()
    turtles[6].clear()

    cards[0].clear()
    cards[1].clear()
    cards[2].clear()
    cards[3].clear()
    cards[4].clear()
    cards[5].clear()
    cards[6].clear()
    cards[7].clear()
    cards[8].clear()
    cards[9].clear()

    cards_on_table = []
    
    for turtle in card_turtles:
        turtle.hideturtle()
        turtle.penup()

    for turtle in card_turtles1:
        turtle.hideturtle()
        turtle.penup()

    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    pdeck = getDeck()
    in_game = True
    start(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)


def create_card_image_player(wn, player_hand, cards_on_table, card_turtles):

  for card in player_hand:
    if card in cards_on_table:
      continue
    else:
      wn.addshape(card[2])
      card_turtles[(len(player_hand)-1)].showturtle()
      card_turtles[(len(player_hand)-1)].shape(card[2])

      cards_on_table.append(card)


def create_card_image_dealer(wn, dealer_hand, cards_on_table, card_turtles1):

    for card in dealer_hand:
        if card in cards_on_table:
            continue
        else:
            wn.addshape(card[2])
            card_turtles1[(len(dealer_hand)-1)].showturtle()
            card_turtles1[(len(dealer_hand)-1)].shape(card[2])

            cards_on_table.append(card)


def draw_card(deck):
    
    drawn_card = random.choice(deck)
    deck.remove(drawn_card)
    return drawn_card


def compute_score(hand):
    
    total = 0
    value_set = []

    for card in hand:
        value_set.append(card[1])

    total = sum(value_set)
    ace_check = True
    
    while ace_check == True:
        
        if total > 21 and 11 in value_set:
            value_set.remove(11)
            value_set.append(1)
            total = sum(value_set)

        else:
            ace_check = False

    return total


def cards_in_hand(hand):
    
    cardNames = []

    for card in hand:
        cardNames.append(card[0])

    handString = cardNames[0]

    for name in cardNames[1:]:
        handString = handString + ', ' + name

    return handString


def hit(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):

            player_hand.append(draw_card(pdeck))
            create_card_image_player(wn, player_hand, cards_on_table, card_turtles)
            player_score = compute_score(player_hand)

            if player_score > 21:

                turtles[1].clear()
                turtles[1].write("Current hand: " + cards_in_hand(player_hand), align="center",
                         font=("Copperplate Gothic Bold", 33))
                turtles[3].clear()
                turtles[3].write("Score: " + str(player_score), align="center", font=("Arial Black", 25))
                turtles[5].clear()
                turtles[5].write("Oh no!  You went bust!", align="center", font=("Copperplate Gothic Bold", 29))
                player_wins = False
                in_game = False
                wn.onkeypress(None, 'h')
                wn.onkeypress(None, 's')
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)

            elif len(player_hand) > 4:

                turtles[5].clear()
                turtles[5].write("Wow!  You got a 'Five Card Charlie'!  You Win!", align="center",
                         font=("Copperplate Gothic Bold", 29))
                player_wins = True
                in_game = False
                wn.onkeypress(None, 'h')
                wn.onkeypress(None, 's')
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)


            else:

                turtles[1].clear()
                turtles[1].write("Current hand: " + cards_in_hand(player_hand), align="center",
                         font=("Copperplate Gothic Bold", 34))
                turtles[3].clear()
                turtles[3].write("Score: " + str(player_score), align="center", font=("Arial Black", 25))


def stay(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):

            wn.onkeypress(None, 'h')
            wn.onkeypress(None, 's')
            turtles[5].clear()
            turtles[5].write("The dealer will now draw", align="center", font=("Copperplate Gothic Bold", 29))
            sleep(.3)
            turtles[5].penup()
            turtles[5].forward(160)
            turtles[5].pendown()
            turtles[5].write(".", align="center", font=("Copperplate Gothic Bold", 29))
            sleep(.3)
            turtles[5].penup()
            turtles[5].forward(8)
            turtles[5].pendown()
            turtles[5].write(".", align="center", font=("Copperplate Gothic Bold", 29))
            sleep(.3)
            turtles[5].penup()
            turtles[5].forward(8)
            turtles[5].pendown()
            turtles[5].write(".", align="center", font=("Copperplate Gothic Bold", 29))
            sleep(.3)
            turtles[5].penup()
            turtles[5].forward(8)
            turtles[5].pendown()
            turtles[5].write(".", align="center", font=("Copperplate Gothic Bold", 29))
            turtles[5].penup()
            turtles[5].setx(0)
            turtles[5].sety(0)
            turtles[5].pendown()
            dealer_hand.append(draw_card(pdeck))
            create_card_image_dealer(wn, dealer_hand, cards_on_table, card_turtles1)
            dealer_score = compute_score(dealer_hand)
            turtles[6].penup()
            turtles[6].sety(185)
            turtles[6].pendown()
            turtles[6].color("white")
            turtles[6].write("The dealer's hand is: " + cards_in_hand(dealer_hand), align="center",
                     font=("Copperplate Gothic Bold", 16))
            turtles[6].penup()
            turtles[6].sety(150)
            turtles[6].pendown()
            turtles[6].write("The dealer's score is: " + str(dealer_score), align="center",
                     font=("Copperplate Gothic Bold", 20))

            player_score = compute_score(player_hand)
            dealer_score = compute_score(dealer_hand)
             
            if dealer_score < 17:
                
                sleep(1.5)
                card_turtles1[(len(dealer_hand))].showturtle()
                turtles[6].clear()
                stay(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)

            elif dealer_score > 21:

                turtles[5].clear()
                turtles[5].write("The dealer went bust!  You win!", align="center", font=("Copperplate Gothic Bold", 29))
                player_wins = True
                in_game = False
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)

            elif len(dealer_hand) > 4:

                turtles[5].clear()
                turtles[5].write("The dealer got a 'Five Card Charlie'.  You lose!", align="center",
                         font=("Copperplate Gothic Bold", 29))
                player_wins = False
                in_game = False
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)

            elif dealer_score >= player_score:
                
                turtles[5].clear()
                turtles[5].write("The dealer beat you!  You lose!", align="center", font=("Copperplate Gothic Bold", 29))
                player_wins = False
                in_game = False
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)

            else:

                turtles[5].clear()
                turtles[5].write("You beat the dealer!  You win!", align="center", font=("Copperplate Gothic Bold", 29))
                player_wins = True
                in_game = False
                postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak)


def postAction(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):
    
    if player_wins == True:

        turtles[7].clear()
        winstreak += 1
        wstr = str(winstreak)
        turtles[7].penup()
        turtles[7].sety(340)
        turtles[7].setx(425)
        turtles[7].pendown()
        turtles[7].color("yellow")
        turtles[7].write("Win Streak: " + wstr, font=("Arial Black", 21))

    else:
        
        winstreak = 0
        turtles[7].clear()

    turtles[1].clear()
    turtles[1].color("red")
    turtles[1].write("GAME OVER  -  Press 'Enter' to play again or 'q' to quit", align="center",
             font=("Copperplate Gothic Bold", 33, "bold"))
    wn.onkeypress(functools.partial(reset_turtles, wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak), 'Return')
    wn.onkeypress(functools.partial(exitGame, wn), 'q')
    wn.listen()

            
def start(wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak):

    cards[0].hideturtle()
    cards[0].penup()
    cards[0].setx(-50)
    cards[0].sety(-75)
    cards[0].pendown()
    cards[0].shape("CB.gif")
    cards[0].showturtle()

    cards[1].hideturtle()
    cards[1].penup()
    cards[1].setx(0)
    cards[1].sety(-75)
    cards[1].pendown()
    cards[1].shape("CB.gif")
    cards[1].showturtle()

    cards[2].hideturtle()
    cards[2].penup()
    cards[2].setx(50)
    cards[2].sety(-75)
    cards[2].pendown()
    cards[2].shape("CB.gif")

    cards[3].hideturtle()
    cards[3].penup()
    cards[3].setx(100)
    cards[3].sety(-75)
    cards[3].pendown()
    cards[3].shape("CB.gif")

    cards[4].hideturtle()
    cards[4].penup()
    cards[4].setx(150)
    cards[4].sety(-75)
    cards[4].pendown()
    cards[4].shape("CB.gif")

    cards[5].hideturtle()
    cards[5].penup()
    cards[5].setx(-50)
    cards[5].sety(110)
    cards[5].pendown()
    cards[5].shape("CB.gif")
    cards[5].showturtle()

    cards[6].hideturtle()
    cards[6].penup()
    cards[6].setx(0)
    cards[6].sety(110)
    cards[6].pendown()
    cards[6].shape("CB.gif")
    cards[6].showturtle()
    
    cards[7].hideturtle()
    cards[7].penup()
    cards[7].setx(50)
    cards[7].sety(110)
    cards[7].pendown()
    cards[7].shape("CB.gif")

    cards[8].hideturtle()
    cards[8].penup()
    cards[8].setx(100)
    cards[8].sety(110)
    cards[8].pendown()
    cards[8].shape("CB.gif")

    cards[9].hideturtle()
    cards[9].penup()
    cards[9].setx(150)
    cards[9].sety(110)
    cards[9].pendown()
    cards[9].shape("CB.gif")

    player_hand.append(draw_card(pdeck))
    create_card_image_player(wn, player_hand, cards_on_table, card_turtles)
    player_hand.append(draw_card(pdeck))
    create_card_image_player(wn, player_hand, cards_on_table, card_turtles)
    player_score = compute_score(player_hand)

    dealer_hand.append(draw_card(pdeck))
    create_card_image_dealer(wn, dealer_hand, cards_on_table, card_turtles1)
    dealer_score = compute_score(dealer_hand)

    turtles[2].penup()
    turtles[2].sety(-265)
    turtles[2].setx(-1000)
    turtles[2].speed(0)
    turtles[2].width(8)
    turtles[2].pendown()
    turtles[2].forward(2000)
    turtles[1].penup()
    turtles[1].sety(-340)
    turtles[1].pendown()
    turtles[1].color("orange")
    turtles[1].write("Starting hand: " + cards_in_hand(player_hand), align="center", font=("Copperplate Gothic Bold", 39))
    turtles[3].penup()
    turtles[3].sety(-250)
    turtles[3].pendown()
    turtles[3].color("orange")
    turtles[3].write("Score: " + str(player_score), align="center", font=("Arial Black", 25))

    while in_game:
        
        turtles[5].penup()
        turtles[5].sety(0)
        turtles[5].pendown()
        turtles[5].color("white")
        turtles[5].write("Would you like to draw a card? ('h' for hit, 's' for stay)", align="center",
                 font=("Copperplate Gothic Bold", 26))

        wn.onkeypress(None, 'Return')
        wn.onkeypress(functools.partial(hit, wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak), 'h')
        wn.onkeypress(functools.partial(stay, wn, turtles, cards, player_hand, player_score, dealer_hand, dealer_score,
                          pdeck, in_game, cards_on_table, card_turtles, card_turtles1, player_wins, winstreak), 's')
        wn.listen()
        wn.mainloop()


