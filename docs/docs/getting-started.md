
::: warning COMPATIBILITY NOTE
Signale.py requires Python >= 3.6 and `pip` installed and on available on `PATH` variable
:::


## Installation
Signale.py is available on **PyPI** ( Python Packing Index ). So, intalling it is very simple. Just run the following command

````bash

    # Optional
    mkdir <dirname> # Create The Project Dir
    cd <dirname>
    virtualenv venv
    . ./venv/bin/activate # Activate The Virtual Environment

    # Install Signale.py
    [sudo] pip install signalepy

````


## Usage
After installing import the `Signale` class from `signalepy` module as it is the constructor class.

Example:-

````python

   # main.py

   from signalepy import Signale

   logger = Signale() # Option can be passed to the constructor
   logger.info("Signale.py is amazing", prefix="Logger")

````

Then run the file using `python` CLI.

````bash

    # If Signale.py is installed in a Virtual Environment, activate it first.
    python[x[.y]] main.py

````

After running it the result will look like:-

![Result](/imgs/usage_result.png)