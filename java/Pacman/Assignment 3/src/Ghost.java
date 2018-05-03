import java.awt.Color;
import java.awt.Graphics;

import util.Depth;
import util.Direction;

public class Ghost extends DynamicEntity {

	public Ghost(GameContext context, int x, int y) {
		super(context, x, y, Depth.FRONT);
		setFacing(Direction.NORTH);
	}

	@Override
	public void draw(Graphics g) {
		g.setColor(Color.PINK);
		g.fillRect(getX(), getY(), Pacman.CELL_SIZE, Pacman.CELL_SIZE);
	}

	@Override
	public void update(Direction input) {
		Player p = super.getContext().getPlayer();
		int dx = p.getGridX() - this.getGridX();
		int dy = p.getGridY() - this.getGridY();
		if (Math.abs(dx) > Math.abs(dy))
			input = (dx > 0) ? Direction.EAST : Direction.WEST;
		else
			input = (dy > 0) ? Direction.SOUTH : Direction.NORTH;
//		do {
//			int rand = (int) (Math.random() * 4);
//			switch (rand) {
//			case 0:
//				input = Direction.NORTH;
//				break;
//			case 1:
//				input = Direction.SOUTH;
//				break;
//			case 2:
//				input = Direction.EAST;
//				break;
//			default:
//				input = Direction.WEST;
//			}
//		} while (input == getFacing().opposite());

		if (!isOnGrid(input) || isTargetBlocked(input)) {
			input = getFacing();
		}

		if (input == null || !isOnGrid(input) || isTargetBlocked(input)) {
			return;
		}

		setFacing(input);

		setX(wrap(getX() + input.getDeltaX(), getContext().getW()));
		setY(wrap(getY() + input.getDeltaY(), getContext().getH()));
	}

	private Player findPlayer() {
		return super.getContext().getPlayer();
	}

}
