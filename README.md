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
	
	To swap reply with question hit ctrl+alt+w. When a swap is done the current flash card is replaced by a new one.

* [DONE] Possibility to read several flash card sets and alternate between them
	
	When you enter ctrl+alt+s to read a new flash card set now you have to supply a name for the set. For switching the set just hit ctrl+alt+s with no selection and enter the name of the set for which you would like to switch.

* [DONE] Possibility of loading the flash card sets through a file
	
	Write the text "file" on the editor, without the quotes, select it, hit ctrl+alt+s and insert the path to your file. Hit enter. The flash card sets there will be read to memory. The example format of the file can be viewed on the [example file](https://raw.githubusercontent.com/Mashashi/flashcard/master/flash_card_sets_example-animals_and_mamals.txt).

* Limitation of time per flashcard

* Get the minimum distance edit ocorrence after 5 wrongs

* Show wrongs more often

* Display statistics like histogram of corrects and histogram of wrongs

##Observations

* You don't have several instances of the flash cards you get only one.

* You are not forced to run the flash cards in the file that opens. You can hit ctrl+alt+space and all text in that document will be deleted and you will be presented with a flash card.

* You may get the response correct and the second flash card be the same.

* If you don't make a valid selection you will see the message invalid selection on the status bar and the flashcards plugin will not load the data.

