from SpecialTokens import KEYWORDS, OPERATORS, DELIMITERS


class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.token_type = token_type

    def __str__(self):
        return f"Token({self.value}, {self.token_type})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_position = 0

    def tokenize(self):
        while self.current_position < len(self.source_code):
            current_char = self.source_code[self.current_position]

            if current_char.isspace():
                self.current_position += 1
            elif current_char.isalpha() or current_char == '_':
                self.tokens.append(self._identify_identifier())
            elif current_char.isdigit():
                self.tokens.append(self._identify_number())
            elif current_char in OPERATORS:  # 使用 OPERATORS
                self.tokens.append(self._identify_operator())
            elif current_char in DELIMITERS:  # 使用 DELIMITERS
                self.tokens.append(self._identify_delimiter())
            else:
                # Unrecognized character
                self.current_position += 1

        return self.tokens

    def _identify_identifier(self):
        start_position = self.current_position
        while (self.current_position < len(self.source_code) and
               (self.source_code[self.current_position].isalnum() or
                self.source_code[self.current_position] == '_')):
            self.current_position += 1

        value = self.source_code[start_position:self.current_position]
        token_type = "keyword" if value in KEYWORDS else "identifier"  # 使用 KEYWORDS
        return Token(value, token_type)

    def _identify_number(self):
        start_position = self.current_position
        while self.current_position < len(self.source_code) and self.source_code[self.current_position].isdigit():
            self.current_position += 1

        value = self.source_code[start_position:self.current_position]
        return Token(value, "constant")

    def _identify_operator(self):
        op = self.source_code[self.current_position]
        self.current_position += 1
        return Token(op, "operator")

    def _identify_delimiter(self):
        delim = self.source_code[self.current_position]
        self.current_position += 1
        return Token(delim, "delimiter")


# Example usage
source_code = "int x = 5 + 3; if (x > 3) { x = 1; }"
lexer = Lexer(source_code)
tokens = lexer.tokenize()
for i in tokens:
    print(i)
