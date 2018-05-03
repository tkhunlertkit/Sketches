import java.util.Scanner;


public class PayItForward {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter depth level: ");
		double d = s.nextDouble();
		double sum = 0;
		int i;
		for (i=1; sum < d; ++i) {
			sum += Math.pow(3,i);
			System.out.println(i + ": " + sum);
		}
		
		System.out.println("\nNumber people got helped: " + sum);
		System.out.println("in " + --i + " days");
		s.close();
	}

}
