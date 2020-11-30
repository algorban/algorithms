from collections import deque
class CardGame:
    """
    Two players are playing a card game where the deck of cards are layed out in a straight line and each card value is
    visible to both the players.
    The value of each card can range from a reasonable [-ve to +ve] number and the length of deck in n.

    The rules of the game are such:

    Player 1 starts the game
    Each player has 3 option:
    (Option 1: Pick 1st card)
    (Option 2: Pick 1st two cards)
    (Option 3: Pick 1st three cards)
    You're only allowed to pick cards from the left side of the deck
    Both players have to play optimally.
    Return the maximum sum of cards Player 1 can obtain by playing optimally.

    Input: cards = [1, 1, 1, 1, 100]
    Output: 101
    Explanation:
    Turn 1: Player 1 picks cards[0] = 1 point
    Turn 2: Player 2 picks cards[1] + cards[2] + cards[3] = 3 points
    Turn 3: Player 1 picks cards[4] = 100 points
    """
    def find(self, cards):
        if not cards or len(cards) == 0:
            return 0

        N = len(cards)
        sum_ = 0
        dp = [0] * (N+3)
        for i in range(N-1, -1, -1):
            sum_ += cards[i]
            min_ = float("inf")
            for j in range(1, 4):
                if dp[i+j] < min_:
                    min_ = dp[i+j]
            dp[i] = sum_ - min_

        return dp[0]

    def find_constant_space(self, cards):
        N = len(cards)
        sum_ = 0
        dp = deque([0,0,0])
        for i in range(N-1, -1, -1):
            sum_ += cards[i]
            min_ = min(dp)
            dp.pop()
            dp.appendleft(sum_-min_)
        return dp[0]


if __name__ == '__main__':
    cg = CardGame()
    cards = [1,1,1,1,100]
    print(cg.find_constant_space(cards))