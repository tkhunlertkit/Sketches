import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import util.Depth;

public class Wall extends StaticEntity {
	private static Image img;

	static {
		try {
			img = ImageIO.read(new File("assets/wall.png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public Wall(int x, int y) {
		super(x, y, Depth.BACK);
	}

	public boolean isSolid() {
		return true;
	}

	@Override
	public void draw(Graphics g) {
		g.drawImage(img, getGridX() * Pacman.CELL_SIZE, getGridY() * Pacman.CELL_SIZE, null);
	}
}
