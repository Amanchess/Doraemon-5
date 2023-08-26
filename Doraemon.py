import javax.swing.*;
import java.awt.*;

public class DoraemonChessGame extends JFrame {

    private static final int BOARD_SIZE = 8;
    private static final int CELL_SIZE = 80;

    public DoraemonChessGame() {
        setTitle("Doraemon vs Shinchan Chess");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE);
        setLocationRelativeTo(null);

        JPanel chessBoard = new JPanel(new GridLayout(BOARD_SIZE, BOARD_SIZE));
        add(chessBoard);

        initializeChessBoard(chessBoard);

        setVisible(true);
    }

    private void initializeChessBoard(JPanel chessBoard) {
        boolean isWhiteCell = true;
        boolean isWhitePiece = true; // To alternate between white and black pieces
        for (int row = 0; row < BOARD_SIZE; row++) {
            isWhiteCell = !isWhiteCell;
            for (int col = 0; col < BOARD_SIZE; col++) {
                JLabel cellLabel = new JLabel();
                cellLabel.setHorizontalAlignment(JLabel.CENTER);

                if (isWhiteCell) {
                    cellLabel.setBackground(new Color(181, 136, 99)); // Light cell color (wooden board)
                } else {
                    cellLabel.setBackground(new Color(240, 217, 181)); // Dark cell color (wooden board)
                }

                isWhiteCell = !isWhiteCell;

                String asciiPiece = getDoraemonAsciiPiece(isWhitePiece, row, col);
                cellLabel.setText(asciiPiece);
                cellLabel.setOpaque(true);

                chessBoard.add(cellLabel);
                isWhitePiece = !isWhitePiece;
            }
            isWhitePiece = !isWhitePiece; // Switch for the next row
        }
    }

    private String getDoraemonAsciiPiece(boolean isWhitePiece, int row, int col) {
        String[] doraemonPieces = {
            "R", "N", "B", "Q", "K", "B", "N", "R",
            "P", "P", "P", "P", "P", "P", "P", "P",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            "P", "P", "P", "P", "P", "P", "P", "P",
            "R", "N", "B", "Q", "K", "B", "N", "R"
        };
        return doraemonPieces[isWhitePiece ? col : BOARD_SIZE - 1 - col];
    }

    private String getShinchanAsciiPiece(boolean isWhitePiece, int row, int col) {
        String[] shinchanPieces = {
            "R", "N", "B", "Q", "K", "B", "N", "R",
            "P", "P", "P", "P", "P", "P", "P", "P",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            ".", ".", ".", ".", ".", ".", ".", ".",
            "p", "p", "p", "p", "p", "p", "p", "p",
            "r", "n", "b", "q", "k", "b", "n", "r"
        };
        return shinchanPieces[isWhitePiece ? col : BOARD_SIZE - 1 - col];
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            DoraemonChessGame game = new DoraemonChessGame();
        });
    }
}
