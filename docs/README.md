---

home: true
heroImage: /hero.png
actionText: Get Started
actionLine: /docs/
features:
- title: Beautiful Logs
  details: Colourful Logs with icons with scopes, prefixes and suffixes
- title: Hackable
  details: Highly Customizable with the support for Custom Loggers
- title: Loggers + Text Formatters
  details: A huge list of Default Loggers and Text Formatters
footer: MIT Licensed | Copyright © 2018 Shardul Nalegave
sidebar: false
editLink: false

---


## One Line Installation

````bash

	# Available On PyPi - https://pypi.org/project/signalepy
    [sudo] pip install signalepy

````

## Easy To Use

````python

from signalepy import Signale

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
s.like("I Love Signale", prefix="Debugger")
s.stop("Stopping", prefix="Debugger")

````

-----

::: warning COMPATIBILITY NOTE
Signale.py Requires Python >= 3.6
:::