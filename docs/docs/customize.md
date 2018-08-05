
# Configuration


## Options
Options taken by constructor

1. `scope`

	<br>
	
	- Type: `str` or `list`

	Signale Logger Scope

	<br><br>

3. `underlined`

	<br>

	- Type: `bool`

	Labels Should Be Underlined Or Not

2. `custom`

	<br>

	- Type: `list`

	List of custom logger configuration.

	- Configuration Type: `dict`

		Custom Logger Configuration Dictionary

		- Keys

			1. `name`

				- Type: `str`

				Name of the logger

			2. `label`

				- Type: `str`

				Label displayed beside the icon ( colored text )

			3. `badge`

				- Type: `str`

				Icon

			4. `color`

				- Type: `str`

				Color of the icon and label. Should be from:-

				- `red`
				- `dark`
				- `blue`
				- `pink`
				- `green`
				- `grey`
				- `purple`
				- `yellow`
				- `cyan`
				- `reset` (color reset code)

	<br><br>