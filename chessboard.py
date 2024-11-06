# Constants to define pieces and board setup
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

WHITE = 1
BLACK = -1

# Initialize the chessboard
class ChessBoard:
    def __init__(self):
        self.board = [
            [-ROOK, -KNIGHT, -BISHOP, -QUEEN, -KING, -BISHOP, -KNIGHT, -ROOK],
            [-PAWN] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [PAWN] * 8,
            [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        ]
        self.turn = WHITE  # White starts first
    
    def display_board(self):
        for row in self.board:
            print(" ".join([self.get_piece_symbol(piece) for piece in row]))
        print("\n")

    def get_piece_symbol(self, piece):
        # Represent pieces with symbols
        if piece == EMPTY:
            return "."
        symbol_map = {
            PAWN: 'P', KNIGHT: 'N', BISHOP: 'B',
            ROOK: 'R', QUEEN: 'Q', KING: 'K'
        }
        symbol = symbol_map[abs(piece)]
        return symbol if piece > 0 else symbol.lower()

# Instantiate and display the board
if __name__ == "__main__":
    board = ChessBoard()
    board.display_board()
