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
        self.board.place(0, 0, "X")
        self.board.place(1, 1, "X")
        self.board.place(2, 2, "X")
        self.board.place(4, 4, "X")
        self.board.place(5, 3, "X")
        self.board.place(5, 1, "Y")
        self.board.place(5, 2, "Y")
        self.board.place(5, 5, "Y")
        self.board.place(4, 5, "Y")
        self.board.place(3, 5, "Y")

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