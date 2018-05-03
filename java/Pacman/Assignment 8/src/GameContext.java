import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Timer;

/**
 * This class represents an in-progress game. It will hold the "global"
 * statistics about a game (such as the size of the level, a reference to the
 * entity bag, and scores).
 */
public class GameContext {
	private int w;
	private int h;
	private EntityBag entities;
	private Player player;
	private boolean paused;
	private int score;
	private int highScore;
	private boolean invincible;
	private boolean flashing;
	private Timer t1;
	private Timer t2;

	public GameContext(EntityBag entities) {
		this.entities = entities;
		invincible = false;
		flashing = false;
	}

	public EntityBag getEntities() {
		return entities;
	}

	public Player getPlayer() {
		return player;
	}

	public void setPlayer(Player player) {
		this.player = player;
	}

	public int getScore() {
		return score;
	}

	public int getHighScore() {
		return highScore;
	}

	public void setHighScore(int score) {
		this.highScore = score;
	}

	public void addScore(int points) {
		score += points;

		if (score > highScore) {
			highScore = score;
		}
	}

	/**
	 * Set the grid size of the current game.
	 * 
	 * @param w
	 *            The maximum x-grid coordinate.
	 * @param h
	 *            The maximum y-grid coordinate.
	 */
	public void setSize(int w, int h) {
		this.w = w;
		this.h = h;
	}

	/**
	 * Get the width of the game (in pixels).
	 * 
	 * @return The width.
	 */
	public int getW() {
		return w * Pacman.CELL_SIZE;
	}

	/**
	 * Get the height of the game (in pixels).
	 * 
	 * @return The height.
	 */
	public int getH() {
		return h * Pacman.CELL_SIZE;
	}

	/**
	 * Used to tell if the game is currently paused.
	 * 
	 * @return true if the game is currently paused and false otherwise
	 */
	public boolean isPaused() {
		return paused;
	}

	/**
	 * Pause the game.
	 */
	public void pause() {
		paused = true;
	}

	/**
	 * Unpause the game.
	 */
	public void resume() {
		paused = false;
	}
	
	public void pauseFor(int delay) {
		pause();
		Timer t = new Timer(delay, new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				resume();
			}
			
		});
		t.start();
		t.setRepeats(false);
	}
	
	public boolean isInvincible() {
		return invincible;
	}
	
	public boolean isFlashing() {
		return flashing;
	}
	
	public void setInvincible(int delay) {
		int firstTimer = delay * 3 / 4;
		int secondTimer = delay - firstTimer;
		
		invincible = true;
		flashing = false;
		if (t1 != null && t1.isRunning()) {
			t1.stop();
		}
		if (t2 != null && t2.isRunning()) {
			t2.stop();
		}
		t2 = new Timer(secondTimer, new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				flashing = false;
				invincible = false;
			}
		});
		
		t1 = new Timer(firstTimer, new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				flashing = true;
				
				t2.start();
				t2.setRepeats(false);
				
			}
		});
		t1.start();
		t1.setRepeats(false);
		
	}
}
