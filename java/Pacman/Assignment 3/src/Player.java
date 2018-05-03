import java.awt.Color;
import java.awt.Graphics;

import util.Depth;
import util.Direction;

public class Player extends DynamicEntity {
	

	public Player(GameContext context, int x, int y) {
		super(context, x, y, Depth.FRONT);
	}

	@Override
	public void draw(Graphics g) {
		g.setColor(Color.YELLOW);
		g.fillRect(getX(), getY(), Pacman.CELL_SIZE, Pacman.CELL_SIZE);
	}
	
	@Override
	public void update(Direction input) {
		if (input == null) {
			return;
		}

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
	
}
