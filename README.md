
# Bangla Tokenizer

A simple Bangla text tokenizer that breaks a given Bangla sentence into smaller tokens for further processing. It removes unnecessary punctuation, preserves Bangla and English words, and ensures proper tokenization of mixed-language text.

## Features
- Supports Bangla and English words.
- Removes punctuation except for necessary word characters.
- Replaces Bangla sentence-ending punctuation (`।`) with a space.
- Works well for both Bangla and mixed Bangla-English text.

## Installation
No external dependencies are required. This script runs with Python 3.x.

## Usage
Run the script and input your text:

```sh
python tokenizer.py
```

Then, enter a Bangla sentence when prompted.

### Example
#### **Input:**
```
আমার নাম রাহুল। আমি Python শিখছি!
```
#### **Output:**
```
টোকেন: ['আমার', 'নাম', 'রাহুল', 'আমি', 'Python', 'শিখছি']
```

## License
This project is open-source and available for modification and improvement.
