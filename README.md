# AES
AES encryption decryption algorithms in python

Note: My program takes input from user using input() method. So, after running the
aestest file it will ask for input string to be entered.

aestest:

Takes input string from user and generates a new key using secrets library.
Then it converts the hexadecimal key into array (matrix) of hexadecimal values of the key and passes the plaintext and the hexadecimal key array to encryption function in aesencrypt file.
The aesencrypt file prints the ciphertext and returns the ciphertext to aestest file.
Then aestest file passes the returned ciphertext to aesdecrypt along with the generated hexadecimal key array.

aesencrypt:

Converts the plaintext string into an array of hexadecimal values and calls key expansion function and generates an array of long (11 words) key from the input key that will be used in every round for encryption.
Also, while converting the input string to hex, it will check for the length of the input whether it is 128 bits or not and will apply padding accordingly. And it will generate list of matrices of 128 bits of hexadecimal plaintext blocks.
Then first word of expanded key (128 bits) which is the original key is XORed with the plaintext which generates input for first round of the cipher.
Then the function iterates through a loop for 9 times and calls 4 different functions in the loop – subBytes, shiftRows, mixColumns, addRoundKey.

• subBytes: Takes the output of the previous round and substitutes each pair of hexadecimal value with a new pair of hexadecimal value based on the sbox matrix given.
• shiftRows: Takes the output of subBytes and shifts the rows of the output matrix according to the subBytes specifications of AES.
• mixColumns: Takes the output of shiftRows and multiplies the matrix with a fixed matrix mentioned in AES encryption.
• addRoundKey: Takes the output of mixColumns and takes one word from expanded key according to the current round and XORes the two inputs to generate the final output of the round.

The final output of 9th round is the again given to subBytes function then to shiftRows and then to addRoundKey to generate the final cipher.
Then this cipher is converted to a single dimensional array of hexadecimal values and printed on the console.
Key Expansion: A 16 bytes (4 words) key is expanded to 176 bytes (44 words) key so that each round mentioned above can use different 16 bytes of the expanded key. Key expansion is done by applying functions – rotWord, subWord, and XOR with a unique round value.

• rotWord: Rotates each word of the key (4 bytes of a row) according to the AES specifications.
• subWord: Works in same way as subBytes.
• XOR with a hexadecimal number in each round.

These above functions are only applied to first word of the key.
Then the output is XORed with the output of previous round.

aesdecrypt:

It will get input from aestest, and the input will be cipher text which will be hexadecimal array, and a key generated by aestest which will be a hexadecimal array as well.
Calls key expansion function and generates an array of long (11 words) key from the input key that will be used in every round for decryption.
Then first word of expanded key (128 bits) which is the original key is XORed with the ciphertext which generates input for first round of the function.
Then the function iterates through a loop for 9 times and calls 4 different functions in the loop – invShiftRows, invSubBytes, addRoundKey, invMixColumns.

• invShiftRows: Takes the output of previous round and shifts the rows of the output matrix according to the subBytes specifications of AES for decryption (reverse from encryption).
• invSubBytes: Takes the output of the invShiftRows and substitutes each pair of hexadecimal value with a new pair of hexadecimal value based on the sbox matrix given which is inverse of the encryption.
• addRoundKey: Takes the output of invSubBytes and takes one word from expanded key according to the current round and XORes the two inputs.
• invMixColumns: Takes the output of addRoundKey and multiplies the matrix with a fixed matrix mentioned in AES decryption to generate the final output of the round.

The final output of 9th round is the again given to invShiftRows function then to invSubBytes and then to addRoundKey to generate the final decrypted plaintext.
Then this cipher is converted to a string from an array of hexadecimal values and printed on the console.
