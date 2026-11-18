## Introduction

In this guide you'll build a tic tac toe game that you can play in the terminal with a friend.

You'll also write your first unit tests. Tests are little bits of code that check your other code for you, so you don't have to keep printing things out to see if they work.
## Prerequisites

- Comfortable with all of the [goals for Java102](Java102.md#goals)
- The VSCode extension "Test Runner for Java" installed (the [Unit Testing](../../sheets/UnitTesting.md) sheet has more on testing if you're curious)
## Goals

By the end, you'll be comfortable with:

- writing a class from scratch
- throwing and catching exceptions
- JUnit tests
- getting input from the user with `Scanner`
- ternary operators

Oh, and you'll have a working tic tac toe game!
## Best Practices

See [Java101](Java101.md#best-practices).
## Setup

If you did [Java101](Java101.md) and [Java102](Java102.md), use the same repository you used there. Otherwise, follow the [instructions in Java101 to set up a repository](Java101.md#setup).

1. Make a new directory called `tictactoe`. You'll work in there for the whole guide.
2. Make a `README.md` file inside `tictactoe` and link [this guide](./TicTacToe.md) in it.
3. Turn on tests:
	- Click the testing tab (the test tube icon) on the left side of VSCode
	- Click "Enable Java Tests"
	- At the top of the screen, pick "JUnit Jupiter"
	- A `lib` folder will show up in your repo. That's JUnit. Leave it there.

*Package note: `Board.java` and `Game.java` are in the `tictactoe` package, so start those files with `package tictactoe;`. `BoardTest.java` is in the `test` subfolder and is in `tictactoe.test`, so start it with `package tictactoe.test;`.*

Here's what your folder will look like by the end:

```
tictactoe/
├── README.md
├── Board.java
├── Game.java
└── test/
    └── BoardTest.java
```
## Board

First up, the board. You made a 3 by 3 2D array in [Java101](Java101.md#2d-arrays) and called it a board. This time you'll wrap it in a `Board` class, so you can make as many `Board` objects as you want.

We'll store each square as a number:

| number | means |
| ------ | ----- |
| `1`    | x     |
| `-1`   | o     |
| `0`    | empty |

Why numbers and not letters? Switching turns becomes super easy. Multiply by `-1` and x turns into o (and o turns back into x).

Your `Board` class is going to have:

- `board`: the 3 by 3 array of numbers. Java fills new `int` arrays with `0`, so every square starts empty for free.
- `get`: tells you what's in a square
- `move`: puts a player's piece in a square
- `winner`: tells you who won (if anyone)
- `over`: tells you if the game is done
- `toString`: turns the board into text so you can print it

Make a file called `Board.java`:

```java
package tictactoe;

public class Board {
	private final int[][] board = new int[3][3];
}
```

`final` here means `board` will always be the same array. You can still change the numbers inside it.

Notice there's no constructor. Every new board looks the same (empty), so you don't need one. When you leave the constructor out, Java gives you a *default constructor* for free. It takes no inputs and just makes a new `Board`.
### toString

Let's make the board printable first. It should look like this:

```
x - -
- o x
- - -
```

Start with a helper that turns one number into a letter. Put it inside your `Board` class:

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

Two new things here:

- It's `static` because it doesn't care about any specific board. You call it like `Board.playerToString(1)`.
- It **throws an exception**. If someone passes in `7`, something has gone wrong. Throwing an exception stops the program and shows your message, so you find the bug right away instead of later. ([More on exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/) if you're curious.)

Now the real `toString`:

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

Read through it line by line until it makes sense. `"\n"` means "new line".

Before you write anything else, let's test it.
### Your first test

Up to now you've checked your code by printing stuff and looking at it. That gets old fast. A [unit test](../../sheets/UnitTesting.md) does the checking for you, and you can rerun all your tests with one click whenever you change something.

Make a directory called `test` inside `tictactoe`. In it, make `BoardTest.java`:

```java
package tictactoe.test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import tictactoe.Board;

public class BoardTest {
}
```

*Watch out: the import is `org.junit.jupiter.api.Test`. If VSCode auto-imports `org.junit.Test` instead, your tests won't show up!*

Now add a test for `playerToString` inside `BoardTest`:

```java
@Test
public void playerToString() {
	assertEquals("x", Board.playerToString(1));
	assertEquals("o", Board.playerToString(-1));
	assertEquals("-", Board.playerToString(0));
	assertThrows(RuntimeException.class, () -> Board.playerToString(2));
}
```

- `@Test` tells JUnit "this method is a test, run it".
- `assertEquals(expected, actual)` fails the test if the two don't match. ([Here are all the assertions](https://junit.org/junit5/docs/current/user-guide/#writing-tests-assertions).)
- `assertThrows` checks that the code throws an exception. Here we *want* `playerToString(2)` to blow up.

The `() ->` part is called a lambda. Don't worry about it yet. Just know it lets you hand a piece of code to `assertThrows` so it can run it. If you're curious, [here's more on lambdas](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html).

Run the test! Click the little green play button in the left margin next to `public void playerToString()`, or use the testing tab. Green check = passing.

Now test `toString`. An empty board should turn into three rows of dashes:

```java
@Test
public void boardToString() {
	assertEquals("- - - \n- - - \n- - - \n", new Board().toString());
}
```

Run it. Green? Nice.
### get & move

`get` is one line:

```java
public int get(int row, int column) {
	return board[row][column];
}
```

Rows and columns are numbered `0`, `1`, `2`, so the top-left square is `(0, 0)`, and the bottom-right square is `(2, 2)`.

`move` takes which player is moving and where. Here's the header:

```java
public void move(int player, int row, int column) {
	// your code here!
}
```

**Your turn.** For now, just put `player` into the right spot in `board`. Then add this test to `BoardTest`:

```java
@Test
public void move() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
}
```

Once that passes, make `move` stricter. It should throw a `RuntimeException` if:

1. `player` isn't `1` or `-1`
2. `row` or `column` isn't between `0` and `2`
3. the square is already taken

Do the checks in that order, before you change the square. (Check 2 has to come before check 3. If `row` is `5`, Java can't look at `board[5]`, so it throws its own confusing error. Your check throws a clear one instead.)

Swap your test for this one and get it passing:

```java
@Test
public void move() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
	// player has to be 1 or -1
	assertThrows(RuntimeException.class, () -> b.move(0, 2, 2));
	// square has to be on the board
	assertThrows(RuntimeException.class, () -> b.move(1, 3, 0));
	// can't play in a square that's already taken
	assertThrows(RuntimeException.class, () -> b.move(-1, 2, 0));
}
```

*Hint: copy the `throw new RuntimeException(...)` line from `playerToString` and change the message.*

*Careful: `player != 1 || player != -1` is always true, so every move would throw. You want `&&`.*
### Update the toString test

Now that you can change a board, make sure `toString` works on a board that isn't empty:

```java
@Test
public void boardToString() {
	assertEquals("- - - \n- - - \n- - - \n", new Board().toString());
	Board b = new Board();
	b.move(1, 1, 1);
	assertEquals("- - - \n- x - \n- - - \n", b.toString());
}
```

**Your turn.** Add one more `move` and `assertEquals` to this test. Make sure it puts an o (`-1`) somewhere.
### winner

`winner` returns `1` if x won, `-1` if o won, and `0` if nobody has won yet.

There are 8 ways to win: 3 rows, 3 columns, and 2 diagonals. Most of the code is below. You fill in `diagonalWon`.

```java
/** @return whether all three squares belong to the same player */
private static boolean setWon(int a, int b, int c) {
	return a != 0 && a == b && b == c;
}

/** @return whether row i or column i has been won */
private boolean rowOrColWon(int i) {
	return setWon(board[i][0], board[i][1], board[i][2]) ||
		   setWon(board[0][i], board[1][i], board[2][i]);
}

/** @return whether either diagonal has been won */
private boolean diagonalWon() {
	return false; // replace this!
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

That `return false` is only there so your code compiles. You'll replace it with your own code.

Grab a pen and paper and draw a board with the row and column numbers on it. Then go through the code.

A few questions to ask yourself:

- Why does `setWon` check `a != 0`? (What happens on an empty board if it doesn't?)
- Why does `winner` return `board[i][i]`? (Hint: that square is in row `i` *and* column `i`.)
- Which squares make up the two diagonals?

The answer to that last one is how you write `diagonalWon`. When you're done, this test should pass:

```java
@Test
public void winner() {
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

	Board b4 = new Board();
	b4.move(-1, 0, 2);
	b4.move(-1, 1, 1);
	b4.move(-1, 2, 0);
	assertEquals(-1, b4.winner());
}
```

*Notice we're cheating a little in these tests: x moves a bunch of times in a row. That's fine. `Board` doesn't keep track of turns. The `Game` class will handle that later.*
### over

A game is over when:

1. someone has won, **or**
2. the board is full

You can use `winner()` for the first one. For the second, loop over every square with nested for loops (just like in `toString`) and look for a `0`.

```java
public boolean over() {
	return false; // replace this!
}
```

Same deal as before: `return false` just keeps your code compiling until you write the real thing.

It should pass this test:

```java
@Test
public void over() {
	Board bWon = new Board();
	bWon.move(1, 0, 2);
	bWon.move(1, 1, 1);
	assertFalse(bWon.over());
	bWon.move(1, 2, 0);
	assertTrue(bWon.over());

	Board bFull = new Board();
	bFull.move(1, 0, 0);
	bFull.move(1, 0, 1);
	bFull.move(-1, 0, 2);
	bFull.move(-1, 1, 0);
	bFull.move(-1, 1, 1);
	bFull.move(1, 1, 2);
	bFull.move(1, 2, 0);
	bFull.move(1, 2, 1);
	bFull.move(-1, 2, 2);
	assertEquals(0, bFull.winner());
	assertTrue(bFull.over());
}
```

These moves fill `bFull` like this:

```
x x o
o o x
x x o
```

The board is full and nobody won. That's a tie, and ties are easy to forget about, so we test them. If you want to check it, play those nine moves on paper.
### Update move (again)

Once someone wins, nobody should be able to keep playing. Update `move` so it throws an exception if the game is already over.

Here's the final version of the `move` test:

```java
@Test
public void move() {
	Board b = new Board();
	b.move(1, 2, 0);
	assertEquals(1, b.get(2, 0));
	b.move(-1, 1, 1);
	assertEquals(-1, b.get(1, 1));
	// player has to be 1 or -1
	assertThrows(RuntimeException.class, () -> b.move(0, 2, 2));
	// square has to be on the board
	assertThrows(RuntimeException.class, () -> b.move(1, 3, 0));
	// can't play in a square that's already taken
	assertThrows(RuntimeException.class, () -> b.move(-1, 2, 0));
	b.move(1, 0, 0);
	b.move(1, 1, 0);
	// can't move after someone already won
	assertThrows(RuntimeException.class, () -> b.move(1, 2, 2));
}
```

Run **all** your tests. If they're all green, your `Board` is done!
## Game

*Now's a great time to commit and push your code.*

Time to make it playable. Make `Game.java`:

```java
package tictactoe;

import java.util.Scanner;

public class Game {
	public static final Board board = new Board();
	public static int currentPlayer = 1;
	public static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {

	}
}
```

- `board` is the one board for this game.
- `currentPlayer` is whose turn it is. x (`1`) goes first.
- `sc` is a `Scanner`. It reads what the player types. You'll only need `sc.nextInt()`, which reads the next number they type. (Here are the [Scanner docs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Scanner.html) if you're curious.)
### Version 1

Start with the simplest game that works. Use a `while` loop that keeps going until the board is over. Each time through the loop is one turn.

Fill in `main`:

```java
public static void main(String[] args) {
	while (!board.over()) {
		// 1. print the board
		// 2. print whose turn it is
		// 3. ask for a row and a column
		// 4. make the move
		// 5. switch players (multiply currentPlayer by -1)
	}
	// print the board one last time
	// print who won (or that it's a tie)
}
```

Two tips below will help with step 3 and the end.
#### Getting the row and column

Use `sc.nextInt()` to read a number. People count from 1, but Java arrays count from 0, so subtract 1:

```java
System.out.println("What row (1-3) will you move in?");
int row = sc.nextInt() - 1;
```

Do the same thing for the column.
#### Ternary operators

At the end you need to print either "It's a tie" or "The winner is x". You could use an if/else. Or you could use a *ternary operator*, which is an if/else squished into one expression:

```java
condition ? valueIfTrue : valueIfFalse
```

Here's a tiny example:

```java
public static double max(double a, double b) {
	return a > b ? a : b;
}
```

If `a > b`, you get `a`. Otherwise you get `b`.

For your game, the ending might look like this:

```java
int winner = board.winner();
System.out.println("Game over! " +
				  (winner == 0 ? "It's a tie" :
								 "The winner is " +
								 Board.playerToString(winner) + "!!"));
```

Now run `Game` and play a round with a friend (or yourself). You type your answers in the terminal at the bottom of VSCode.
### Version 2

Try this: when it's your turn, pick a square that's already taken.

The whole game crashes! That's your `move` method throwing an exception, which is what you told it to do. It's great for catching bugs, but bad for a game.

You can **catch** an exception so it doesn't crash the program:

```java
try {
	// code that might throw an exception
} catch (RuntimeException e) {
	// what to do if it does
}
```

**Your turn.** Wrap the `move` call in a `try`/`catch`. If the move doesn't work, print something like "You can't go there! Try again." and **don't** switch players.

*Hint: put the "switch players" line inside the `try`, right after `move`. It only runs if `move` didn't throw.*

Play again and try to break it. Pick taken squares. Type `5` for a row. Your game should keep going.
### Stuck?

Try on your own first! If you're really stuck, here's one way to write `main`:

```java
public static void main(String[] args) {
	while (!board.over()) {
		System.out.println(board);
		System.out.println("It's " + Board.playerToString(currentPlayer) + "'s turn!");

		System.out.println("What row (1-3) will you move in?");
		int row = sc.nextInt() - 1;
		System.out.println("What column (1-3) will you move in?");
		int column = sc.nextInt() - 1;

		try {
			board.move(currentPlayer, row, column);
			currentPlayer *= -1;
		} catch (RuntimeException e) {
			System.out.println("You can't go there! Try again.");
		}
	}

	System.out.println(board);
	int winner = board.winner();
	System.out.println("Game over! " +
					  (winner == 0 ? "It's a tie" :
									 "The winner is " +
									 Board.playerToString(winner) + "!!"));
}
```
## You did it!

You built a whole game, and you wrote tests that prove your `Board` works. Commit and push!

Want more? Try one of these:

- Typing a letter instead of a number still crashes the game. Can you fix it? (*Hint: look up `hasNextInt()` on [Scanner](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Scanner.html).*)
- Ask "Play again? (y/n)" when the game ends.
- Replace the `1`, `-1`, and `0` with an [enum](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) called `Player`.
- Make a computer player that picks a random empty square.
