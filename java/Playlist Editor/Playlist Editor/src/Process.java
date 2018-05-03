import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public class Process {
	
	public static void main(String[] args) {
		File f = GetFile.get();
		String[] ss;
		if (f != null) {
			ss = getText(f);
			try {
				writeText(f,ss);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			for (String s: ss) {
				String test = f.getName();
				test = test.substring(0, test.length()-4);
				System.out.println(test);
				System.out.println(s);
			}
		}
	}
	
	public static String[] getText(File F) {
		String total = "";
		try {
			BufferedReader br = new BufferedReader(new FileReader(F.getPath()));
			String ts;
			while ((ts = br.readLine()) != null) {
				total += ts + '\n';
			}
			br.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return total.split("\n");
	}
	
	public static void writeText(File f, String[] s) throws IOException {
		if (f.exists()) f.delete();
		f.createNewFile();
		String name = f.getName();
		name = name.substring(0, name.length()-4);

		FileWriter fw = new FileWriter(f.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);
		bw.write("#EXTM3U\n");
		for (String content: s) {
			if (!content.isEmpty() && content.charAt(0) != '#') {
				String[] contents = content.split("/");
				bw.write(name + "/" + contents[contents.length-1] + "\n");
			}
		}
		bw.close();
	}

}