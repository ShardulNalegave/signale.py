
<div align="center" id="main">
	<h1 align="center">Signale.py</h1>
	<p align="center">Elegant Console Logger For Python Command-Line Apps</p>
	<br>
	<br>
	<img src="./imgs/main.png" alt="example" align="center">
</div>

<hr>



## Installation
**Signale.py** can be installed using pip.

````bash

    [sudo] pip install signalepy

````



## Usage
Package consists of a class `Signale`, it is the main constructor class. The object created has all the logger functions in it.


### Using Loggers
Each logger function takes in three arguments:-
- `text`
- `prefix` ( Optional )
- `suffix` ( Optional )

They all are available in the logger object. To create one do this:-
````python

    from signalepy import Signale

    logger = Signale()

````

Now you can use the default loggers using this object like:-
````python

    ...

	logger.success("Started Successfully", prefix="Debugger")
	logger.warning("`a` function is deprecated", suffix="main.py")
	logger.complete("Run Complete")

    ...

````


This will produce the following result:-

<div align="center">
	<img align="center" src="./imgs/result.png">
</div>

<br><br>

<details>
	<summary>View All Available Loggers</summary>

- `simple`
- `success`
- `error`
- `warning`
- `start`
- `stop`
- `watch`
- `important`
- `pending`
- `complete`
- `debug`
- `pause`
- `info`
- `center`

</details>



----------------------------------------------------------------------------------------------------------



## API

signalepy.`<logger>(message="", prefix="", suffix="")`

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



----------------------------------------------------------------------------------------------------------



**Licensed Under [MIT License](https://github.com/ShardulNalegave/signale.py/blob/master/LICENSE)**
**A Project By [Shardul Nalegave](https://shardul.netlify.com)**