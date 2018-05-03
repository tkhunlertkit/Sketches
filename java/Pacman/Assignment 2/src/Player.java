import java.awt.Color;
import java.awt.Graphics;

import util.Depth;
import util.Direction;

public class Player extends Entity {
	private GameContext context;
	private int x;
	private int y;
	private Direction facing = null;

	public Player(GameContext context, int x, int y) {
		this.context = context;
		this.x = x * Pacman.CELL_SIZE;
		this.y = y * Pacman.CELL_SIZE;
	}

	@Override
	public Depth getDepth() {
		return Depth.FRONT;
	}

	@Override
	public void draw(Graphics g) {
		g.setColor(Color.YELLOW);
		g.fillRect(x, y, Pacman.CELL_SIZE, Pacman.CELL_SIZE);
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	@Override
	public void update(Direction input) {
		boolean blocked = true;
		if (input == null) {
			return;
		}
		Direction prev = facing;
		if (x % Pacman.CELL_SIZE == 0 && y % Pacman.CELL_SIZE == 0) {
			facing = input;
		}
		
		if (facing.getDeltaX() != 0 && input.getDeltaX() != 0) {
			facing = input;
		}
		
		if (facing.getDeltaY() != 0 && input.getDeltaY() != 0) {
			facing = input;
		}
		
		
		int nextX = getNextPoint(x, facing.getDeltaX(), context.getW());
		int nextY = getNextPoint(y, facing.getDeltaY(), context.getH());
		if (context.getEntities().isBlocked(nextX, nextY)) {
			blocked = true;
		} 
		if (!checkBlocked(facing)){
			x = wrap(x + facing.getDeltaX(), context.getW());
			y = wrap(y + facing.getDeltaY(), context.getH());
			blocked = false;
		}
		if (blocked && !checkBlocked(prev)) {
				facing = prev;
				x = wrap(x + facing.getDeltaX(), context.getW());
				y = wrap(y + facing.getDeltaY(), context.getH());
		}
	}
	
	private boolean checkBlocked(Direction d) {
		if (d == null) return true;
		boolean blocked = false;
		int nextX = getNextPoint(x, d.getDeltaX(), context.getW());
		int nextY = getNextPoint(y, d.getDeltaY(), context.getH());
		if (context.getEntities().isBlocked(nextX, nextY)) {
			blocked = true;
		}
		return blocked;
	}
	
	private int getNextPoint(int val, int direction, int max) {
		int nextVal = wrap(val + direction, max);
		return ((nextVal + ((direction == 1) ? Pacman.CELL_SIZE - 1 : 0)) / Pacman.CELL_SIZE);
	}

	private int wrap(int val, int max) {
		return (val < 0) ? (val + max) : (val % max);
	}

	@Override
	public int getGridX() {
		return (x + (Pacman.CELL_SIZE / 2)) / Pacman.CELL_SIZE;
	}

	@Override
	public int getGridY() {
		return (y + (Pacman.CELL_SIZE / 2)) / Pacman.CELL_SIZE;
	}
}
