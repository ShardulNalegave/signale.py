#!/usr/bin/env python


"""

	author: Shardul Nalegave
	license:

		MIT License

		Copyright (c) 2018 Shardul Nalegave

		Permission is hereby granted, free of charge, to any person obtaining a copy
		of this software and associated documentation files (the "Software"), to deal
		in the Software without restriction, including without limitation the rights
		to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
		copies of the Software, and to permit persons to whom the Software is
		furnished to do so, subject to the following conditions:

		The above copyright notice and this permission notice shall be included in all
		copies or substantial portions of the Software.

		THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
		OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
		SOFTWARE.

"""



__version__ = '0.1.0'


import os
import sys
from sys import platform, stdout


class Signale:

	def __init__(self, opts={"scope": None}):

		scope = opts["scope"]

		if scope != None:
			self.scope = scope if scope != "" else "global"
		else:
			self.scope = None

		if platform == "win32":
			self.figures = {
				"pause": "||",
				"tick": '√',
				"cross": '×',
				"star": '*',
				"squareSmallFilled": '[█]',
				"play": '►',
				"bullet": '*',
				"ellipsis": '...',
				"pointerSmall": '»',
				"info": 'i',
				"warning": '‼',
				"heart": '♥',
				"radioOn": '(*)',
				"radioOff": '( )'
			}
		else:
			self.figures = {
				"pause": "||",
				"tick": '✔',
				"cross": '✖',
				"star": '★',
				"squareSmallFilled": '◼',
				"play": '▶',
				"bullet": '●',
				"ellipsis": '…',
				"pointerSmall": '›',
				"info": 'ℹ',
				"warning": '⚠',
				"heart": '♥',
				"radioOn": '◉',
				"radioOff": '◯'
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
			"pink": "\u001b[38;5;198m",
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
		if self.scope != None:
			if isinstance(self.scope, list):
				message = "   " + message
				scopes = ""
				for item in self.scope:
					scopes += f" \u001b[38;5;248m[{item}]\u001b[0m"
				if prefix == "":
					pointer = self.figures["pointerSmall"]
					message = f"  \u001b[38;5;248m{scopes} \u001b[38;5;248m{pointer}\u001b[0m" + message
				else:
					message = f" \u001b[38;5;248m{scopes}\u001b[0m" + message
			else:
				if prefix == "":
					pointer = self.figures["pointerSmall"]
					message = f"   \u001b[38;5;248m[{self.scope}] \u001b[38;5;248m{pointer}\u001b[0m" + message
				else:
					message = f"   \u001b[38;5;248m[{self.scope}]\u001b[0m" + message
				# message = f"   \u001b[38;5;248m[{self.scope}]\u001b[0m" + message
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
		icon = self.figures["radioOff"]
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
		icon = self.figures["radioOn"]
		text = "{}:  {}".format(self.coloured("very light blue", "{} Complete".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def like(self, text="", prefix="", suffix=""):
		icon = self.figures["heart"]
		text = "{}:  {}".format(self.coloured("pink", "{} Like".format(icon)), text)
		message = self.logger(text=text, prefix=prefix, suffix=suffix)
		print(message)

	def center(self, text="", prefix="", suffix=""):
		rows, cols = os.popen('stty size', 'r').read().split()
		rows, cols = int(rows), int(cols)
		text = "-" * 10 + "  " + text + "  " + "-" * 10
		len_text = len(text)
		message = " " * ((cols - len_text) // 2) + text + " " * ((cols - len_text) // 2)
		print(message)



# s = Signale()
# s.center("Testing Logger")
# s.simple("ABC", prefix="Debugger", suffix="xyz")
# s.info("Starting", prefix="Debugger")
# s.success("Started Successfully", prefix="Debugger", suffix="xyz")
# s.watch("Watching All Files", prefix="Debugger")
# s.error("Something Went Wrong", prefix="Debugger")
# s.warning("Deprecation Warning", prefix="Debugger")
# s.pending("Postponed", prefix="Debugger")
# s.debug("Found A Bug on L55", prefix="Debugger")
# s.start("Started New Process", prefix="Debugger")
# s.pause("Process Paused", prefix="Debugger")
# s.complete("Task Completed", prefix="Debugger")
# s.important("New Update Available. Please Update!", prefix="Debugger")
# s.like("I Love Signale", prefix="Debugger")
# s.stop("Stopping", prefix="Debugger")

# print("\n")

# logger = Signale("")
# logger.success("Started Successfully", prefix="Debugger")
# logger.warning("`a` function is deprecated", suffix="main.py")
# logger.complete("Run Complete")

# print("\n")

# logger = Signale("custom")
# logger.success("Started Successfully", prefix="Debugger")
# logger.warning("`a` function is deprecated", suffix="main.py")
# logger.complete("Run Complete")

# logger = Signale({
# 	"scope": ["global scope", "inner scope"]
# 	# "scope": "global scope"
# })
# logger.success("Scoped Logger Works!")