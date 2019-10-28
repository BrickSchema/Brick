# brick-convert

## Install dependencies
```bash
pip3 install -r requirements.txt
```

## Help
```bash
python3 update.py --help     
```

## Usage
```bash
python3 update.py --source 1.0.2 --target 1.1.0 ../../examples/ebu3b_brick.ttl 
```

For multiple files, use glob patterns or filenames separated by whitespaces.
```bash
python3 update.py --source 1.0.2 --target 1.1.0 ../../examples/*.ttl
```
