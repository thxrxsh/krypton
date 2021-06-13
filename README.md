# krypton
Usefull python scripts to slove overthewire krypton levels

- frequency_analyzer.py

    + Usage:
        frequency_analyzer.py [-h] [-f FILE] [-g GROUP_SIZE]
        
    + Optional arguments:
       + -h , --help                                 Show help message and exit.
       + -f FILE, --file FILE                        Name of the file that you want to analyze.
       + -g GROUP_SIZE, --group_size GROUP_SIZE      Number of letters that you want to group. Set this to 1, if you want to analyze letter by letter.




- vignereCipher_keyShifter.py

    + Usage:
        vigenereCipher_keyShifter.py [-h] [-f FILE] [-g GROUP_SIZE] [-s SHIFT]
        
    + Optional arguments:
       + -h, --help                                   Show help message and exit.
       + -f FILE, --file FILE                         Name of the file that you want to shift keys from.
       + -g GROUP_SIZE, --group_size GROUP_SIZE       Number of the characters that you want to group together. You need to specify this number according to the character length of the encryption key
       + -s SHIFT, --shift SHIFT                      Index number of the key that you want to shift from a each group. The index starts from 0.

    



- vigenereCipher_decoder.py

    + Usage:
        vigenereCipher_decoder.py [-h] [-f FILE] [-t TEXT] [-k KEY]
        
    + Optional arguments:
         + -h, --help                                Show help message and exit.
         + -f FILE, --file FILE                      Vigenere Cipher text contained file that you want to decode.
         + -t TEXT, --text TEXT                      Vigenere Cipher text that you want to decode.
         + -k KEY, --key KEY                         The key to decode Vigenere Cipher
 
         ** You can't specify [FILE] ( -f / --file ) and [TEXT] ( -t / --text ) together
         
