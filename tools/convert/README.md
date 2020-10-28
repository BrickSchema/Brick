# brick-convert

## Install dependencies
```bash
pip install -r requirements.txt
```

## Help
```bash
python convert.py --help
```

## Usage
```bash
python convert.py --source 1.0.2 --target 1.1 examples/ebu3b_brick.ttl
```

For multiple files, use glob patterns or filenames separated by whitespaces.
```bash
python convert.py --source 1.0.2 --target 1.1 examples/*.ttl
```
