package chess;

import chess.dice.Die;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class Board extends JComponent {
    private static Image NULL_IMAGE = new BufferedImage(10, 10, BufferedImage.TYPE_INT_ARGB);

    private final int SQUARE_WIDTH = 65;
    public ArrayList<Die> BLUE_DIE;
    public ArrayList<Die> RED_DIE;

    public Integer[][] BOARD_GRID;
    public ArrayList<DrawingShape> STATIC_SHAPES;
    public ArrayList<DrawingShape> PEICE_GRAPHICS;
    private final int rows = 8;
    private final int cols = 8;
    private String board_file_path = "images/board.png";


    public void initGrid() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                BOARD_GRID[i][j] = 0;
            }
        }

    }

    public Board() {

        BOARD_GRID = new Integer[rows][cols];
        STATIC_SHAPES = new ArrayList();
        PEICE_GRAPHICS = new ArrayList();

        this.setBackground(new Color(37,13,84));
        this.setPreferredSize(new Dimension(520, 520));
        this.setMinimumSize(new Dimension(100, 100));
        this.setMaximumSize(new Dimension(1000, 1000));

        this.setVisible(true);
        this.requestFocus();
        drawBoard();
    }

    public void drawBoard(){
        STATIC_SHAPES.clear();
        PEICE_GRAPHICS.clear();

        Image board = loadImage(board_file_path);
        STATIC_SHAPES.add(new DrawingImage(board, new Rectangle2D.Double(0, 0, board.getWidth(null), board.getHeight(null))));
        this.repaint();
    }

    private Image loadImage(String imageFile) {
        try {
            return ImageIO.read(new File(imageFile));
        }
        catch (IOException e) {
            return NULL_IMAGE;
        }
    }

    public interface DrawingShape {
        boolean contains(Graphics2D g2, double x, double y);
        void adjustPosition(double dx, double dy);
        void draw(Graphics2D g2);
    }


    class DrawingImage implements DrawingShape {

        public Image image;
        public Rectangle2D rect;

        public DrawingImage(Image image, Rectangle2D rect) {
            this.image = image;
            this.rect = rect;
        }

        @Override
        public boolean contains(Graphics2D g2, double x, double y) {
            return rect.contains(x, y);
        }

        @Override
        public void adjustPosition(double dx, double dy) {
            rect.setRect(rect.getX() + dx, rect.getY() + dy, rect.getWidth(), rect.getHeight());
        }

        @Override
        public void draw(Graphics2D g2) {
            Rectangle2D bounds = rect.getBounds2D();
            g2.drawImage(image, (int)bounds.getMinX(), (int)bounds.getMinY(), (int)bounds.getMaxX(), (int)bounds.getMaxY(),
                    0, 0, image.getWidth(null), image.getHeight(null), null);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {

        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D)g;
        drawBackground(g2);
        drawShapes(g2);
    }

    private void drawBackground(Graphics2D g2) {
        g2.setColor(getBackground());
        g2.fillRect(0,  0, getWidth(), getHeight());
    }


    private void drawShapes(Graphics2D g2) {
        for (DrawingShape shape : STATIC_SHAPES) {
            shape.draw(g2);
        }
        for (DrawingShape shape : PEICE_GRAPHICS) {
            shape.draw(g2);
        }
    }
    public Die getPiece(int x, int y) {
        for (Die p : RED_DIE)
        {
            if (p.getX() == x && p.getY() == y)
            {
                return p;
            }
        }
        for (Die p : BLUE_DIE)
        {
            if (p.getX() == x && p.getY() == y)
            {
                return p;
            }
        }
        return null;
    }

    private MouseAdapter mouseAdapter = new MouseAdapter() {

        @Override
        public void mouseClicked(MouseEvent e) {


        }

        @Override
        public void mousePressed(MouseEvent e) {
            int d_X = e.getX();
            int d_Y = e.getY();
            int Clicked_Row = d_Y / Square_Width;
            int Clicked_Column = d_X / Square_Width;
            boolean is_whites_turn = true;
            if (turnCounter%2 == 1)
            {
                is_whites_turn = false;
            }

            Piece clicked_piece = getPiece(Clicked_Column, Clicked_Row);

            if (Active_Piece == null && clicked_piece != null &&
                    ((is_whites_turn && clicked_piece.isWhite()) || (!is_whites_turn && clicked_piece.isBlack())))
            {
                Active_Piece = clicked_piece;
            }
            else if (Active_Piece != null && Active_Piece.getX() == Clicked_Column && Active_Piece.getY() == Clicked_Row)
            {
                Active_Piece = null;
            }
            else if (Active_Piece != null && Active_Piece.canMove(Clicked_Column, Clicked_Row)
                    && ((is_whites_turn && Active_Piece.isWhite()) || (!is_whites_turn && Active_Piece.isBlack())))
            {
                // if piece is there, remove it so we can be there
                if (clicked_piece != null)
                {
                    if (clicked_piece.isWhite())
                    {
                        White_Pieces.remove(clicked_piece);
                    }
                    else
                    {
                        Black_Pieces.remove(clicked_piece);
                    }
                }
                // do move
                Active_Piece.setX(Clicked_Column);
                Active_Piece.setY(Clicked_Row);

                // if piece is a pawn set has_moved to true
                if (Active_Piece.getClass().equals(Pawn.class))
                {
                    Pawn castedPawn = (Pawn)(Active_Piece);
                    castedPawn.setHasMoved(true);
                }


                Active_Piece = null;
                turnCounter++;
            }

            drawBoard();
        }

        @Override
        public void mouseDragged(MouseEvent e) {
        }

        @Override
        public void mouseReleased(MouseEvent e) {
        }

        @Override
        public void mouseWheelMoved(MouseWheelEvent e)
        {
        }


    };

    private void adjustShapePositions(double dx, double dy) {

        STATIC_SHAPES.get(0).adjustPosition(dx, dy);
        this.repaint();

    }

    private ComponentAdapter componentAdapter = new ComponentAdapter() {

        @Override
        public void componentHidden(ComponentEvent e) {

        }

        @Override
        public void componentMoved(ComponentEvent e) {

        }

        @Override
        public void componentResized(ComponentEvent e) {

        }

        @Override
        public void componentShown(ComponentEvent e) {

        }
    };

    private KeyAdapter keyAdapter = new KeyAdapter() {

        @Override
        public void keyPressed(KeyEvent e) {

        }

        @Override
        public void keyReleased(KeyEvent e) {

        }

        @Override
        public void keyTyped(KeyEvent e) {

        }
    };

}
}
