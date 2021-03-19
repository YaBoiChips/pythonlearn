package chess;

import javax.swing.*;
import java.awt.*;

public class BoardFrame extends JFrame {
    Component component;
    public BoardFrame()
    {
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setTitle("chess.Chess");
        this.setResizable(false);
        component = new Board();
        this.add(component, BorderLayout.CENTER);

        this.setLocation(200, 50);
        this.pack();
        this.setVisible(true);
    }
}
