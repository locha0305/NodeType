import sys
import os
import datatype as dt





def init():
    version = 0.1
    author = "locha"
    github = ""
    email = "locha0305@naver.com"
    print("NodeType v{}".format(version))
    print("developed by {}".format(author))
    print("github : {}".format(github))
    print("email : {}".format(email))





class ntobject():
    def __init__(self, route):
        try:
            self.desc = ""
            self.node = {}
            with open(route, 'r', encoding='UTF-8') as file:
                file = file.readlines()
            for lines in file:
                self.desc += lines
            self.readdesc()
        except:
            print("[nt] ERROR OCCURED WHILE LOADING NODETYPE FILE")
        
    def readdesc(self):
        try:
            word = ""
            paren = " {}():"
            self.mother = None
            is_paren_open = False
            cursor = 0
            is_string = False
            print(self.desc)
            while cursor < len(self.desc):
                letter = self.desc[cursor]
                if not(is_string):
                    if letter in paren:
                        if letter == " ":
                            word = ""
                        elif letter == "\n":
                            word = ""
                        elif letter == ":":
                            left_indi = word.strip('\n')
                            print(word)
                            word = ""
                            jump = 1
                            right_indi_is_string = False
                            string_indi = False
                            while self.desc[cursor + jump] != "\n" and not(is_string):
                                if self.desc[cursor + jump] == '"' and not(is_string):
                                    is_string = True
                                    string_indi = True
                                if self.desc[cursor + jump] == '"' and is_string:
                                    is_string = False
                                    right_indi_is_string = True
                                    string_indi = True
                                else:
                                    pass
                                if not(string_indi):
                                    word += self.desc[cursor + jump]
                                else:
                                    string_indi = False
                                jump += 1
                            cursor += jump
                            right_indi = word.strip("\n")
                            print(left_indi)
                            print(word)
                            if right_indi_is_string:
                                self.node[self.mother][left_indi] = right_indi
                            else:
                                if dt.is_int(right_indi):
                                    self.node[self.mother][left_indi] = int(right_indi)
                                elif dt.is_float(right_indi):
                                    self.node[self.mother][left_indi] = float(right_indi)
                                elif dt.is_bool(right_indi):
                                    self.node[self.mother][left_indi] = bool(right_indi)
                            word = ""
                        elif letter == "{":
                            self.mother = word.strip('\n')
                            print(self.mother)
                            self.node[self.mother] = {}
                            word = ""
                            is_paren_open = True
                        elif letter == "}":
                            self.mother = None
                            word = ""
                            is_paren_open = False
                    else:
                        word += letter
                cursor += 1
        except:
            print("[nt] ERROR OCCURED WHILE COMPILING")
