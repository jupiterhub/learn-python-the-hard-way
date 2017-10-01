# Character Encoding, if , lists
import sys # note: from not specified; import all

script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    # line has a value ie. not empty string?
    if line:    # if not empty, note ":"
        print_line(line, encoding, errors)
        # works even without 'return, added by book for clarity
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # .strip() - create a copy, remove whitespace
    next_lang = line.strip()

    # .encode() - encode to see the unicode value (in hex)
    #  (UTF-8) means using 8bits and escaping it to display the common 32 bits of data.
    # we don't use 32 bit encoding because it'll take more space
    # UTF-16 covers all known emjois, and languages (even uncommon ones)
    # Thus, “Unicode Transformation Format 8 Bits.”
    # errors=errors -  lots of params, override this only
    # if your DB does not support UTF-8 it is better to encode, otherwise you can skip it
    # DBES (Decode Bytes, Encode Strings) think "deebess, or the best"
    raw_bytes = next_lang.encode(encoding, errors=errors)

    # you can also chose not to override
    cooked_string = raw_bytes.decode(encoding, errors)

    print(raw_bytes, "<===>", cooked_string)

#  encoding="utf-8" - lots of params, override this only
languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
