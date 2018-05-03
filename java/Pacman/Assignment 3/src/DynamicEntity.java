import java.awt.Graphics;

import util.Depth;
import util.Direction;

public class DynamicEntity extends Entity {
	
	private GameContext context;
	private int x;
	private int y;
	private Direction facing;
	private Depth depth;
	
	public DynamicEntity(GameContext context, int x, int y, Depth depth) {
		this.context = context;
		this.x = x * Pacman.CELL_SIZE;
		this.y = y * Pacman.CELL_SIZE;
		this.depth = depth;
	}
	
	@Override
	public int getGridX() {
		return (x + Pacman.CELL_SIZE / 2) / Pacman.CELL_SIZE;
	}

	@Override
	public int getGridY() {
		return (y + Pacman.CELL_SIZE / 2) / Pacman.CELL_SIZE;
	}

	@Override
	public Depth getDepth() {
		return depth;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	public Direction getFacing() {
		return facing;
	}
	
	public GameContext getContext() {
		return context;
	}
	
	public void move(Direction d) {
		
	}
	
	public void setX(int x) {
		this.x = x;
	}
	
	public void setY(int y) {
		this.y = y;
	}
	
	public void setFacing(Direction facing) {
		this.facing = facing;
	}

	/**
	 * Determines if moving in the given direction will keep the player aligned
	 * on the grid.
	 * 
	 * @param direction
	 *            The player's facing.
	 * @return true if the player is on the grid, false otherwise
	 */
	protected boolean isOnGrid(Direction direction) {
		int dx = direction.getDeltaX();
		int dy = direction.getDeltaY();

		return (x + dx) % Pacman.CELL_SIZE == 0
				|| (y + dy) % Pacman.CELL_SIZE == 0;
	}

	/**
	 * Determines if the next block in the direction of movement is blocked.
	 * 
	 * @param direction
	 *            The player's facing
	 * @return true if the player will collide with this facing on the next
	 *         update
	 */
	protected boolean isTargetBlocked(Direction direction) {
		// Get delta x and y
		int dx = direction.getDeltaX();
		int dy = direction.getDeltaY();

		// Get center point x and y
		int cx = x + Pacman.CELL_SIZE / 2;
		int cy = y + Pacman.CELL_SIZE / 2;

		// Get the pixel coordinates of the leading edge
		int nx = cx + dx * Pacman.CELL_SIZE / 2 - (dx < 0 ? 1 : 0);
		int ny = cy + dy * Pacman.CELL_SIZE / 2 - (dy < 0 ? 1 : 0);

		// Wrap and convert to grid coordinates
		int tx = wrap(nx, context.getW()) / Pacman.CELL_SIZE;
		int ty = wrap(ny, context.getH()) / Pacman.CELL_SIZE;

		// Determine if blocked
		return context.getEntities().isBlocked(tx, ty);
	}

	protected int wrap(int val, int max) {
		return (val < 0) ? (val + max) : (val % max);
	}

	@Override
	public void draw(Graphics g) {
		// TODO Auto-generated method stub
	}
	
}
