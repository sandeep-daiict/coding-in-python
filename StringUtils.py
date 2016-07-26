__author__ = 'sandeepsharma'

class StringUtils:
    """A String Utility Class in Python"""
    def character_frequency(self,string):
        data = {}
        for c in string:
            if c in data:
                data[c] = data[c] + 1
            else:
                data[c] = 1
        return data

    def duplicate_characters(self,string):
        character_frequency_dictionary = self.character_frequency(string)
        duplicate_chars = []
        for k,v in character_frequency_dictionary.iteritems():
            if v > 1:
                duplicate_chars.append(k)
        return duplicate_chars

    def is_anagram(self,string1,string2):
        character_frequency_dictionary1 = self.character_frequency(string1)
        character_frequency_dictionary2 = self.character_frequency(string2)
        if character_frequency_dictionary1 == character_frequency_dictionary2:
            return True
        return False

    def first_non_repeated_Character_two_pass(self,string):
        character_frequency_dictionary1 = self.character_frequency(string)
        for c in string:
            if character_frequency_dictionary1[c] == 1:
                return c
        return ''



if __name__ == '__main__':
    string_util = StringUtils()
    print(string_util.first_non_repeated_Character_two_pass("sandeepsharma"))
