# Elements Code

encoding text into numbers using periodic table element positions.

## Idea

- Each character is converted to the first letter of an element symbol.
- The output is a list of atomic numbers.
- Decryption turns each number back into the first letter of the element at that position.

Because the periodic table has no symbols starting with `j` or `q`, this project adds:

- `j` as element 119
- `q` as element 120

## How it works

- `Elements.encrypt(text)`
  - Converts text to lowercase.
  - For each character, finds all elements whose symbol starts with that letter.
  - Randomly picks one matching atomic number.
  - Returns a list of integers.

- `Elements.decrypt(cipher)`
  - For each number, takes the element at that position.
  - Uses the first letter of its symbol.
  - Returns the decoded text.

## Files

- `elements.py`: Main `Elements` class (encrypt/decrypt logic).
- `main.py`: Simple usage example.
- `test.py`: Small random test snippet.

## Run

```bash
python main.py
```

Example output will look like:

- Encrypted: `[89, 35, 96, 110, 26, 9]`
- Decrypted: `abcdef`

Note: encrypted numbers can change each run because encryption uses random selection.
