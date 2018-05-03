import javax.swing.*;
import java.awt.*;

/**
 * Created by MSDK on 4/25/16.
 */
public class GameOfLife extends JFrame {

    private int windowSize = 700;
    private int canvasSize = 500;
    private int gridSize = 200;
    private int cellSize = (canvasSize / gridSize) + 1;
    private int aliveThreshold = 10;
    private Point[][] points;
    private MyCanvas c;
    private boolean wrapped;
    private int fps = 20;


    public GameOfLife(boolean wrapped) {
        this.wrapped = wrapped;
        int size = gridSize * cellSize;

        initialize();
        setSize(windowSize, windowSize);
        setTitle("Game Of Life");
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        GraphicsDevice gd = GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice();
        int width = gd.getDisplayMode().getWidth();
        int height = gd.getDisplayMode().getHeight();
        setLocation((width - size) / 2, (height - size) / 2);

        JSlider framesPerSecond = new JSlider(JSlider.HORIZONTAL, 0, 1000, fps);
        framesPerSecond.setMajorTickSpacing(200);
        framesPerSecond.setMinorTickSpacing(50);
        framesPerSecond.setPaintTicks(true);
        framesPerSecond.setPaintLabels(true);
        framesPerSecond.addChangeListener(e -> {
            fps = framesPerSecond.getValue();
        });

        JSlider numGrid = new JSlider(JSlider.HORIZONTAL, 0, 500, gridSize);
        numGrid.setMajorTickSpacing(100);
        numGrid.setMinorTickSpacing(25);
        numGrid.setPaintTicks(true);
        numGrid.setPaintLabels(true);
        numGrid.addChangeListener(e -> {
            gridSize = numGrid.getValue();
            cellSize = (canvasSize / gridSize) + 1;
            c.setBackground(Color.BLACK);
            initialize();
            System.out.println(c.getSize().width + " x " + c.getSize().height);
            System.out.println(cellSize + " x " + gridSize + " = " + (cellSize * gridSize));
        });

        JSlider threshold = new JSlider(JSlider.HORIZONTAL, 0, 100, aliveThreshold);
        threshold.setMajorTickSpacing(25);
        threshold.setMinorTickSpacing(5);
        threshold.setPaintTicks(true);
        threshold.setPaintLabels(true);
        threshold.addChangeListener(e -> {
            aliveThreshold = threshold.getValue();
            initialize();
        });

        c = new MyCanvas(this, canvasSize);
        add(c);
        JPanel top = new JPanel();
        top.add(new JLabel("FPS:"));
        top.add(framesPerSecond);
        top.add(new JLabel("Cells:"));
        top.add(numGrid);
        add(top, BorderLayout.NORTH);
        add(threshold, BorderLayout.SOUTH);

        setVisible(true);
        new Thread(() -> {
           while(true) {
               try {
                   if (fps != 0) {
                       update();
                       Thread.sleep(1000 / fps);
                   }
                   Thread.yield();
               } catch (InterruptedException e) {
                   e.printStackTrace();
               } catch (Exception e) {
                   e.printStackTrace();
               }
           }
        }).start();
    }

    public void initialize() {

        points = new Point[gridSize][gridSize];
            for (int i = 0; i < gridSize; i++) {
                for (int j = 0; j < gridSize; j++) {
                    points[i][j] = new Point(i, j, (double)aliveThreshold / 100);
                }
            }
    }

    public void update() {
        Point[][] cloned = new Point[gridSize][gridSize];
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                cloned[i][j] = new Point(i, j, points[i][j].isAlive());
            }
        }
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                if (wrapped) changeStateUnwrapped(cloned, points[i][j]);
                else changeState(cloned, points[i][j]);

            }
        }

        c.render();
    }

    private boolean changeStateUnwrapped(Point[][] cloned, Point point) {
        boolean wasAlive = point.isAlive();
        int numAliveNeighbors = 0;
        int i = point.getX();
        int j = point.getY();

        if (i - 1 >= 0) {
            if (cloned[(i - 1)][j].isAlive()) numAliveNeighbors++;
            if (j - 1 >= 0 && cloned[(i - 1)][(j - 1)].isAlive()) numAliveNeighbors++;
            if (j + 1 < gridSize && cloned[(i - 1)][(j + 1)].isAlive()) numAliveNeighbors++;
        }

        if (j - 1 >= 0 && cloned[i][(j-1)].isAlive()) numAliveNeighbors++;
        if (j + 1 < gridSize && cloned[i][(j+1)].isAlive()) numAliveNeighbors++;

        if (i + 1 < gridSize) {
            if (cloned[(i + 1)][j].isAlive()) numAliveNeighbors++;
            if (j - 1 >= 0 && cloned[(i + 1)][(j - 1)].isAlive()) numAliveNeighbors++;
            if (j + 1 < gridSize && cloned[(i + 1)][(j + 1)].isAlive()) numAliveNeighbors++;
        }

        if (numAliveNeighbors == 3) {
            point.setAlive();
        } else if (numAliveNeighbors != 2) {
            point.setDead();
        }

        return wasAlive != point.isAlive();
    }

    private boolean changeState(Point[][] cloned, Point point) {
        boolean wasAlive = point.isAlive();
        int numAliveNeighbors = 0;
        int i = point.getX() + gridSize;
        int j = point.getY() + gridSize;

        if (cloned[(i-1) % gridSize][j % gridSize].isAlive()) numAliveNeighbors++;
        if (cloned[(i-1) % gridSize][(j-1) % gridSize].isAlive()) numAliveNeighbors++;
        if (cloned[(i-1) % gridSize][(j+1) % gridSize].isAlive()) numAliveNeighbors++;

        if (cloned[i % gridSize][(j-1) % gridSize].isAlive()) numAliveNeighbors++;
        if (cloned[i % gridSize][(j+1) % gridSize].isAlive()) numAliveNeighbors++;

        if (cloned[(i+1) % gridSize][j % gridSize].isAlive()) numAliveNeighbors++;
        if (cloned[(i+1) % gridSize][(j-1) % gridSize].isAlive()) numAliveNeighbors++;
        if (cloned[(i+1) % gridSize][(j+1) % gridSize].isAlive()) numAliveNeighbors++;

        if (numAliveNeighbors == 3) {
            point.setAlive();
        } else if (numAliveNeighbors != 2) {
            point.setDead();
        }

        return wasAlive != point.isAlive();
    }

    public int getGridSize() {
        return this.gridSize;
    }

    public int getCellSize() {
        return cellSize;
    }

    public Point[][] getPoints() {
        return points.clone();
    }

}
