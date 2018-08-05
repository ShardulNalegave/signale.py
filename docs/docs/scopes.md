
# Scoped Loggers

Loggers can have scopes too. They help in understanding from where the log is ( Eg:- `Debugger`, `Compiler`, etc ).

Scope of a logger is defined by setting the `scope` field of the options dictionary to the scope. `scope` field may have a string value if there is one scope or a list if there are multiple.

Example:-

````python

    from signalepy import Signale

    logger = Signale({
		"scope": "global scope"
	})

	logger.success("Scoped Logger Works!")

````

This will produce the following result:-

![Result](/imgs/scope_str.png)

----

Example with a list:-

````python

	from signalepy import Signale

	logger = Signale({
		"scope": ["global scope", "inner scope"]
	})
	logger.success("Scoped Logger Works!")

````

This will produce the following result:-

![Result](/imgs/scope_list.png)