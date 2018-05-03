import java.awt.Color;
import java.awt.Graphics;

import util.Depth;

public class Wall extends Entity {
	private int gridX; 
	private int gridY;
	
	public Wall(int x, int y) {
		gridX = x;
		gridY = y;
	}
	
	public int getGridX() {
		return gridX;
	}
	
	public int getGridY(){
		return gridY;
	}
	
	public Depth getDepth(){
		return Depth.BACK;
	}
	
	@Override
	public boolean isSolid(){
		return true;
	}
	
	@Override
	public void draw(Graphics g) {
		int x = gridX * Pacman.CELL_SIZE;
		int y = gridY * Pacman.CELL_SIZE;
		g.setColor(Color.GREEN);
		g.fillRect(x, y, Pacman.CELL_SIZE, Pacman.CELL_SIZE);
	}
	
	// + equals(draw : Graphics) ?
}
