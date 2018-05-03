import java.util.Calendar;
import javax.swing.*;
public class ShowTime {
   public static void main(String[] args) {
      JFrame f = new JFrame();
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setTitle("It's Showtime!");
      f.getContentPane().add(new JLabel(
         Calendar.getInstance().getTime().toString()));
      f.pack();
      f.setVisible(true);
   }
}
