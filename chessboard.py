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
    
    # Helper function to check if a move is within the board limits
    def in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    # Move generation for pawns
    def generate_pawn_moves(self, row, col):
        moves = []
        direction = 1 if self.board[row][col] > 0 else -1
        # Move one step forward
        if self.in_bounds(row + direction, col) and self.board[row + direction][col] == EMPTY:
            moves.append((row + direction, col))
            # Move two steps forward from starting position
            if (row == 1 and direction == 1) or (row == 6 and direction == -1):
                if self.board[row + 2 * direction][col] == EMPTY:
                    moves.append((row + 2 * direction, col))
        # Capture diagonally
        for d_col in [-1, 1]:
            if self.in_bounds(row + direction, col + d_col):
                target = self.board[row + direction][col + d_col]
                if target != EMPTY and (target * self.board[row][col] < 0):
                    moves.append((row + direction, col + d_col))
        return moves

    # Move generation for rooks
    def generate_rook_moves(self, row, col):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d_row, d_col in directions:
            r, c = row + d_row, col + d_col
            while self.in_bounds(r, c):
                if self.board[r][c] == EMPTY:
                    moves.append((r, c))
                elif self.board[r][c] * self.board[row][col] < 0:
                    moves.append((r, c))
                    break
                else:
                    break
                r += d_row
                c += d_col
        return moves

    # Move generation for knights
    def generate_knight_moves(self, row, col):
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for d_row, d_col in knight_moves:
            r, c = row + d_row, col + d_col
            if self.in_bounds(r, c):
                if self.board[r][c] == EMPTY or self.board[r][c] * self.board[row][col] < 0:
                    moves.append((r, c))
        return moves

    # Wrapper function to get all legal moves for a given position
    def generate_moves(self, row, col):
        piece = abs(self.board[row][col])
        if piece == PAWN:
            return self.generate_pawn_moves(row, col)
        elif piece == ROOK:
            return self.generate_rook_moves(row, col)
        elif piece == KNIGHT:
            return self.generate_knight_moves(row, col)
        # Placeholder for other pieces
        return []

# Instantiate and display the board
if __name__ == "__main__":
    board = ChessBoard()
    board.display_board()
