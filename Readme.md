# FastAPI 

Protected route with JWT.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r --upgrade requirement.txt
```

## Usage

```python
#create .env file for db connection
ie : DB_URL = mysql://user:passwd@localhost:3306/jwt

#migrate
aerich migrate

run project using 
#uvicorn
uvicorn main:app --reload --port=8100 --host=0.0.0.0

#  or run with py
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT]