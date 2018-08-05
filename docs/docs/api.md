
# API
-------

<br>

1. logger = `Signale(<options>)`

	<br>

	`Signale`

	- Type: `class`

	Signale class imported from `signalepy` module

	<br>

	`options`

	- Type: `dict`

	Options Dictionary for logger.

	<br>

	- Returns: Signale Logger Object

	Logger object which can be used for logging

	<br><br>

2. logger.`<logger>(message="", prefix="", suffix="")`

	<br>

	`logger`

	- Type: `function`

	Can be any default logger

	<br>

	`message`

	- Type: `str`

	Message to be displayed

	<br>

	`prefix`

	- Type: `str`
	- Required: False

	Prefix text

	<br>

	`suffix`

	- Type: `str`
	- Required: False

	Suffix text

	<br>

	- Returns: `None`

	<br><br>

3. logger2 = `logger`.scoped(`<new scope>`)

	<br>

	`logger`

	- Type: Signale Logger Object

	Parent Logger

	<br>

	`new scope`

	- Type: `str`

	New Scope Name

	<br>

	- Returns: Signale Logger Object

	Clone Logger object with extended scope

	<br><br>