package chess.dice;


import chess.Board;

public class Die{
    private int x;
    private int y;
    final private boolean is_red;
    private String file_path;
    public Board board;

    public Die(int x, int y, boolean is_red, String file_path, Board board){
        this.x = x;
        this.y = y;
        this.file_path = file_path;
        this.is_red = is_red;
        this.board = board;
    }
    public String getFilePath(){return file_path;}

    public void setFilePath(String path) {this.file_path = path;}

    public boolean isRed(){return is_red;}
    public boolean isBlue(){return !is_red;}

    public void setX(int x)
    {
        this.x = x;
    }

    public void setY(int y)
    {
        this.y = y;
    }

    public int getX()
    {
        return x;
    }

    public int getY()
    {
        return y;
    }

    public boolean canMove(int destination_x, int destination_y)
    {
        return false;
    }
}

