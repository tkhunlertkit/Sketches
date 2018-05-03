import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.text.BadLocationException;
import javax.swing.text.DefaultHighlighter;
import javax.swing.text.Highlighter;

public class Read extends JFrame implements ActionListener {
	/**
	 * 
	 */

	private static final long serialVersionUID = 1L;
	protected JTextField textField;
	protected JTextArea productInfo = new JTextArea(10, 70);
	protected JTextArea images = new JTextArea(10, 30);
	protected JTextArea Shipping = new JTextArea(10, 50);
	protected JTextArea Payment = new JTextArea(10, 50);
	protected JTextArea Result = new JTextArea(17 ,100);
	private static ConstructString cs = new ConstructString();

	public Read() {
		this.setSize(1300, 1000);
		
		
		String t = setShipping();
		Shipping.setText(t);
		t = setPayment();
		Payment.setText(t);
		textField = new JTextField("Save as..", 20);
		textField.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent evt) {
				try {
					String text = genHTML();
					Result.setText(text);
					Highlighter h = Result.getHighlighter();
					h.removeAllHighlights();
					int pos = text.indexOf(cs.getAdded());
					try {
						h.addHighlight(pos, pos + cs.getAdded().length(),
								DefaultHighlighter.DefaultPainter);
					} catch (BadLocationException e) {
						JOptionPane.showMessageDialog(null, "error highlighting");
						e.printStackTrace();
					}
					
					textField.selectAll();

					if (!textField.getText().equalsIgnoreCase("save as..")) {

						String content = genHTML();

						File file = new File(System.getProperty("user.dir") + "/"
								+ textField.getText() + ".html");

						if (file.exists()) {
							file.delete();
						}
						// if file doesnt exists, then create it

						file.createNewFile();

						FileWriter fw = new FileWriter(file.getAbsoluteFile());
						BufferedWriter bw = new BufferedWriter(fw);
						bw.write(content);
						bw.close();

						JOptionPane.showMessageDialog(null, "Done created!!!");
					} else {
						JOptionPane
								.showMessageDialog(null, "Type in the file name");
					}

				} catch (IOException e) {

					JOptionPane.showMessageDialog(null, "Error Writing to File: "
							+ textField.getText());
					e.printStackTrace();
				}
			}
		});
		
		JScrollPane ProductInfo = createSP(productInfo);
		JScrollPane Images = createSP(images);
		JScrollPane ShippingInfo = createSP(Shipping);
		JScrollPane PaymentInfo = createSP(Payment);
		JScrollPane HTML = createSP(Result);
		Result.setEditable(false);

		

		JButton j = new JButton("Compute");
		JButton exit = new JButton("Exit");
		JButton write = new JButton("Save as HTML File");
		j.addActionListener(this);
		exit.addActionListener(this);
		write.addActionListener(this);

		// setting layout
		setTitle("HTML");
		setLayout( new FlowLayout(FlowLayout.CENTER,-5,-4) ); 

		// add components
		JPanel first = new JPanel();
		JPanel second = new JPanel();
		JPanel result = new JPanel();
		JPanel last = new JPanel();
		
		first.add(ProductInfo);
		first.add(Images);
		add(first);
		
		second.add(ShippingInfo);
		second.add(PaymentInfo);
		add(second);
		
		result.add(HTML);
		add(result);
		
		last.add(textField);
		last.add(j);
		last.add(write);
		last.add(exit);
		add(last);
//		add(ShippingInfo);
//		add(PaymentInfo);
//		add(HTML, c);
//		add(textField);
//		add(j);
//		add(write);
//		add(exit);
		textField.selectAll();

	}
	


	private String setPayment() {
		String t = "";
		t += "Payment\n";
		t += "\u2022\tWe accept PayPal only.\n";
		t += "\u2022\tThe payment should be made within 3 days after auction ends. Please contact us if payment will be late for any reason.\n";
		t += "\u2022\tIf you buy more than one item, please hold on until all bids you will win end, then pay for them together.\n";
		t += "Feedback\n";
		t += "\u2022\tFeedback is a very important part of ebay. We will leave positive feedback for each customer. We are looking forward to your positive feedback after you received the item.\n";
		t += "\u2022\tWe will leave feedback in return when we receive it. This assures us that your shipment has arrived at its destination.\n";
		t += "\u2022\tIf there are any problems, please email us before posting feedback so we may try to resolve the issue first.\n";
		return t;
	}



	private String setShipping() {
		String t = "";
		t += "Shipping\n";
		t += "\u2022\tAll items will be shipped within 3 business days after payment has been received.\n";
		t += "\u2022\tThe package will be shipped from Thailand via standard airmail.\n";
		t += "\u2022\tThe delivery time is estimate 3-5 weeks international shipping.\n";
		t += "\u2022\tImport duties, taxes, and charges are not included in the item price or shipping cost. These charges are the buyer's responsibility.\n";
		t += "\u2022\tNo return accepted.\n";
		t += "\u2022\tIf you are OK with this please go ahead and purchase and please do not leave us low star rating feedback on the shipping time and shipping cost categories as we have no control over the price and delivery time.\n";
		t += "\u2022\tThank you for your understanding we are sure you will love the product.\n";
		return t;
	}



	private String genHTML() {
		String im = images.getText() + '\n';
		String product = productInfo.getText() + '\n';
		String shipping = Shipping.getText() + '\n';
		String payment = Payment.getText() + '\n';
		String text = cs.append(im, product, shipping, payment);
		return text;
	}
	
	private JScrollPane createSP(JTextArea J) {
		J.setEditable(true);
		JScrollPane scrollPane = new JScrollPane(J);
		return scrollPane;
		
	}

	public void actionPerformed(ActionEvent evt) {
		textField.selectAll();

		if (evt.getActionCommand().equalsIgnoreCase("compute")) {
			
			String text = genHTML();
			productInfo.setText(productInfo.getText());
			Result.setText(text);
			Highlighter h = Result.getHighlighter();
			h.removeAllHighlights();
			int pos = text.indexOf(cs.getAdded());
			try {
				h.addHighlight(pos, pos + cs.getAdded().length(),
						DefaultHighlighter.DefaultPainter);
			} catch (BadLocationException e) {
				JOptionPane.showMessageDialog(null, "error highlighting");
				e.printStackTrace();
			}
		}

		if (evt.getActionCommand().equalsIgnoreCase("Exit")) {
			System.exit(1);
		}

		if (evt.getActionCommand().equalsIgnoreCase("save as HTML File")) {
			try {

				if (!textField.getText().equalsIgnoreCase("save as..")) {

					String content = genHTML();
					Result.setText(content);

					File file = new File(System.getProperty("user.dir") + "/"
							+ textField.getText()  + ".html");

					if (file.exists()) {
						file.delete();
					}
					// if file doesnt exists, then create it

					file.createNewFile();

					FileWriter fw = new FileWriter(file.getAbsoluteFile());
					BufferedWriter bw = new BufferedWriter(fw);
					bw.write(content);
					bw.close();

					JOptionPane.showMessageDialog(null, "Done created!!!");
				} else {
					JOptionPane
							.showMessageDialog(null, "Type in the file name");
				}

			} catch (IOException e) {

				JOptionPane.showMessageDialog(null, "Error Writing to File: "
						+ textField.getText());
				e.printStackTrace();
			}
		}
		// Make sure the new text is visible, even if there
		// was a selection in the text area.
		productInfo.setCaretPosition(productInfo.getDocument().getLength());
		
	}

	/**
	 * Create the GUI and show it. For thread safety, this method should be
	 * invoked from the event dispatch thread.
	 */
	private static void createAndShowGUI() {
		// Create and set up the window.
		Read frame = new Read();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// Display the window.
		frame.setVisible(true);

	}
	
	

	public static void main(String[] args) {
		// Schedule a job for the event dispatch thread:
		// creating and showing this application's GUI. 
		javax.swing.SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				createAndShowGUI();
			}
		});
	}
	
	
}