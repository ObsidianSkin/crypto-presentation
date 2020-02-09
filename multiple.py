#Credit to https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/

"""
# Initialize variable to store each value of each character.
scores = []
# Iterate over each character and make each character lowercase
for byte in input_bytes.lower()
    # Change the byte value to a string, and look up the
    # character in the character_frequencies variable. If the
    # character doesn’t exist in the dictionary, make the value 0.
    score = character_frequencies.get(chr(byte), 0)
    # Add the score to the list of scores
    scores.append(score)
# Sum and return the score
return sum(scores)
"""

def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def main():
    f = open("file", "r") #opening file
    #some global-er variables
    highest_score = 0
    best_message = {
                'message': '',
                'score': 0,
                'key': 0
            }
    #Reading each line of file
    for line in f:
        hexstring = line

        ciphertext = bytes.fromhex(hexstring)
        potential_messages = []

        for key_value in range(256):
            message = single_char_xor(ciphertext, key_value)
            score = get_english_score(message)
            data = {
                'message': message,
                'score': score,
                'key': key_value
                }
            potential_messages.append(data)
        best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
        #Added this bit
        if best_score['score'] > highest_score:
            highest_score = best_score['score']
            best_message = best_score

    #After loop
    for item in best_message:
        print("{}: {}".format(item.title(), best_message[item]))

if __name__ == '__main__':
    main()
