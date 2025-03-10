# Alex Miller
# BlackJack

import random, sys 

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    money = 5000
    while True:
        if money <= 0:
            PrintStyle('You\'re broke! play again? (y/n)')
            m = input().upper()
            if m == 'Y':
                main()
            else:
                PrintStyle('Goodbye')
                sys.exit()

        PrintStyle('Money: {}'.format(makeNormal(money)))
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        PrintStyle('Bet: {}'.format(makeNormal(bet)))
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break
            
            move = getMove(playerHand, money - bet)
            if move =='D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                PrintStyle('Bet increased to {}'.format(makeNormal(bet)))
                PrintStyle('Bet: {}'.format(bet))

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                PrintStyle('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            PrintStyle('Dealer busts! you win ${}!'.format(makeNormal(bet)))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            PrintStyle('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            PrintStyle('You won ${}!'.format(makeNormal(bet)))
            money += bet
        elif playerValue == dealerValue:
            PrintStyle('It\'s a tie, the bet is returned to you')
        
        print()
        input('Press Enter to coninue...')
        ClearScreen()
    
def ClearScreen():
    for i in range(50):
        print()

def getBet(maxBet):
    while True:
        PrintStyle('How much do you bet? (1-{} or QUIT)'.format(makeNormal(maxBet)))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            PrintStyle('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def PrintStyle(t):
    print()
    print('='*50)
    print()
    print(t)
    print()
    print('='*50)
    print()

def PrintStyle2(t):
    print()
    print('`'*50)
    print()
    print(t)
    print()
    print('`'*50)
    print()

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        PrintStyle2('DEALER: {}'.format(getHandValue(dealerHand)))
        displayCards(dealerHand)
    else:
        PrintStyle2('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    
    PrintStyle2('PLAYER: {}'.format(getHandValue(playerHand)))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    
    return value

def displayCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    
    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        movePrompt = ', '.join(moves) + '> '
        PrintStyle((movePrompt).upper())
        move = input('> ').upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

def makeNormal(money):
    m = str(money)
    s = ''
    t = ''
    Amounts = {
        '1000': '1',
        '10000': '1',
        '100000': '1',
        '1000000': '2',
        '10000000': '2',
        '100000000': '2',
        '1000000000': '3',
        '10000000000': '3',
        '100000000000': '3'
    }
    for i in Amounts.keys():
        if len(i) == len(m):
            t = str(Amounts.get(i, 0))
            break
    
    if t == '1':
        if len(m) == 4:
            s += m[0]
            s += ','
            for i in range(1,4):
                s += m[i]
            return s
        elif len(m) == 5:
            s += m[0]
            s += m[1]
            s += ','
            for i in range(2,5):
                s += m[i]
            return s
        else:
            for i in range(3):
                s += m[i]
            s += ','
            for i in range(3,6):
                s += m[i]
            return s
    elif t == 2:
        if len(m) == 7:
            s += m[0]
            s += ','
            for i in range(1,4):
                s += m[i]
            s += ','
            for i in range(5,7):
                s += m[i]
            return s
    else:
        return money
    

        

if __name__ == '__main__':
    main()