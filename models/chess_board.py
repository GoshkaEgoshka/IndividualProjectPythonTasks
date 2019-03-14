class ChessBoard:
    def __init__(self, width: int, height: int):
        self.chess_board_width = width
        self.chess_board_height = height

    def chess_board_display(self) -> None:
        self.chess_board_width = int(self.chess_board_width / 2)

        for i in range(self.chess_board_height):
            if i % 2 > 0:
                print(u"\u2592\u2592\u2588\u2588" * self.chess_board_width)
            else:
                print(u"\u2588\u2588\u2592\u2592" * self.chess_board_width)
