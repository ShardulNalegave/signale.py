__version__ = '0.1.0'


import os
import sys
from sys import platform, stdout


class Signale:

	def __init__(self):
		if platform == "win32":
			self.figures = {
				"pause": "||",
				"tick": '√',
				"cross": '×',
				"star": '*',
				"square": '█',
				"squareSmall": '[ ]',
				"squareSmallFilled": '[█]',
				"play": '►',
				"circle": '( )',
				"circleFilled": '(*)',
				"circleDotted": '( )',
				"circleDouble": '( )',
				"circleCircle": '(○)',
				"circleCross": '(×)',
				"circlePipe": '(│)',
				"circleQuestionMark": '(?)',
				"bullet": '*',
				"dot": '.',
				"line": '─',
				"ellipsis": '...',
				"pointer": '>',
				"pointerSmall": '»',
				"info": 'i',
				"warning": '‼',
				"hamburger": '≡',
				"smiley": '☺',
				"mustache": '┌─┐',
				"radioOn": '(*)',
				"radioOff": '( )',
				"checkboxOn": '[×]',
				"checkboxOff": '[ ]',
				"checkboxCircleOn": '(×)',
				"checkboxCircleOff": '( )',
				"questionMarkPrefix": '？'
			}
		else:
			self.figures = {
				"pause": "||",
				"tick": '✔',
				"cross": '✖',
				"star": '★',
				"square": '▇',
				"squareSmall": '◻',
				"squareSmallFilled": '◼',
				"play": '▶',
				"circle": '◯',
				"circleFilled": '◉',
				"circleDotted": '◌',
				"circleDouble": '◎',
				"circleCircle": 'ⓞ',
				"circleCross": 'ⓧ',
				"circlePipe": 'Ⓘ',
				"circleQuestionMark": '?⃝',
				"bullet": '●',
				"dot": '․',
				"line": '─',
				"ellipsis": '…',
				"pointer": '❯',
				"pointerSmall": '›',
				"info": 'ℹ',
				"warning": '⚠',
				"hamburger": '☰',
				"smiley": '㋡',
				"mustache": '෴',
				"heart": '♥',
				"arrowUp": '↑',
				"arrowDown": '↓',
				"arrowLeft": '←',
				"arrowRight": '→',
				"radioOn": '◉',
				"radioOff": '◯',
				"checkboxOn": '☒',
				"checkboxOff": '☐',
				"checkboxCircleOn": 'ⓧ',
				"checkboxCircleOff": 'Ⓘ',
				"questionMarkPrefix": '?⃝'
			}

		self.colors = {
			"green": "\u001b[32;1m",
			"grey": "\u001b[38;5;240m",
			"red": "\u001b[38;5;196m",
			"yellow": "\u001b[38;5;11m",
			"purple": "\u001b[38;5;127m",
			"dark blue": "\u001b[38;5;33m",
			"cyan": "\u001b[36;1m",
			"very light blue": "\u001b[38;5;39m",
			"reset": "\u001b[0m"
		}

	def coloured(self, color, text):
		color = self.colors[color]
		reset = self.colors["reset"]
		return f"{color}{text}{reset}"

	def logger(self, text="", prefix="", suffix=""):
		message = ""
		if prefix != "":
			pointer = self.figures["pointerSmall"]
			message = f"  \u001b[38;5;248m[{prefix}] {pointer}\u001b[0m  {text}"
		else:
			message = f"  {text}"
		if suffix != "":
			message += f"   \u001b[38;5;245m-- {suffix}\u001b[0m"
		return message

	def simple(self, text="", prefix="", suffix=""):
		print(self.logger(text, prefix, suffix))

	def success(self, text="", prefix="", suffix=""):
		tick = self.figures["tick"]
		text = "{}:  {}".format(self.coloured("green", "{} Success".format(tick)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def start(self, text="", prefix="", suffix=""):
		icon = self.figures["play"]
		text = "{}:  {}".format(self.coloured("green", "{} Start".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def error(self, text="", prefix="", suffix=""):
		cross = self.figures["cross"]
		text = "{}:  {}".format(self.coloured("red", "{} Error".format(cross)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def warning(self, text="", prefix="", suffix=""):
		icon = self.figures["warning"]
		text = "{}:  {}".format(self.coloured("yellow", "{} Warning".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def watch(self, text="", prefix="", suffix=""):
		icon = self.figures["ellipsis"]
		text = "{}:  {}".format(self.coloured("yellow", "{} Watching".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def stop(self, text="", prefix="", suffix=""):
		icon = self.figures["squareSmallFilled"]
		text = "{}:  {}".format(self.coloured("red", "{} Stop".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def important(self, text="", prefix="", suffix=""):
		icon = self.figures["star"]
		text = "{}:  {}".format(self.coloured("yellow", "{} Important".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def pending(self, text="", prefix="", suffix=""):
		icon = self.figures["circle"]
		text = "{}:  {}".format(self.coloured("purple", "{}  Pending".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def debug(self, text="", prefix="", suffix=""):
		icon = self.figures["squareSmallFilled"]
		text = "{}:  {}".format(self.coloured("dark blue", "{} Debug".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def info(self, text="", prefix="", suffix=""):
		icon = self.figures["info"]
		text = "{}:  {}".format(self.coloured("cyan", "{} Info".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def pause(self, text="", prefix="", suffix=""):
		icon = self.figures["pause"]
		text = "{}:  {}".format(self.coloured("yellow", "{} Pause".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def complete(self, text="", prefix="", suffix=""):
		icon = self.figures["circleFilled"]
		text = "{}:  {}".format(self.coloured("very light blue", "{} Complete".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def center(self, text="", prefix="", suffix=""):
		rows, cols = os.popen('stty size', 'r').read().split()
		rows, cols = int(rows), int(cols)
		text = "-" * 10 + "  " + text + "  " + "-" * 10
		len_text = len(text)
		message = " " * ((cols - len_text) // 2) + text + " " * ((cols - len_text) // 2)
		print(message)



s = Signale()
s.center("Testing Logger")
s.simple("ABC", prefix="Debugger", suffix="xyz")
s.info("Starting", prefix="Debugger")
s.success("Started Successfully", prefix="Debugger", suffix="xyz")
s.watch("Watching All Files", prefix="Debugger")
s.error("Something Went Wrong", prefix="Debugger")
s.warning("Deprecation Warning", prefix="Debugger")
s.pending("Postponed", prefix="Debugger")
s.debug("Found A Bug on L55", prefix="Debugger")
s.start("Started New Process", prefix="Debugger")
s.pause("Process Paused", prefix="Debugger")
s.complete("Task Completed", prefix="Debugger")
s.important("New Update Available. Please Update!", prefix="Debugger")
s.stop("Stopping", prefix="Debugger")