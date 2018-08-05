
# Custom Loggers

Sometimes the default loggers may not be enough or yoy may need a different one. At that time you can create your own logger. For example:-

````python

	logger = Signale({
		"scope": "global scope",
		"custom": [
			{
				"badge": "!",
				"label": "Attention",
				"color": "red",
				"name": "attention"
			}
		],
		"underlined": False
	})

	logger.attention("It Works!")

````

The log will look like:-

![Result](/imgs/custom1.png)

---

As you can see a list of custom logger configuration can be passed to the constructor by setting the `custom` field of the option to the list.

The configuration is a dictionary with the following fields:-
- `name`
- `badge`
- `label`
- `color`

To know more about them see [this](./customize.md)

::: warning NOTE
All the fields are required
:::