import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class LevelLoader {
	private GameContext context;

	public LevelLoader(GameContext context) {
		this.context = context;
	}

	public void clear() {
		context.setSize(0, 0);
		context.setPlayer(null);

		for (Entity e : context.getEntities().getAllEntities()) {
			context.getEntities().removeEntity(e);
		}
	}

	public void load(File file) {
		clear();

		try (Scanner s = new Scanner(file)) {
			int x = 0;
			int w = 0;
			int y = 0;
			int g = 0;

			while (s.hasNextLine()) {
				x = 0;

				for (char c : s.nextLine().toCharArray()) {
					switch (c) {
					case ' ':
						break;

					case '#':
						context.getEntities().addEntity(new Wall(x, y));
						break;

					case '.':
						context.getEntities().addEntity(new Pellet(context, x, y, false));
						break;

					case 'o':
						context.getEntities().addEntity(new Pellet(context, x, y, true));
						break;

					case '*':
						if (context.getPlayer() != null) {
							throw new RuntimeException("Too many players in file.");
						}

						Player player = new Player(context, x, y);
						context.setPlayer(player);
						context.getEntities().addEntity(player);
						break;

					case '^':
						g++;
						context.getEntities().addEntity(new Ghost(context, x, y));
						break;

					default:
						throw new RuntimeException(String.format("Unrecognized character `%s`.\n", c));
					}

					x++;
				}

				y = y + 1;
				w = Math.max(w, x);
			}

			if (context.getPlayer() == null) {
				throw new RuntimeException("No players in file.");
			}

			if (g < 2) {
				throw new RuntimeException("Too few ghosts in file.");
			}

			if (g > 2) {
				throw new RuntimeException("Too many ghosts in file.");
			}
			
			context.setSize(w, y);
		} catch (IOException ex) {
			throw new RuntimeException("Could not open file.");
		}
	}
}
