import json
import chardet

# Determine the encoding of the datadump.json file
with open('datadump.json', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# Load the data from the datadump.json file using the appropriate encoding
with open('datadump.json', 'r', encoding=encoding) as f:
    data = f.read().replace('\x92', '�')  # Replace non-UTF-8 characters with U+FFFD

# Parse the JSON data into a Python object
data = json.loads(data)

# Save the data to a new file using the UTF-8 encoding
with open('new_datadump.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)