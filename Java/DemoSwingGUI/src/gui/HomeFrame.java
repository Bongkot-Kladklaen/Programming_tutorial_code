package gui;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HomeFrame {
    private JPanel panel1;
    private JLabel label1;
    private JTextField text1;
    private JButton clickMeButton;
    private JLabel resultLabel;

    public HomeFrame() {
        clickMeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                resultLabel.setText(text1.getText());
            }
        });
    }

    public static void main(String[] args) {
        JFrame jFrame = new JFrame("Test Swing GUI");
        jFrame.setContentPane(new HomeFrame().panel1);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.pack();
        jFrame.setVisible(true);
    }
}
