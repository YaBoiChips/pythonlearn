package chess;

public class Chess {

    public BoardFrame boardframe;
    public static void main(String[] args){
        Chess gui = new Chess();
        gui.boardframe = new BoardFrame();
        gui.boardframe.setVisible(true);
    }
}
