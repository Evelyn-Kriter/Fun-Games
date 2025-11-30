//I have neither given nor received unauthorized aid on this assignment.

import java.util.Random;
import java.lang.String;

public class Hangman {

	private int numwords = 10;
	private String[] words = new String[numwords];
	private String gameWord; // the answer
	private String dispWord = "-------";
	private char[] dispArr = dispWord.toCharArray();
	private String incorrectGuess = ""; // keep track of letters guessed
	private int numParts; // keep track of guess #

	public String selectGameWord() {
		// retrieves and returns a random word from the list of words for the
		// player to guess.
		System.out.println("Generating a secret word...");
		setWords();
		Random rand = new Random(); // instance of random class
		int upperbound = getNumWords();
		int int_random = rand.nextInt(upperbound); // generate random values from 0-24
		gameWord = words[int_random];
		System.out.println("Here is your word:");
		System.out.println(dispWord);
		gameWord = gameWord.toUpperCase(); // for continuity
		return gameWord;
	}

	public String getCurrentWord(char guessL) {
		// returns the word with each letter that has been correctly guessed
		// or a dash (–) for each letter that has not yet been guessed
		// (initially, this should be all dashes).
		boolean isCorrect = false; // did the player guess right?
		char[] gameWordarr = gameWord.toCharArray();
		for (int i = 0; i < gameWordarr.length; i++) {
			if (gameWordarr[i] == guessL) {
				dispArr[i] = gameWordarr[i];
				isCorrect = true; // true if player guessed right
			}
		}
		if (isCorrect == true) {
			System.out.println("Correct!");
		} else if (isCorrect == false) {
			System.out.println("Incorrect!");
			incorrectGuess += guessL;
		}
		numParts += 1; // add 1 to number of guesses
		System.out.println(dispArr);
		return dispWord;
	}

	public void getguessCurrentWord(String guessW) {
		// Compares two strings to see if player guessed the word
		boolean isCorrect = false;
		if (gameWord.equals(guessW) == true) {
			System.out.println("Correct!");
			System.out.println("You Win!");
			isCorrect = true;
		}
		if (isCorrect == false) {
			System.out.println("Incorrect!");
			System.out.println("You Lost!");
		}
		numParts = 11;
	}

	public String getIncorrectGuesses() {
		// returns the incorrect guesses so far.
		System.out.println("Incorrect Guesses:" + incorrectGuess);
		return incorrectGuess;
	}

	public int getnumParts() {
		return numParts;
	}

	public String getgameWord() {
		return gameWord;
	}

	/*
	 * Method to display the hangman given the number of body parts to show Player
	 * gets at most 10 turns.
	 */
	public void showMan(int numParts) {

		if (numParts == 0) {
			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 1) {
			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 2) {
			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|        |");
			System.out.println("|        |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}

		if (numParts == 3) {
			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|      __|");
			System.out.println("|        |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 4) {
			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|");
			System.out.println("|     	 |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 5) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__");
			System.out.println("|     	 |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 6) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__o");
			System.out.println("|     	 |");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}
		if (numParts == 7) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__o");
			System.out.println("|     	 |");
			System.out.println("|       /");
			System.out.println("|      /  ");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}

		if (numParts == 8) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__o");
			System.out.println("|     	 |");
			System.out.println("|       / \\");
			System.out.println("|      /   \\");
			System.out.println("|");
			System.out.println("|");
			System.out.println("____");
		}

		if (numParts == 9) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__o");
			System.out.println("|     	 |");
			System.out.println("|       / \\");
			System.out.println("|      /   \\");
			System.out.println("|    O/    ");
			System.out.println("|");
			System.out.println("____");

		}
		if (numParts == 10) {

			System.out.println("________");
			System.out.println("|       |");
			System.out.println("|      ____");
			System.out.println("|     / .. \\");
			System.out.println("|    <   .  >");
			System.out.println("|     \\__^_/");
			System.out.println("|        |");
			System.out.println("|     o__|__o");
			System.out.println("|     	 |");
			System.out.println("|       / \\");
			System.out.println("|      /   \\");
			System.out.println("|    O/     \\O");
			System.out.println("|");
			System.out.println("____");
		}

	}

	// Sets the list of candidate words for the player to guess
	public void setWords() {

		words[0] = "notions";
		words[1] = "measure";
		words[2] = "product";
		words[3] = "foliage";
		words[4] = "garbage";
		words[5] = "minutes";
		words[6] = "chowder";
		words[7] = "recital";
		words[8] = "concoct";
		words[9] = "brownie";
	}

	// Returns the number of words to choose from
	public int getNumWords() {
		return numwords;
	}

	// Returns the array of words
	public String[] getWords() {
		return words;
	}

}
