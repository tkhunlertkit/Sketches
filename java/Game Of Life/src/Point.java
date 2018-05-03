/**
 * Created by MSDK on 4/25/16.
 */
public class Point {
    private int i;
    private int j;
    private boolean alive;

    public Point(int i, int j, boolean alive) {
        this.i = i;
        this.j = j;
        this.alive = alive;
    }

    public Point(int i, int j, double threshold) {
        this(i, j, Math.random() < threshold ? true : false);
    }


    public boolean isAlive() {
        return alive;
    }

    public int getX() {
        return i;
    }

    public int getY() {
        return j;
    }

    public void setAlive() {
        alive = true;
    }

    public void setDead() {
        alive = false;
    }
}
