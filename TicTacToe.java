import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TicTacToe implements ActionListener {
    JFrame tct;
    JButton[] xox = new JButton[9];
    JPanel board;
    JLabel label;
    Font font = new Font("Aharoni", Font.BOLD, 34);
    int c = 0;
    int[] n = new int[9];
    String[] s = new String[9];
    int x = 0;
    JButton playagain;

    TicTacToe() {
        tct = new JFrame("Tic Tac Toe Game");
        tct.setSize(800, 650);
        tct.setLocationRelativeTo(null);
        tct.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tct.setLayout(null);
        tct.setResizable(false);

        board = new JPanel();
        board.setBounds(150, 80, 480, 400);
        board.setLayout(new GridLayout(3, 3));
        board.setBackground(Color.white);

        JButton b1 = new JButton();
        JButton b2 = new JButton();
        JButton b3 = new JButton();
        JButton b4 = new JButton();
        JButton b5 = new JButton();
        JButton b6 = new JButton();
        JButton b7 = new JButton();
        JButton b8 = new JButton();
        JButton b9 = new JButton();

        xox[0] = b1;
        xox[1] = b2;
        xox[2] = b3;
        xox[3] = b4;
        xox[4] = b5;
        xox[5] = b6;
        xox[6] = b7;
        xox[7] = b8;
        xox[8] = b9;

        for (int i = 0; i < 9; i++) {

            xox[i].setFocusable(false);
            if (i == 1 || i == 3 || i == 5 || i == 7) {
                xox[i].setBackground(Color.blue);
                xox[i].setForeground(Color.white);
                board.add(xox[i]);

            } else {
                xox[i].setBackground(new Color(191, 24, 9));
                xox[i].setForeground(Color.BLUE);
                board.add(xox[i]);
            }
            xox[i].addActionListener(this);

            xox[i].setFont(font);
          
            board.add(xox[i]);
        }

        label = new JLabel();
        label.setBounds(290, 10, 300, 80);
        label.setFont(font);
        label.setText("X's Turn");
        label.setForeground(new Color(0, 160, 5));

        playagain = new JButton("PLAY AGAIN");
        playagain.setBounds(230, 520, 270, 50);
        playagain.setFont(font);
        playagain.setFocusable(false);
        playagain.setBackground(Color.green);
        playagain.setForeground(Color.red);
        playagain.addActionListener(this);

        tct.add(label);
        tct.add(board);
        tct.add(playagain);
        tct.setVisible(true);

    }

    public static void main(String[] args) {
        new TicTacToe();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == playagain){
            tct.dispose();
            new TicTacToe();
        }

        if (c % 2 == 0) {
            for (int i = 0; i < 9; i++) {
                if (e.getSource() == xox[i]) {
                    xox[i].setText("X");
                    xox[i].setEnabled(false);
                    n[i] = Integer.parseInt(String.valueOf(i));
                    System.out.println(n[i]);
                    s[i] = xox[i].getText();
                    System.out.println(s[i]);
                    label.setText("O's Turn");
                    label.setForeground(new Color(105, 0, 184));
                }
                c += 1;

            }
        } else {
            for (int i = 0; i < 9; i++) {
                if (e.getSource() == xox[i]) {
                    xox[i].setText("O");
                    xox[i].setEnabled(false);
                    n[i] = Integer.parseInt(String.valueOf(i));
                    System.out.println(n[i]);
                    s[i] = xox[i].getText();
                    System.out.println(s[i]);
                    label.setText("X's Turn");
                    label.setForeground(new Color(0, 160, 5));

                }
                c += 1;

            }

        }
        for (int i = 0; i < 9; i++) {
            if (s[0] == "X" && s[1] == "X" && s[2] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);

            } else if (s[0] == "X" && s[3] == "X" && s[6] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[0] == "X" && s[4] == "X" && s[8] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[8] == "X" && s[5] == "X" && s[2] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[6] == "X" && s[4] == "X" && s[2] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[3] == "X" && s[4] == "X" && s[5] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[6] == "X" && s[7] == "X" && s[8] == "X") {
                label.setText("X Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[0] == "O" && s[1] == "O" && s[2] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[0] == "O" && s[3] == "O" && s[6] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[0] == "O" && s[4] == "O" && s[8] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[8] == "O" && s[5] == "O" && s[2] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[6] == "O" && s[4] == "O" && s[2] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[3] == "O" && s[4] == "O" && s[5] == "O") {
                label.setText("O  Is the Winner");
                xox[i].setEnabled(false);
            } else if (s[6] == "O" && s[7] == "O" && s[8] == "O") {
                label.setText("O Is the Winner");
                xox[i].setEnabled(false);
            } 

        }
        

    }
}