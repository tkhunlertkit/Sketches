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

	public GameContext(EntityBag entities) {
		this.entities = entities;
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

	public int getScore() {
		return score;
	}

	public void addScore(int increment) {
		this.score = score + increment;
		if (score > this.highScore) {
			highScore = score;
		}
	}

	public int getHighScore() {
		return highScore;
	}

	public void setHighScore(int highScore) {
		this.highScore = highScore;
	}
}
