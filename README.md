
# Text Tokenizer

A simple Python script that breaks a given text into smaller tokens for further processing.

## Features
- Splits text into individual words.
- Retains only lowercase English letters and digits as tokens.
- Replaces specific non-English punctuation (`।`) with spaces.

## Usage

### Prerequisites
- Install Python 3.x

### Running the Script
1. Clone or download the script.
2. Run it using:
   ```sh
   python tokenizer.py
   ```
3. Enter your text when prompted.
4. The script outputs the tokenized list.

## Example
**Input:**
```
এখানে আপনার পাঠ্য লিখুন: Hello, this is a test. বাংলা । example123।
```
**Output:**
```
['Hello,', 'this', 'is', 'a', 'test.', 'বাংলা', 'example123']
```

## License
MIT License.
