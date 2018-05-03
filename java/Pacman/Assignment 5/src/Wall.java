import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import util.Depth;

public class Wall extends StaticEntity {
	
	private static Image wall;
	
	static {
		try {
			wall = ImageIO.read(new File("wall.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
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
		g.drawImage(wall, getGridX() * Pacman.CELL_SIZE, getGridY() * Pacman.CELL_SIZE, null);
	}
}
