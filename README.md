# flashcard

A plugin for sublime that helps to memoraize like you would with flash cards.

## Compatibility

Developed and tested under Sublime 3 and Windows 7 x64

## Usage

1. Type a pair of words separated by a tab in each line of a file
	
	+ The 1st sequence of the characters is the question
	+ The 2nd is the expected reply

2. Select the lines that you would like to see as question on the flash card

3. Press ctrl+alt+s

4. A new tab appears with a random selected question

5. Type the reply you think is correct on the second line

6. Press ctrl+alt+space to check your answer

	On the status bar at the end you will see one of two things:
	+ "wrong" and the question doesn't change
	+ "correct" and a new question appears

![alt tag](https://raw.githubusercontent.com/Mashashi/flashcard/master/demo.gif)

##Roadmap

* [DONE] If invalid tell invalid line

* [DONE] Swap questions and replies 

* Limitation of time per flashcard

* Get the minimum distance edit ocorrence after 5 wrongs

* Show wrongs more often

* Display statistics like histogram of corrects and histogram of wrongs

* Possibility to read several flash card sets and alternate between them

##Observations

* You don't have several instances of the flash cards you get only one.

* You are not forced to run the flash cards in the file that opens. You can hit ctrl+alt+space and all text in that document will be deleted and you will be presented with a flash card.

* You may get the response correct and the second flash card be the same.

* If you don't make a valid selection you will see the message invalid selection on the status bar and the flashcards plugin will not load the data.

* To swap reply with question hit ctrl+alt+w. When a swap is done the current flash card is replaced by a new one.