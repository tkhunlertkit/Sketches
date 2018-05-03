import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class LevelLoader {
	
	private GameContext context;
	
	public LevelLoader(GameContext context) {
		this.context = context;
	}

	public void clear() {
		for (Entity e: context.getEntities().getAllEntities()) {
			context.getEntities().removeEntity(e);
		}
	}
	
	public void load(File file) throws RuntimeException {
		try  (Scanner s = new Scanner(file)) {
//			2. An unknown character is encountered while parsing 
//			3.  
//			4. There are fewer/more than two ghosts on the grid
			int row = 0; 
			int col = 0;
			int pacman = 0;
			int ghost = 0;
			while (s.hasNextLine()) {
				String str = s.nextLine();
				for (col=0; col<str.length(); col++) {
					char c = str.charAt(col);
					switch(c){
					case '#':
						context.getEntities().addEntity(new Wall(col, row));
						break;
					case '.':
						context.getEntities().addEntity(new Pellet(context, col, row, false));
						break;
					case 'o':
						context.getEntities().addEntity(new Pellet(context, col, row, true));
						break;
					case '*':
						Player p = new Player(context, col, row);
						context.getEntities().addEntity(p);
						context.setPlayer(p);
						pacman++;
						break;
					case '^':
						context.getEntities().addEntity(new Ghost(context, col, row));
						ghost++;
						break;
					case ' ':
						break;
					default:
						throw new RuntimeException("An unknown character is encountered while parsing");
							
					}
				}
				row++;
			}
			context.setSize(col, row);
			if (pacman < 1) {
				throw new RuntimeException("There are fewer than one player on the grid");
			}
			if (pacman > 1) {
				throw new RuntimeException("There are more than one player on the grid");
			}
			if (ghost > 2) {
				throw new RuntimeException("There are more than two ghosts on the grid");
			}
			if (ghost < 2) {
				throw new RuntimeException("There are fewer than two ghosts on the grid");
			}
		} catch (FileNotFoundException f) {
			throw new RuntimeException("Input file does not exist or is not readable");
		}
	}
}
