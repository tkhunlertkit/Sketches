import java.awt.Color;
import java.awt.Graphics;

import util.Depth;
import util.Direction;

public class Player extends Entity {
	// TODO - add instance variables
	private GameContext context;
	private int x;
	private int y;

	public Player(GameContext context, int x, int y) {
		// TODO - implement	// )#
		this.context = context;
		this.x = x*Pacman.CELL_SIZE;
		this.y = y*Pacman.CELL_SIZE;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY(){
		return y;
	}

	@Override
	public Depth getDepth() {
		// TODO - implement
		return Depth.FRONT;
	}

	@Override
	public void draw(Graphics g) {
		// TODO - implement
		g.setColor(Color.YELLOW);
		g.fillRect(x, y, Pacman.CELL_SIZE, Pacman.CELL_SIZE);
	}

	// TODO - add additional methods
	
	public void update(Direction input) {
		if (input == null) return;
		
		x += input.getDeltaX();
		y += input.getDeltaY();
		x = (x < 0) ? context.getW() - 1 : x % context.getW();
		y = (y < 0) ? context.getH() : y % context.getH();
	}
	
	// not sure what to do.
	public boolean equals(Graphics draw) {
		return false;
	}
}
