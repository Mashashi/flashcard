import sublime, sublime_plugin, random, math, re

FLASH_CARD_SEP = "\n"
LIST_FLASH_CARDS_SEP = "\n"
LIST_FLASH_CARD_SEP = "\t"

class FlashCardCommand(sublime_plugin.TextCommand):

	sels = []
	line_count = 0

	def run(self, edit, operation=None):
		

		if operation == "correct_flash_card":
			body = getBodyFlashCard(self.view)
			line = Line(body, FLASH_CARD_SEP)
			result = newFlashCard(line.question, line.reply)
			if result: initQuestion(edit)

		elif operation == "swap_map":
			for part in FlashCardCommand.sels:
				part.swap()
			initQuestion(edit)
			sublime.status_message("swap done")

		else:
			[valid, invalid_line] = validSelection(self.view)
			if valid:
				new_view = setup(self.view, edit)
				initQuestion(edit, new_view)
			else:
				sublime.status_message("invalid selection: " + invalid_line)



def getBody(view):
	body = view.substr(sublime.Region(0, view.size()))
	return body

def getBodyFlashCard(view):
	body = view.substr(sublime.Region(0, view.size()))
	if body.count(FLASH_CARD_SEP) != 1: body = FLASH_CARD_SEP
	return body

def getSelection(view):
	return view.substr(view.sel()[0])

def getLine():
	pick_idx = math.floor(random.random()*FlashCardCommand.line_count)
	picked_line = FlashCardCommand.sels[pick_idx]
	return picked_line



def validSelection(view):
	body = getSelection(view)
	valid = False
	invalid = None
	parts = body.split(LIST_FLASH_CARDS_SEP)
	for part in parts:
		valid = part.count(LIST_FLASH_CARD_SEP) == 1
		if not(valid): 
			invalid = part 
			break
	return [valid, part]

def setup(view, edit):
	window = sublime.active_window()
	window.new_file()
	new_view = window.active_view()
	sels = getSelection(view)
	FlashCardCommand.sels = list(map(Line, sels.split(LIST_FLASH_CARDS_SEP)))
	FlashCardCommand.line_count = len(FlashCardCommand.sels)
	return new_view

def initQuestion(edit, view = None):
	if view == None: view = sublime.active_window().active_view()
	view.erase(edit, sublime.Region(0, view.size()))
	view.insert(edit, 0, getLine().flash_card)




def newFlashCard(question, reply):
	response = None

	for sel in FlashCardCommand.sels:
		if question == sel.question:
			response = False
			if reply == sel.reply:
				response = True
				break
	
	if response != None: sublime.status_message( 'correct' if response else 'wrong' )
	if response == None: response = True

	return response



class Line:
	def __init__(self, line, separator = LIST_FLASH_CARD_SEP):
		if not line: line = separator
		[self.question, self.reply] = line.split(separator)
		self.buildQuestion()
	def swap(self):
		reply = self.reply
		self.reply = self.question
		self.question = reply
		self.buildQuestion()
	def buildQuestion(self):
		self.flash_card = self.question + FLASH_CARD_SEP 
	