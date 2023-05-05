import tkinter as tk


class CheckerPiece:
    def __init__(self, color, king=False):
        self.color = color
        self.king = king


class CheckerBoard(tk.Canvas):
    def __init__(self, parent, rows=8, columns=8, size=50, color1="white", color2="black"):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.current_piece = None
        self.turn = "red"
        canvas_width = columns * size
        canvas_height = rows * size

        super().__init__(parent, width=canvas_width, height=canvas_height, highlightthickness=0)

        self.create_board()
        self.create_pieces()

        self.bind("<Button-1>", self.on_square_click)

    def create_board(self):
        color = self.color2
        for y in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for x in range(self.columns):
                x1, y1 = x * self.size, y * self.size
                x2, y2 = x1 + self.size, y1 + self.size
                self.create_rectangle(x1, y1, x2, y2, fill=color, tags=f"{x},{y}")
                color = self.color1 if color == self.color2 else self.color2

    def create_pieces(self):
        for x in range(self.columns):
            for y in range(3):
                if (x + y) % 2 == 1:
                    self.create_piece(x, y, "red")
            for y in range(5, 8):
                if (x + y) % 2 == 1:
                    self.create_piece(x, y, "black")

    def create_piece(self, x, y, color):
        piece_id = self.create_oval(
            x * self.size + 5,
            y * self.size + 5,
            (x + 1) * self.size - 5,
            (y + 1) * self.size - 5,
            fill=color,
            tags=f"piece {x},{y}",
        )
        self.pieces[piece_id] = CheckerPiece(color)

    def on_square_click(self, event):
        x, y = event.x // self.size, event.y // self.size
        piece_id = self.find_withtag(f"piece {x},{y}")

        if piece_id:
            piece = self.pieces[piece_id[0]]
            if piece.color == self.turn:
                self.current_piece = piece_id[0]
        elif self.current_piece:
            piece = self.pieces[self.current_piece]
            old_x, old_y = [int(coord) for coord in self.gettags(self.current_piece)[1].split(",")]
            if self.is_valid_move(piece, old_x, old_y, x, y):
                self.move_piece(self.current_piece, old_x, old_y, x, y)
                self.turn = "black" if self.turn == "red" else "red"

    def is_valid_move(self, piece, old_x, old_y, x, y):
        move_distance = abs(old_x - x), abs(old_y - y)

        if move_distance not in [(1, 1), (2, 2)]:
            return False

        if move_distance == (2, 2):
            middle_piece_id = self.find_withtag(f"piece {old_x + (x - old_x)//2},{old_y + (y - old_y)//2}")

