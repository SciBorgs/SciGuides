# Introduction

In this guide, we're going to be making a tic tac toe game, and learning important Java concepts as we go.
## Prerequisites

- Java101
- Java102
- Unit Testing with JUnit (make guide
	- Extension installed
- etc
## Goals

Familiarity with the following:
- JUnit testing
- Enums
- Records

Also, a working tic tac toe game!
## Best Practices

See [Java101](Java101.md#best-practices).
## Setup

If you did [Java101](/projects/intro-to-programming/Java101.md) and [Java102](/projects/intro-to-programming/Java102.md), use the same repository that you used there. Otherwise, follow the [instructions in Java101 to set up a repository](Java101.md#setup).

Make a new directory called `tictactoe` (or if you're making a whole new repository, just call it tic-tac-toe). We'll be working in that directory/package. Every Java file of `tictactoe` should  start with the line `package tictactoe;`. Make a file in `tictactoe` called `Main.java`, as well as a `README.md` file.

In the README, link [this guide](/projects/intro-to-programming/TicTacToe.md).

Press on the testing tab -- test tube -- on the left side of the VSCode window. Click "Enable Java Tests". At the top of the screen, press "JUnit Jupiter".
# Board

First off, we're going to make the tic tac toe board. We did something similar in [Java101](/projects/intro-to-programming/Java101.md#2d-arrays), where we made a three by three 2D array, and called it a board. Now, we're going to make a `Board` class, from which we will be able to create `Board` objects. Our board class will contain a few things:
- the `board`: a three by three 2D integer array. It will start out with only 0s, because all squares start out blank.
- a `get` method: a method that takes a row and column and returns the contents of that place
- a `move` method: a method that takes a move (which player's turn it is and where they want to go) and updates the board to reflect the new turn
- an `winner` method: a method that takes no inputs, and returns who (if anyone) has won the game.
- an `over` method: a method that takes no inputs and returns whether or not the game is over.
- a `toString` method

We will not write our own constructor, because we don't need any input to customize each board. When first created, every board should look the same. It is only as the game goes on and players take turns that board become more unique. When you don't add a constructor, instead there is a *default constructor*. Default constructors take no inputs, and simply return a new object of that class.

```java
package tictactoe;

public class Board {
	private final int[][] board = new int[3][3];
}
```
## toString

Okay, next let's add our `toString` method. Let's try to make our board look like this:

```
x - -
- o x
- - -
```

First off, let's make a method to convert integers that represent players ($0$, $-1$, $1$) to strings:

```java
public static String playerToString(int player) {
	if (player == -1) {
		return "o";
	} else if (player == 0) {
		return "-";
	} else if (player == 1) {
		return "x";
	} else {
		throw new RuntimeException("not a valid player: " + player);
	}
}
```

This is static because it doesn't have anything to do with a particular `Board`. I did something here that we haven't done before: I threw an exception. Theoretically, someone could pass this method an integer that is not 1 or -1 or 0, and if that happens, we know that something has gone wrong. So we throw an exception (an error), and that will stop everything and show us our message.

Now let's write our `toString` method:

```java
@Override
public String toString() {
	String str = "";
	for (int[] row : board) {
		for (int square : row) {
			str += playerToString(square) + " ";
		}
		str += "\n";
	}
	return str;
}
```

As always, go through this method and make sure you really understand all of it.

Now, before we write anything else in this class, let's test what we've done so far.
### Testing

So far in the intro to programming series, we've tested our code by printing values and checking if they are what we expected. For this guide, our code is getting a little more complicated, and we're going to start using [Unit Tests](link)!

Make a new directory inside of `tictactoe` called `test`. Inside of `test`, make a file called `BoardTest.java`.  Import JUnit assertions. Here's what your file should look like:
```java
package tictactoe.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.Test;

import tictactoe.Board;

public class BoardTest {
}
```

Let's add a test to make sure that our `playerToString` works! We'll have four test cases: `playerToString(1)`, `playerToString(-1)`, `playerToString(0)`, and  `playerToString(2)`. The first three cases should give us "x", "o", and "-" respectively. The last case, `playerToString(2)`, should cause an exception to be thrown. Here's how we would write a test to verify those expectations:

```java
@Test
public void playerToString() {
    assertEquals("x", Board.playerToString(1));
    assertEquals("o", Board.playerToString(-1));
    assertEquals("-", Board.playerToString(0));
    assertThrows(RuntimeException.class, () -> Board.playerToString(2));
}
```

The first three assertions are pretty intuitive. The last one is a little more complicated. Essentially, it's asserting that when the code `Board.playerToString(2)` is run, a `RuntimeException` will be thrown. I'm not going to explain the `() ->` notation here, but it will become important in future projects. If you want to learn more now, read [this](link).

Now run the test and see if it works!

Next, let's test our whole `toString` method. If we take an empty board and turn it into a String, we should expect to get back the following: `"- - - \n- - - \n- - - \n"`

```java
@Test
public void boardToString() {
	assertEquals("- - - \n- - - \n- - - \n", new Board().toString());
}
```

Run it to check if it works!
## get & move

Let's write a super simple method to get the contents of a place:

```java
public int get(int row, int column) {
	return board[row][column];
}
```

Next up is our `move` method. This method needs to take what player is playing and which row and column they want to move in. Here's the header:

```java
public void move(int player, int row, int column);
```

Try to fill in the function. To start, write something that just inserts `player` at the specified `row` and `column` of `board`. Then, in `BoardTest`, write something like the following to test your function:

```java
@Test
public void testMove() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
}
```

Once you have that test working, update your `move` function so that it doesn't allow invalid moves. It should pass this updated version of `testMove`:

```java
@Test
public void testMove() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
	// check that you can't play in a space that's full already
	assertThrows(RuntimeException.class, () -> b.move(-1, 2, 0));
	// check that you can't give an int other than 1 or -1 as player
	assertThrows(RuntimeException.class, () -> b.move(0, 2, 2));
}
```

### Update toString test

Now that we can change a board, let's make sure that the `toString` method works with a not-empty board.

```java
@Test
public void boardToString() {
	assertEquals("- - - \n- - - \n- - - \n", new Board().toString());
	Board b = new Board();
	b.move(1, 1, 1);
	assertEquals("- - - \n- x - \n- - - \n", new b.toString());
}
```

Add one more test case! It should have at least one space with an o (-1) in it.
## winner

The next step is to write a method that finds the winner of a board. This method will return `1` if `x` has won the board, `-1` if y has won, and `0` if no one has won. I'm going to write most of the code for you. Fill the rest in.

```java
/** @return whether a set of three spaces are won by one player */
private static boolean setWon(int a, int b, int c) {
	return a != 0 && a == b && b == c;
}

/** @return Whether the ith row or column has been won */
private boolean rowOrColWon(int i) {
	return setWon(board[i][0], board[i][1], board[i][2]) ||
		   setWon(board[0][i], board[1][i], board[2][i]);
}

/** @return Whether either of the diagonals has been won */
private boolean diagonalWon() {
	// write this!
}

public int winner() {
	for (int i = 0; i < 3; i++) {
		if (rowOrColWon(i)) {
			return board[i][i];
		}
	}
	if (diagonalWon()) {
		return board[1][1];
	}
	return 0;
}
```

Go through all the code (use a pen and paper to visualize if you're having trouble). Then fill in the `diagonalWon` method. At the end, the following test should pass:

```java
@Test
public void testWinner() {
	Board b1 = new Board();
	b1.move(1, 0, 1);
	b1.move(-1, 1, 1);
	b1.move(1, 2, 1);
	assertEquals(0, b1.winner());
	
	b1.move(1, 0, 0);
	b1.move(1, 0, 2);
	assertEquals(1, b1.winner());
	
	Board b2 = new Board();
	b2.move(-1, 0, 0);
	b2.move(-1, 1, 1);
	b2.move(-1, 2, 2);
	assertEquals(-1, b2.winner());

	Board b3 = new Board();
	b3.move(1, 1, 1);
	b3.move(1, 0, 2);
	b3.move(1, 1, 2);
	b3.move(1, 2, 2);
	assertEquals(1, b3.winner());
}
```
## over

The next method is `over`, which returns whether a game is over. The two possibilities for a game to be over are:
1. a player has won
2. the board is full
You can check whether the board has been won by analyzing the output of `winner()`. To check if the board is full, you will need to iterate over the whole board (you can use *nested for loops*).

Here's the header:
```java
public boolean over();
```

Fill in the function! It should pass the following test:

```java
@Test
public void testOver() {
	Board bWon = new Board();
	bWon.move(1, 0, 2);
	bWon.move(1, 1, 1);
	assertFalse(bWon.over());
	bWon.move(1, 2, 0);
	assertTrue(bWon.over());

	Board bFull = new Board();
	for (int r = 0; r < 3; r++) {
		int firstSpace = (r % 2) * 2 - 1;
		for (int c = 0; c < 3; c++) {
			int mult = c / 2 * 2 - 1;
			bFull.move(firstSpace * mult, r, c);
		}
	}
	assertTrue(bFull.over());
}
```

The for loop in this test is a little confusing. It fills `bFull` with the following pattern:

```
x x o
o o x
x x o
```

The point of this is that the board is full, but there isn't a winner, which is an important case to test our over function on.

If you want to understand exactly how this pattern is being made, I encourage you to go through the loop step by step with pen and paper.
### Updating move

Now that we can tell whether a game is over, let's update our `move` method. Because if a game is over and someone has one, we don't want to continue allowing players to take moves. So update the `move` method so that it passes this test:

```java
@Test
public void testMove() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
	// check that you can't play in a space that's full already
	assertThrows(RuntimeException.class, () -> b.move(-1, 2, 0));
	// check that you can't give an int other than 1 or -1 as player
	assertThrows(RuntimeException.class, () -> b.move(0, 2, 2));
	b.move(1, 0, 0);
	b.move(1, 1, 0);
	// check that you can't move after a board is already won
	assertThrows(RuntimeException.class, () -> b.move(1, 2, 2));
}
```
# Game

*Note: now would be a great time to push your code if you haven't already!*

Now that the `Board` class is finished, we can make an actually playable game!

Create a `Game.java` file for a `Game` class. `Game` will store the board and which player's turn it is. It will have a `main` method, and when `main` is run the game will begin. Each turn, the computer will print the board and ask the player what row and column they want to go in.

```java
package tictactoe;

public class Game {
	public static final Board board = new Board();
	public static int currentPlayer = 1;

	public static void main(String[] args) {
		
	}
}
```

First things first, we're going to be using `Scanner` for this in order to get user input. Take a couple minutes to [learn what it is!](https://www.geeksforgeeks.org/scanner-class-in-java/)

We're going to need to make a `Scanner` object, but first, we need to import the `Scanner` class, so add the following line below `package tictactoe;`:

```java
import java.util.Scanner;
```

Next, we'll make a `Scanner` object inside of `Game`:

```java
public static Scanner sc = new Scanner(System.in);
```

So whenever we want to get user input (i.e. for the next move), we can use our scanner, `sc`.

## Version 1

Let's start by writing the simplest possible version of this game. We'll have a while loop that runs until the board is over. Each run of the while loop will be a new turn. Here's what we'll do in the while loop:
1. print out the board
2. print out who's turn it is
3. ask the player for a row and column (use scanner)
4. update the board with the player's move
5. update `currentPlayer` (multiply by -1)

Then, after the while loop ends, print out the board and what the result is.

Mostly I'm going to let you do this on your own. But I will give you a couple of hints/tricks to make this easier and your code nicer.
## Ternary Operators

When you're printing out the message about what the result of the game is, you can use a *ternary operator*. This is basically an inline if expression.

Here's how a ternary operator works:
```java
condition ? expr1 : expr2
```

`condition` is a boolean, and `expr1` and `expr2` are expressions that evaluate to the same type. The entire expression (`condition ? expr1 : expr2`) evaluates to `expr1` if `condition` is true, and `expr2` if condition is false.

 For an example, let's look at how you might use this to write a simple `max` function:
```java
public static double max(double a, double b) {
	return a > b ? a : b;
}
```

Now, for the tictactoe game, it might look more like this:
```java
System.out.println("Game over! " + 
				  (winner == 0 ? "It's a tie" :
								 "The winner is " +
								 Board.playerToString(winner) + "!!"));
```
## Collecting indices

When you're collecting the rows and columns from the user, you should use `sc.nextInt()`. But make sure that if you're asking the user to input a number from 1-3 for the indices, that you subtract one because arrays in Java are indexed starting from 0!

In the end, getting a row might look like this:
```java
System.out.println("what row (1-3) will you move in?");
int row = sc.nextInt() - 1;
```