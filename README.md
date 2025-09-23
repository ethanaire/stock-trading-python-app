# stock-trading-python-app

This uses the Polygon.io API to extract stocks data

## Setup

Create the virtual python envỉonment: Use the `venv` module

```bash
python3 -m venv pythonenv
```

Activate the virtual envỉonment: 

  - On Windows (Command Prompt)
    ```bash
    pythonenv\Scripts\activate.bat
    ```
  
  - On Windows (PowerShell)
    ```bash
    pythonenv\Scripts\activate.ps1
    ```

Install the required libraries using the provided `requirements.txt` file:

```bash
python3 -m pip install -r requirements.txt
```

Run the script:

```bash
python3 script.py
```

Activate and edit `crontab` utility: 

```bash
crontab -e
```

```bash
* * * * * /usr/bin/python3 /path/stock-trading-python-app/script.py
```

Run the Python script every minute: 

```bash
crontab 
```
