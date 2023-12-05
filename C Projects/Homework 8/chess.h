//Zach Mitchell 700726936

#ifndef CHESS_H
#define CHESS_H

// Enumerated type for the piece on a square
typedef enum {
    EMPTY,
    PAWN,
    KNIGHT,
    BISHOP,
    ROOK,
    QUEEN,
    KING
} Piece;

// Enumerated type for the color of a piece
typedef enum {
    BLACK,
    WHITE
} Color;

// Structure type to represent a square on the chessboard
typedef struct {
    Piece piece;
    Color color;
} Square;

// Prototype for the printSquare function
void printSquare(const Square *square);

#endif /* CHESS_H */