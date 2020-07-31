class Solution(object):
    """
    According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
    by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
    eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia
    article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state. The next state
    is created by applying the above rules simultaneously to every cell in the current state, where births and deaths
    occur simultaneously.
    """
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        def neighbors(r, c):
            res = []
            for mr, mc in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]:
                if -1 < r + mr < R and -1 < c + mc < C:
                    res.append((r + mr,c + mc))
            return res
        # 1 -> -1 died
        # 0 -> 2 alive
        for r in range(R):
            for c in range(C):
                live = 0
                nbs = 0
                for nr, nc in neighbors(r,c):
                    nbs += 1
                    if board[nr][nc] == 1 or board[nr][nc] == -1:
                        live += 1
                if live in [3] and board[r][c] == 0:
                    board[r][c] = 2
                elif board[r][c] == 1 and live < 2:
                    board[r][c] = -1
        for r in range(R):
            for c in range(C):
                if board[r][c] == -1:
                    board[r][c] = 0
                if board[r][c] == 2:
                    board[r][c] = 1
        return board





if __name__ == '__main__':
    s = Solution()
    board = [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
        ]
    print(s.gameOfLife(board))