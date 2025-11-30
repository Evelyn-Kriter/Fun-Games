
//I have neither given nor received unauthorized aid on thlis assignment.
import java.util.Scanner;
import java.lang.Character;
import java.lang.String;

public class HangmanDriver {
	static Scanner scan = new Scanner(System.in);
	static boolean playing = true; // true means the game is running

	public static void main(String[] args) {
		do {
			System.out.println("Welcome to Hangman!");
			Hangman game = new Hangman();
			game.selectGameWord();
			while (game.getnumParts() <= 10) {
				game.showMan(game.getnumParts());
				game.getIncorrectGuesses();
				char choice = getChoice();
				if (choice == 'L') {
					game.getCurrentWord(getGuessL());
				}
				if (choice == 'W') {
					game.getguessCurrentWord(getGuessW());
				}
			}
			System.out.println(game.getgameWord());
			System.out.println("Play again: Yes(Y) or No(N)");
			char playagain = (scan.next().charAt(0));
			playagain = Character.toUpperCase(playagain);
			if (playagain == 'N') {
				playing = false;
			}
		} while (playing == true);
		System.out.println("Goodbye!");
		scan.close();
	}

	public static char getChoice() {
		// asks the player to choose to guess a letter or the entire word.
		System.out.println("Type L to guess a letter or W to guess a word:");
		char choice = scan.next().charAt(0);
		choice = Character.toUpperCase(choice);
		return choice;
	}

	public static char getGuessL() {
		// prompts the player to guess a letter
		System.out.println("Enter your guess (as a single letter):");
		char guessL = scan.next().charAt(0);
		guessL = Character.toUpperCase(guessL);
		return guessL;
	}

	public static String getGuessW() {
		// prompts the player to guess the entire word
		System.out.println("Enter your guess (as a word):");
		scan.nextLine();
		String guessW = scan.nextLine();
		guessW = guessW.toUpperCase();
		return guessW;
	}

}