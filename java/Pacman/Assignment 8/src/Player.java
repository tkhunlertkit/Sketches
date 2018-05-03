import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import util.Depth;
import util.Direction;

public class Player extends DynamicEntity {
	private static Image imgN1, imgN2, imgS1, imgS2;
	private static Image imgE1, imgE2, imgW1, imgW2;

	static {
		try {
			imgN1 = ImageIO.read(new File("assets/pacman-n1.png"));
			imgN2 = ImageIO.read(new File("assets/pacman-n2.png"));
			imgS1 = ImageIO.read(new File("assets/pacman-s1.png"));
			imgS2 = ImageIO.read(new File("assets/pacman-s2.png"));
			imgE1 = ImageIO.read(new File("assets/pacman-e1.png"));
			imgE2 = ImageIO.read(new File("assets/pacman-e2.png"));
			imgW1 = ImageIO.read(new File("assets/pacman-w1.png"));
			imgW2 = ImageIO.read(new File("assets/pacman-w2.png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private int lastX;
	private int lastY;
	private int counter;

	public Player(GameContext context, int x, int y) {
		super(context, x, y, Depth.FRONT);
	}

	@Override
	public void update(Direction input) {
		move(input);
	}

	@Override
	public void touched(Entity other) {
		other.touchedPlayer(this);
	}

	@Override
	public void draw(Graphics g) {
		boolean animate = (lastX != getX() || lastY != getY()) && (counter++ % 20) > 10;

		Image img;
		if      (getFacing() == Direction.NORTH) img = animate ? imgN1 : imgN2;
		else if (getFacing() == Direction.SOUTH) img = animate ? imgS1 : imgS2;
		else if (getFacing() == Direction.WEST)  img = animate ? imgW1 : imgW2;
		else                                     img = animate ? imgE1 : imgE2;

		g.drawImage(img, getX(), getY(), null);
		lastX = getX();
		lastY = getY();
	}
}
