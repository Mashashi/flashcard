import sublime, sublime_plugin, random, math

class FlashCardCommand(sublime_plugin.TextCommand):

	sels = []
	line_count = 0
	new_view = None

	def run(self, edit, get_selection=False):
		if get_selection:
			
			body = self.view.substr(sublime.Region(0, self.view.size()))
			body = body.split('\n')
			question = body[0]
			reply = body[1]

			result = FlashCardCommand.checkAnswer(question, reply)

			if result:
				FlashCardCommand.initQuestion(FlashCardCommand.new_view, edit)

		else:
			FlashCardCommand.new_view = FlashCardCommand.setup(self.view, edit)
			FlashCardCommand.initQuestion(FlashCardCommand.new_view, edit)





	def initQuestion(view, edit):
		view.erase(edit, sublime.Region(0, view.size()))
		line = FlashCardCommand.getLine()
		question = line.split(' ')[0]
		view.insert(edit, 0, question)

	def checkAnswer(question, reply):
		result = False
		for sel in FlashCardCommand.sels:
			
			sel = sel.split(' ')
			key = sel[0]
			value = sel[1]
			
			if question == key:
				if reply == value:
					sublime.status_message('correct')
					result = True
				else:
					sublime.status_message('wrong')
					result = False

		return result

	def setup(view, edit):
		window = sublime.active_window()
		window.new_file()
		new_view = window.active_view()
		sels = view.sel()
		sels = view.substr(sels[0])
		FlashCardCommand.sels = sels.split("\n")
		FlashCardCommand.line_count = len(FlashCardCommand.sels)
		return new_view
		
	def getLine():
		random_number = random.random()
		pick_idx = math.floor(random_number*FlashCardCommand.line_count)
		pick_line = FlashCardCommand.sels[pick_idx]
		return pick_line