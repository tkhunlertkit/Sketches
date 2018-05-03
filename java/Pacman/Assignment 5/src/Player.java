import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import util.Depth;
import util.Direction;

public class Player extends DynamicEntity {
	
	private static Image PEC;
	private static Image PEO;
	private static Image PNC;
	private static Image PNO;	
	private static Image PWC;
	private static Image PWO;
	private static Image PSC;
	private static Image PSO;
	
	private int count;
	private int prev_x;
	private int prev_y;
	
	static {
		try {
			PEC = ImageIO.read(new File("pacman-e1.png"));
			PEO = ImageIO.read(new File("pacman-e2.png"));
			PNC = ImageIO.read(new File("pacman-n1.png"));
			PNO = ImageIO.read(new File("pacman-n2.png"));
			PWC = ImageIO.read(new File("pacman-w1.png"));
			PWO = ImageIO.read(new File("pacman-w2.png"));
			PSC = ImageIO.read(new File("pacman-s1.png"));
			PSO = ImageIO.read(new File("pacman-s2.png"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public Player(GameContext context, int x, int y) {
		super(context, x, y, Depth.FRONT);
		count = 0;
		prev_x = x;
		prev_y = y;
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
		
		if (getFacing() == Direction.NORTH) 
			g.drawImage(count % 20 < 10 ? PNO : PNC, getX(), getY(), null); 
		else if (getFacing() == Direction.WEST) 
			g.drawImage(count % 20 < 10 ? PWO : PWC, getX(), getY(), null); 
		else if (getFacing() == Direction.SOUTH) 
			g.drawImage(count % 20 < 10 ? PSO : PSC, getX(), getY(), null); 
		else 
			g.drawImage(count % 20 < 10 ? PEO : PEC, getX(), getY(), null); 
		if (prev_x != getX() || prev_y != getY()) {
			count++;
			prev_x = getX();
			prev_y = getY();
		}
		
	}
}
