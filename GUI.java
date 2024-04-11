import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class GUI {
    private static JFrame frame;
    private static JLabel label;
    private static JButton button;
    private static JLabel imageLabel;
    private static JPanel imagePanel;
    private static JPanel videoPanel;
    private static CardLayout cardLayout;

    public static void main(String[] args) {
        // Get screen dimensions
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int screenWidth = (int) screenSize.getWidth();
        int screenHeight = (int) screenSize.getHeight();

        // Create the main frame
        frame = new JFrame("What's Waldo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a menu bar
        JMenuBar menuBar = new JMenuBar();
        JMenu switchMenu = new JMenu("Switch");
        JMenuItem imageItem = new JMenuItem("Image");
        JMenuItem videoItem = new JMenuItem("Video");
        switchMenu.add(imageItem);
        switchMenu.add(videoItem);
        menuBar.add(switchMenu);
        frame.setJMenuBar(menuBar);

        // Create a label to display file path
        label = new JLabel("Selected File: ");
        label.setBounds(20, 20, 350, 30);

        // Create a button
        button = new JButton("Select Image File");
        button.setBounds(20, 60, 150, 30);

        // Create panels for image and video
        imagePanel = new JPanel();
        videoPanel = new JPanel();
        cardLayout = new CardLayout();
        frame.setLayout(cardLayout);

        // Create an area to display the image
        imageLabel = new JLabel();
        int imageWidth = (int) (screenWidth * 0.8);
        int imageHeight = (int) (screenHeight * 0.80);
        imageLabel.setBounds(20, 100, screenWidth - 40, screenHeight - 250);

        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                fileChooser.setCurrentDirectory(new File(System.getProperty("user.home")));
                int result = fileChooser.showOpenDialog(frame);
                if (result == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = fileChooser.getSelectedFile();
                    label.setText("Selected File: " + selectedFile.getAbsolutePath());
                    // Display the selected image
                    try {
                        Image img = ImageIO.read(selectedFile);
                        Image scaledImg = img.getScaledInstance(imageLabel.getWidth(), imageLabel.getHeight(), Image.SCALE_SMOOTH);
                        ImageIcon icon = new ImageIcon(scaledImg);
                        imageLabel.setIcon(icon);
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });

        // Add components to panels
        imagePanel.setLayout(null);
        imagePanel.add(label);
        imagePanel.add(button);
        imagePanel.add(imageLabel);

        // Add panels to frame
        frame.add(imagePanel, "Image");
        frame.add(videoPanel, "Video");

        // Set the frame size to fit the screen
        frame.setSize(screenWidth, screenHeight);

        // Make the frame visible
        frame.setVisible(true);

        // Add action listeners to the menu items
        imageItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(frame.getContentPane(), "Image");
            }
        });

        videoItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(frame.getContentPane(), "Video");
            }
        });
    }
}
