from art import logo
from random import *
from replit import clear

clear()
print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

print(logo)
print("Your cards: [11, 1], current score: 12")
print("Computer's first card: 9")
print("Type 'y' to get another card, type 'n' to pass: ")
print("Your cards: [11, 1, 7], current score: 19")
print("Computer's first card: 9")
print("Type 'y' to get another card, type 'n' to pass: ")
print("Your final hand: [11, 1, 7], final score: 19")
print("Computer's final hand: [9, 10], final score: 19")
print("Draw.")
print("You win.")
print("You went over. You lose.")
print("Opponent went over. You win.")
print("You lose.")
print("You win with a Blackjack")
print("You lose, opponent has a Blackjack")

# https://www.youtube.com/watch?v=XYgdLMcPspo
#
# exchange money for chips
# bet chips in betting area
# hands are dealt:
#  player face up, dealer face up
#  player face up, dealer face down
# j,q,k = 10
# a = 1,11
# * = face value 
#object of game, for player to get closer to 21 than the dealer without going over 21. best way = blackjack, first two cards are an ace and 10
# blackjack auto-pays amount of their bet plus a bonus - blackjack typically pays 3:2, which means you get 1.5x your bet. blackjacks never lose, they only push
# if player and dealer get blackjack, then the hand will be pushed, and the player gets no money, but they keep their original bet
# if dealer has blackjack and player has any other hand. player auto-loses bet
# casinos offer 6:5 blackjack instead of 3:2 blackjack, but it's smarter for player to choose 3:2 as they get paid more
#
#if no blackjack on first hand, then have to work:
# if original cards are 17-21, then you would stay
#   shake hand back and forth
# if orig cards 2-17, they may decide to hit
#  drag two fingers on table towards themselves
#   bust, means went over 21
#ace = soft total
# if orig cards 9-11, they may double down
#    player puts up an add'l bet equal to their orig bet
#    if player wins, wins both bets
#    if lose, lose both bets
#    after requesting double down, player gets 1 and only
#    1 card, no more cards afterwards
#    finger pointing at the double down bet
# if orig cards are the same face value, they may split
#    split two fingers on table near bet
#    dealer splits the original two cards and bets
#    now player is playing two hands instead of one
#    player is allowed to hit, double down or split again
#   but can only play one hand at a time  (bust or stay)
#  can split up to 3 times, or up to 4 hands
#   if splitting aces, only gets one card for each hand
#   and if you get a 10, that's not a blackjack
##blackjack strategy card
# if dealer hace ace showing, can bet insurance or bet that
#   dealer has a blackjack as a side bet of 50% the orig # 
#   bet which pays 2:1
#   if dealer no blackjack, then lose the insurance bet
# if player has blackjack, then can take even money
#   same as insurance, but don't get the 50% bonus
#   for their blackjack, this prevents the hand
#   being a push if both have blackjacks
#once players go, dealer goes
#dealer only hit,stay
#hit while 16 or lower
#stay at 17 or higher
#bust if going over 21
#some casino's stay,hit on soft 17
#player double's bet on win
#loses bet on loss
#and on draw it's a push, neither win nor lose bet

#surrender, is when player believes they'll lose, they
# get half their bet

# changing money, dealer wishes good luck



## chips at casinos
#1,*2, 5, 10, 20, 25, 50, 100, 250, 500, 1000, 2000, 5000
#* - rare
## basic chips
#1, *2.50, 5, 10, 25, 100
#* - rare, sometimes in blackjack
##### https://www.youtube.com/watch?v=WZlMO2SFpm4
#### red,green,black below are always the same:::
###
#0.50 - real $0.50 piece, 1 - white, 5 - red, 25 - green
#100 - black, 500 - purple
##
## greens are cut in 4's, all else is cut in 5's

# 6 decks are used, now the way they're shuffled
# is not random


### calc odds of diff hands: ie: blackjack

