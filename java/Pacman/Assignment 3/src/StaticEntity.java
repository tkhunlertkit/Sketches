import java.awt.Graphics;

import util.Depth;


public class StaticEntity extends Entity{

	private int x;
	private int y;
	private Depth depth;
	
	public StaticEntity(int x, int y, Depth depth) {
		this.x = x;
		this.y = y;
		this.depth = depth;
	}

	@Override
	public Depth getDepth() {
		return depth;
	}

	@Override
	public int getGridX() {
		return x;
	}

	@Override
	public int getGridY() {
		return y;
	}

	@Override
	public void draw(Graphics g) {
		// TODO Auto-generated method stub
		
	}
	
	public boolean isSolid() {
		return false;
	}

}
