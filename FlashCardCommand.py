import sublime, sublime_plugin, random, math, re

FLASH_CARD_SEP = "\n"
LIST_FLASH_CARDS_SEP = "\n"
LIST_FLASH_CARD_SEP = "\t"
FILE_SET_SEPARATOR = "#"

class FlashCardCommand(sublime_plugin.TextCommand):

	selected = None
	sels = {}

	def run(self, edit, operation=None):

		def doneNewSet(txt):
			FlashCardCommand.selected = txt
			FlashCardCommand.sels[FlashCardCommand.selected] = FlashCardCommand.sels[None]
			sublime.status_message("new flash card set: " + txt)
		def doneChangeSet(txt):
			FlashCardCommand.selected = txt
			sublime.status_message("changed to flash card set: " + txt)
		def doneFilePicker(txt):
			f = open(txt, 'r')
			f_contents = f.read()
			f.close()
			sets = f_contents.split(FILE_SET_SEPARATOR)
			for s in sets: newSetRaw(s)
			sublime.status_message("file loaded: " + txt)
			

		if operation == "correct_flash_card":
			body = getBodyFlashCard(self.view)
			line = Line(body, FLASH_CARD_SEP)
			result = newFlashCard(line.question, line.reply)
			if result: initQuestion(edit)

		elif operation == "swap_map":
			for part in getSelectedSet():
				part.swap()
			#initQuestion(edit)
			sublime.status_message("swap done")
		else:
			
			[valid, invalid_line] = validSelection(self.view)
			if valid:
				FlashCardCommand.selected = None
				sublime.active_window().show_input_panel("new name", "", doneNewSet, lambda: None, lambda: None)
				new_view = setup(self.view, edit)
				initQuestion(edit, new_view)
			elif invalid_line == "file":
				sublime.active_window().show_input_panel("file_path", "", doneFilePicker, lambda: None, lambda: None)
			elif invalid_line != "":
				sublime.status_message("invalid selection: " + invalid_line)
			else:
				sublime.active_window().show_input_panel("select name", "", doneChangeSet, lambda: None, lambda: None)
			

def getSelectedSet():
	return FlashCardCommand.sels[FlashCardCommand.selected] if (FlashCardCommand.selected in FlashCardCommand.sels) else None

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
	pick_idx = math.floor(random.random()*len(getSelectedSet()))
	picked_line = getSelectedSet()[pick_idx]
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
	newSet(FlashCardCommand.selected, sels)
	return new_view

def newSetRaw(raw_content):
	lines = raw_content.split(LIST_FLASH_CARDS_SEP)
	content = LIST_FLASH_CARDS_SEP.join(l for l in lines[1:])
	newSet(lines[0], content)

def newSet(name, content):
	sels = list(map(Line, content.split(LIST_FLASH_CARDS_SEP)))
	FlashCardCommand.sels[name] = sels

def initQuestion(edit, view = None):
	if view == None: view = sublime.active_window().active_view()
	view.erase(edit, sublime.Region(0, view.size()))
	view.insert(edit, 0, getLine().flash_card)




def newFlashCard(question, reply):
	response = None
	setSelected = getSelectedSet()

	if setSelected != None:
		for sel in setSelected:
			if question == sel.question:
				response = False
				if reply == sel.reply:
					response = True
					break
		
		if response != None: sublime.status_message( 'correct' if response else 'wrong' )
		if response == None: response = True
	else:
		sublime.status_message("invalid flash card set: " + str(FlashCardCommand.selected))


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