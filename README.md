Message Encoder/Decoder
This Python script allows you to encode and decode messages using a simple substitution cipher. When encoding, it adds random prefixes and suffixes to the words, and when decoding, it removes these prefixes and suffixes.

Features
Encoding: Adds random prefixes and suffixes to words of length 3 or more.
Decoding: Removes the added prefixes and suffixes to restore the original message.
Usage
Run the Script: Start the script and follow the prompts.
Input Message: Enter the message you want to encode or decode.
Choose Operation: Specify whether you want to perform encoding or decoding.
How It Works
Encoding
For words of length 3 or more:
Adds a random 3-character prefix.
Moves the first character to the end.
Adds a random 3-character suffix.
For words of length less than 3:
Reverses the word.
Decoding
For words of length 3 or more:
Removes the 3-character prefix.
Moves the last character to the front.
Removes the 3-character suffix.
For words of length less than 3:
Reverses the word back.
Example
python
Copy code
Enter the message: Hello World
Enter coding or decoding: coding
# Output: RANDOMellHOrandom RANDOMorldWrandom

Enter the message: RANDOMellHOrandom RANDOMorldWrandom
Enter coding or decoding: decoding
# Output: Hello World
