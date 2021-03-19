package chess.dice;

import chess.Board;

public class OneDice extends Die{
    public OneDice(int x, int y, boolean is_red, String file_path, Board board) {
        super(x, y, is_red, file_path, board);
    }

    @Override
    public boolean canMove(int destination_x, int destination_y) {
        return super.canMove(destination_x, destination_y);
    }
}
