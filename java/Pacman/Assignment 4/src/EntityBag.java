import java.util.ArrayList;
import java.util.List;

import util.Depth;



/**
 * A simple bag (unordered list) of entities. This bag has a maximum of 500
 * entities (for now) which should be enough for basic testing purposes.
 */
public class EntityBag {

	/**
	 * A static array to hold entities, and the array's effective size.
	 */
	private List<Entity> entities; 

	public EntityBag() {
		entities = new ArrayList<Entity>();
	}

	/**
	 * Return a copy of the entity array. Since we can't also pass back an
	 * effective size, we only make the returned array (exactly) as big as
	 * necessary.
	 * 
	 * @return A copy of the entity array.
	 */
	public List<Entity> getAllEntities() {
		List<Entity> e = new ArrayList<Entity>();
		e.addAll(entities);
		return e;
	}

	/**
	 * Add an entity to the bag.
	 * 
	 * @param e
	 *            The entity to add.
	 */
	public void addEntity(Entity e) {
		entities.add(e);
	}

	/**
	 * Determine if there is a blocking entity at grid coordinate (x, y).
	 * 
	 * @param x
	 *            The x-coordinate.
	 * @param y
	 *            The y-coordinate.
	 * @return true if (x, y) is blocked, false otherwise
	 */
	public boolean isBlocked(int x, int y) {
		for (Entity e: getAllEntities()) {
			if (e.getGridX() == x && e.getGridY() == y && e.isSolid()) {
				return true;
			}
		}

		return false;
	}
	public void removeEntity(Entity e) {
		for (int i=0; i<entities.size(); ++i) {
			if (entities.get(i).equals(e)) {
				entities.remove(i);
				return;
			}
		}
	}
	
	public List<Entity> getEntitiesAtDepth(Depth depth) { 
		List<Entity> e = new ArrayList<>();
		for (Entity en: getAllEntities()) {
			if (en.getDepth() == depth) {
				e.add(en);
			}
		}
		return e;
	}
	
	public void onMove(Entity e) { 
		for (Entity en: getAllEntities()) {
			if (e != en && en.getGridX() == e.getGridX() && en.getGridY() == e.getGridY()) {
				e.touched(en);
				en.touched(e);
			}
		}
	}
}
