class Board:
    def __init__(self):
        self.board = [[None] * 9, [None] * 9, [None] * 9, [None] * 9]

    def xy_to_index(self, x, y):
        firstrow = x // 3
        secondrow = y // 3

        rowindex = firstrow + 2 * secondrow

        blockX = x % 3
        blockY = y % 3

        blockindex = blockX + 3 * blockY

        return rowindex, blockindex

    def get_color(self, x, y):
        rowindex, blockindex = self.xy_to_index(x, y)
        return self.board[rowindex][blockindex]

    def place(self, x, y, color):
        rowindex, blockindex = self.xy_to_index(x, y)

        if self.board[rowindex][blockindex] is not None:
            return False

        self.board[rowindex][blockindex] = color
        return True

    def rotate(self, block_index, rotation):

        for i in range(rotation):
            block = self.board[block_index].copy()
            for x in range(3):
                for y in range(3):
                    block[x + y * 3] = self.board[block_index][2 - y + x * 3]
            self.board[block_index] = block

    def __str__(self):
        res = ""
        for y in range(6):
            for x in range(6):
                rowindex, blockindex = self.xy_to_index(x, y)

                color = self.board[rowindex][blockindex]
                res += color if color is not None else '-'
            res += '\n'
        return res


class Gamelogic:
    def __init__(self):
        self.player = ["X", "Y"]
        self.turn = 0
        self.board = Board()
        self.board.place(0, 3, "X")
        self.board.place(0, 4, "X")
        self.board.place(0, 5, "X")
        self.board.place(1, 5, "X")
        self.board.place(2, 5, "X")
        self.board.place(1, 0, "Y")
        self.board.place(2, 1, "Y")
        self.board.place(3, 0, "Y")
        self.board.place(4, 3, "Y")
        self.board.place(5, 4, "Y")

    def move(self, x, y, rblock, rotation):
        if self.board.place(x, y, self.player[self.turn]):
            self.board.rotate(rblock, rotation)
            self.turn = 1 - self.turn
            return True
        else:
            return False

    def check_for_five(self):
        winners = {"X" : 0, "Y" : 0, None: 0}
        countrow = 0
        countcol = 0
        for i in range(6):
            for j in range(5):
                if self.board.get_color(i, j) == self.board.get_color(i, j+1):
                    countrow += 1
                    if countrow == 4:
                        winners[self.board.get_color(i, j)] += 1
                        countrow = 0
                else:
                    countrow = 0

                if self.board.get_color(j, i) == self.board.get_color(j + 1, i):
                    countcol += 1
                    if countcol == 4:
                        winners[self.board.get_color(j, i)] += 1
                        countcol = 0
                else:
                    countcol = 0

        d1 = 0
        d2 = 0
        for i in range(5):
            if self.board.get_color(i, i) == self.board.get_color(i + 1, i + 1):
                d1 += 1
                if d1 == 4:
                    winners[self.board.get_color(i, i)] += 1
                    d1 = 0
            else:
                d1 = 0

            if self.board.get_color(i, 5-i) == self.board.get_color(i + 1, 5-i - 1):
                d2 += 1
                if d2 == 4:
                    winners[self.board.get_color(i, 5-i)] += 1
                    d2 = 0
            else:
                d2 = 0

        d1 = 0
        d2 = 0
        d3 = 0
        d4 = 0
        for i in range(4):
            if self.board.get_color(i + 1, i) == self.board.get_color(i + 2, i + 1):
                d1 += 1
                if d1 == 4:
                    winners[self.board.get_color(i + 1, i)] += 1
                    d1 = 0

            if self.board.get_color(i, i + 1) == self.board.get_color(i + 1, i + 2):
                d2 += 1
                if d2 == 4:
                    winners[self.board.get_color(i, i + 1)] += 1
                    d2 = 0

            if self.board.get_color(i, 4 - i) == self.board.get_color(i + 1, 4 - (i + 1)):
                d3 += 1
                if d3 == 4:
                    winners[self.board.get_color(i, 4 - i)] += 1
                    d3 = 0

            if self.board.get_color(i + 1, 5 - i) == self.board.get_color(i + 2, 5 - (i + 1)):
                d4 += 1
                if d4 == 4:
                    winners[self.board.get_color(i + 1, 5 - i)] += 1
                    d4 = 0

        if winners["X"] > winners["Y"]:
            return "X"
        elif winners["X"] < winners["Y"]:
            return "Y"
        elif 0 < winners["X"] == winners["Y"]:
            return ["X", "Y"]
        else:
            return None

    def run(self):
        while self.check_for_five() is None:
            print(self.board)
            x = int(input("Enter x"))
            y = int(input("Enter y"))
            blockindex = int(input("Enter blockindex"))
            rotation = int(input("Enter rotation"))
            self.move(x, y, blockindex, rotation)

        print("################")
        print(self.board)
        print(self.check_for_five())



game = Gamelogic()
game.run()