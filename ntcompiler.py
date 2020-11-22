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
            with open(route, 'r', encoding='UTF8') as file:
                file = file.readlines()
            for lines in file:
                self.desc += lines
        except:
            print("[nt] ERROR OCCURED WHILE LOADING NODETYPE")
            print("[nt] FOR MORE INFO : CONTACT locha0305@naver.com")
    def readdesc(self):
        try:
            self.parse = ""
            word = ""
            paren = " {}():"
            self.mother = None
            cursor = 0
            is_string = False
            while cursor < len(self.desc):
                letter = self.desc[cursor]
                if letter in paren:
                    if not(is_string):
                        if letter == " ":
                            self.parse += word + " "
                            try:
                                if self.desc[cursor + 1] == "{":
                                    pass
                                else:
                                    word = ""
                            except:
                                word = ""
                        elif letter == "\n":
                            self.parse += word + "\n"
                            try:
                                if self.desc[cursor + 1] == "{":
                                    pass
                                else:
                                    word = ""
                            except:
                                word = ""
                            word = ""
                        elif letter == ":":
                            left_indi = word
                            word = ""
                            jump = 0
                            while letter[jump] != "\n" and letter[jump] != " ":
                                jump += 1
                                word += letter[jump]
                            right_indi = word
                            word = ""
                            cursor += (jump - 1)
                            self.node[self.mother][left_indi] = right_indi
                        elif letter == "{":
                            if self.desc[cursor - 1] == " " or self.desc[cursor - 1] == "\n":
                                self.mother = word
                                self.node[word] = {}
                                word = ""
                            else:
                                self.mother = word
                                self.node[word] = {}
                                word = ""
                cursor += 1
        except:
            print("[nt] ERROR OCCURED WHILE COMPILING")
            print("[nt] FOR MORE INFO : CONTACT locha0305@naver.com")
