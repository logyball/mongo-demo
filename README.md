how to initialize!

Make sure that you have the [mtools tool installed](https://github.com/rueckstiess/mtools).

Create a python virtualenv with python3:
```bash
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

Install dependencies:
```bash
(venv) $ pip install -r requirements.txt
```

Run the initial setup script (from the root project directory):
```bash
(venv) $ python scripts/setup_mongos.py
```