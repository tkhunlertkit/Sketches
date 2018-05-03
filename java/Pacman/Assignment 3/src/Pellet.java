import java.awt.Color;
import java.awt.Graphics;

import util.Depth;


public class Pellet extends StaticEntity {
	
	boolean large;
	
	public Pellet(int x, int y, boolean large) {
		super(x, y, Depth.MIDDLE);
		this.large = large; 
	}
	
	
	@Override
	public void draw(Graphics g) {
		int radius = (large) ? 7 : 3;
		int x = (getGridX() * Pacman.CELL_SIZE) + Pacman.CELL_SIZE / 2 - radius;
		int y = (getGridY() * Pacman.CELL_SIZE) + Pacman.CELL_SIZE / 2 - radius;
		g.setColor(Color.GREEN);
		g.fillOval(x, y, radius * 2, radius * 2);
	}

}
