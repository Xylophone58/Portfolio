//Zach Mitchell 700726936

#include "chess.h"
#include <stdio.h>

void printSquare(const Square *square) {
    char pieceSymbol;

    switch (square->piece) {
        case EMPTY:
            pieceSymbol = '*';
            break;
        case PAWN:
            pieceSymbol = (square->color == BLACK) ? 'P' : 'p';
            break;
        case KNIGHT:
            pieceSymbol = (square->color == BLACK) ? 'N' : 'n';
            break;
        case BISHOP:
            pieceSymbol = (square->color == BLACK) ? 'B' : 'b';
            break;
        case ROOK:
            pieceSymbol = (square->color == BLACK) ? 'R' : 'r';
            break;
        case QUEEN:
            pieceSymbol = (square->color == BLACK) ? 'Q' : 'q';
            break;
        case KING:
            pieceSymbol = (square->color == BLACK) ? 'K' : 'k';
            break;
        default:
            // Handle invalid piece type (optional)
            pieceSymbol = '?';
            break;
    }

    printf("%c", pieceSymbol);
}
