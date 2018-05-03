import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import util.Depth;
import util.Direction;

public class Ghost extends DynamicEntity {
	private static Image img;
	private static Image blue;
	private static Image flash;
	static {
		try {
			img = ImageIO.read(new File("assets/ghost.png"));
			flash = ImageIO.read(new File("assets/flashing.png"));
			blue = ImageIO.read(new File("assets/scatter.png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	private int count;
	
	public Ghost(GameContext context, int x, int y) {
		super(context, x, y, Depth.FRONT);
		count = 0;
	}

	@Override
	public void update(Direction input) {
		move(atIntersection() ? chooseFacing() : getFacing());
	}

	/**
	 * Determine if the ghost is at an intersection (has the possibility of
	 * choice).
	 * 
	 * @return true if the ghost is at an intersection, false otherwise
	 */
	private boolean atIntersection() {
		return getX() % Pacman.CELL_SIZE == 0 && getY() % Pacman.CELL_SIZE == 0;
	}

	/**
	 * Choose a new facing according to the ghost's AI. This implementation
	 * chooses a the "closest" non-blocked direction with respect to the
	 * player's current position. This will only choose the "backwards"
	 * direction of the current facing if the ghost is at a dead-end.
	 * 
	 * @return The "best" direction.
	 */
	private Direction chooseFacing() {
		Player p = getContext().getPlayer();

		int tx = p.getGridX();
		int ty = p.getGridY();

		int cost = getContext().isInvincible() ? Integer.MIN_VALUE : Integer.MAX_VALUE;
		Direction best = Direction.NORTH;

		for (Direction d : Direction.values()) {
			int x = getGridX() + d.getDeltaX();
			int y = getGridY() + d.getDeltaY();

			int c = Math.abs(tx - x) + Math.abs(ty - y);

			if (!getContext().isInvincible() && d.opposite() == getFacing()) {
				c += getContext().getW() + getContext().getH();
			}

			
			if (!getContext().isInvincible() && !this.isTargetBlocked(d) && c < cost) {
				cost = c;
				best = d;
			}
			if (getContext().isInvincible() && !this.isTargetBlocked(d) && c > cost) {
				cost = c;
				best = d;
			}
		}

		return best;
	}
	
	@Override
	public void touchedPlayer(Player player) {
		getContext().pauseFor(1000);
		if (getContext().isInvincible()) {
			getContext().getEntities().removeEntity(this);
			getContext().addScore(200);
		} else {
			getContext().getEntities().removeEntity(player);
		}
	}

	@Override
	public void draw(Graphics g) {
		Image i = img;
		if (getContext().isInvincible()) 
			if (getContext().isFlashing()) {
				i = count % 20 < 10 ? flash : blue;
				count++;
			} else {
				i = blue;
			}
		g.drawImage(i, getX(), getY(), null);
	}
}