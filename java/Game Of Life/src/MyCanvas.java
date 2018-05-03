import java.awt.*;
import java.awt.image.BufferStrategy;

/**
 * Created by MSDK on 4/25/16.
 */
public class MyCanvas extends Canvas {

    private GameOfLife g;
    private int size;

    public MyCanvas(GameOfLife g, int size) {
        this.g = g;
        this.size = size;
        setSize(size, size);
    }

    public void render() {
        BufferStrategy bs = this.getBufferStrategy();

        if (bs == null) {
            this.createBufferStrategy(2);
            return;
        }

        do {
            do {
                Graphics2D g = (Graphics2D) bs.getDrawGraphics();
                render(g);
                g.dispose();
            } while (bs.contentsRestored());

            bs.show();
        } while (bs.contentsLost());
    }
    public void render(Graphics2D g2) {
        g2.setColor(Color.BLACK);
        g2.fillRect(0, 0, size + 200, size + 200);
        Point[][] points = this.g.getPoints();
        for (int i=0; i<this.g.getGridSize(); i++) {
            for (int j=0; j<this.g.getGridSize(); j++) {
                g2.setColor(points[i][j].isAlive() ? Color.WHITE : Color.BLACK);
                g2.fillRect(points[i][j].getX() * this.g.getCellSize(),
                            points[i][j].getY() * this.g.getCellSize(),
                            this.g.getCellSize(),
                            this.g.getCellSize());
            }
        }
    }

}

