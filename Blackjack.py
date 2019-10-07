import random
#This is a Blackjack game
class Players(object):
#This is the class that is for the player
    def __init__(Self_player):
        Self_player.Alive = True
        Self_player.Lost = False
        Self_player.Hand = []
        Self_player.Total = 0
        Self_player.Distance_away_from_goal = None

    def show_to_self(Self_player):
        return "%d: %s" % (Self_player.total, str(Self_player.hand))

    def update(Self_player):
        temp = 0
        for card in Self_player.Hand:
            temp += card[0]

        Self_player.total = temp

    def show(Self_player):
        if not Self_player.Lost:
            return "%s and %d more cards" % (Self_player.Hand[0], len(Self_player.Hand) - 1)
        else:
            return "%d: %s" % (Self_player.total, str(Self_player.Hand))


class Game(object):

#Description of what is consisted in the game, specifically the cards
    Suits = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    Cards_per_suit = 13
    Cards_in_deck = len(Suits) * Cards_per_suit
    Goal = 21

#The initiation of the game
    def __init__(Self_player, Number_of_Players):
        Self_player.Deck = [(value, Suit) for Suit in Self_player.Suits for value in list(range(1, Self_player.Cards_per_suit+1))]
        Self_player.Players = []
        Self_player.Possible_winners = []
        Self_player.Round = 0

        for x in range(Number_of_Players):
            p = Players()
            Self_player.Players.append(p)


#The cards being dealt
    def deal_cards(Self_player, Number_of_Cards, Player):
        if Player.Alive:
            for card in range(Number_of_Cards):
                c = Self_player.Deck[0]
                Player.Hand.append(c)
                Self_player.Deck.remove(c)

#The dealer asking the question to continue or to stop
    def response_handler(Self_player, Response, Player):
        if Response is 's':
            Player.Alive = False
        elif Response is 'c':
            Self_player.deal_cards(1, Player)
            print(Player.Hand[-1])
            Player.update()
        elif Response is 'l':
            print(Player.show_to_self())
            New_Response = input("Player %d: \'s\' to stop, \'c\' to continue, and \'l\' to look at your hand:" %
                                 (Self.players.index(Player) + 1))
            Self_player.response_handler(New_Response, Player)
        else:
            print("Not a valid response")
            New_Response = input("Player %d: \'s\' to stop, \'c\' to continue, and \'l\' to look at your hand:" %
                                 (Self_player.players.index(Player) + 1))
            Self_player.response_handler(New_Response, Player)

#Results of the game
    def final_score_handler(Self_player, Player):
        if Player.Lost:
            return "**lost** %d" % Player.Total
        else:
            score_board = sorted(self.possible_winners,
                                 key=lambda x: x.distance_away_from_goal)

            if Player is score_board[0]:
                return "**Winner** %d" % Player.Total

            else:
                return Player.Total

    def main(Self_player):

        random.shuffle(Self_player.Deck)

        for Player in Self_player.Players:
            Self_player.deal_cards(2, Player)
            Player.update()

        while True:

            Self_player.Round += 1
            Number_Alive = len(Self_player.Players)

            print("Round: %d" % Self_player.Round)

            for Player in Self_player.Players:
                print("Player %d: % s" %
                      (Self_player.Players.index(Player) + 1, Player.show()))

            for Player in Self_player.Players:

                if Player.Alive:

                    Response = input("Player %d: \'s\' to stop, \'c\' to continue, and \'l\' to look at your hand:" %
                                     (Self_player.Players.index(Player) + 1))

                    Self_player.response_handler(Response, Player)

                    if Player.Total > Self_player.Goal:
                        Player.Alive = False
                        Player.Lost = True
                        print("Player %d is out of the game" %
                              (Self_player.Players.index(Player) + 1))

                if not Player.Alive:
                    Number_Alive -= 1

            if Number_Alive is 0:
                break

        for Player in Self_player.Players:
            if not Player.Lost:
                Player.Distance_away_from_goal = Self_player.Goal - Player.Total
                Self_player.Possible_winners.append(Player)

        for Player in Self_player.Players:
            print("Player %d: %s" % (Self_player.Players.index(
                Player) + 1, Self_player.final_score_handler(Player)))


if __name__ == '__main__':
    g = Game(7)
    g.main()
