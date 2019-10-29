how to initialize:

Make sure that you have the [mtools tool installed](https://github.com/rueckstiess/mtools).
Edit the `config.yaml` file as necessary


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

Run the data population script:
```bash
(venv) $ python scripts/setup_test_data.py single
(venv) $ python scripts/setup_test_data.py shard
```

View your data in [Mongo Compass](https://www.mongodb.com/products/compass).