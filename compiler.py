import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f'Token<{self.type}, {self.value}>'

class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.current_position = 0

        # Define keywords
        self.keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'break', 'char', 'const', 'continue', 'default', 'double', 'float', 'include', 'main', 'printf', 'return', 'scanf', 'switch', 'void']

    def scan_tokens(self):
        tokens = []

        while self.current_position < len(self.source_code):
            char = self.source_code[self.current_position]

            # Ignore whitespace
            if char.isspace():
                self.current_position += 1
                continue

            # Check for comments
            if char == '/':
                if self.current_position + 1 < len(self.source_code) and self.source_code[self.current_position + 1] == '/':
                    self.scan_line_comment()
                    continue
                elif self.current_position + 1 < len(self.source_code) and self.source_code[self.current_position + 1] == '*':
                    self.scan_block_comment()
                    continue

            # Check for numbers
            if char.isdigit():
                number = self.scan_number()
                tokens.append(Token("NUMBER", number))
                continue

            # Check for identifiers or keywords
            if char.isalpha() or char == '_':
                identifier = self.scan_identifier()
                token_type = "KEYWORD" if identifier in self.keywords else "IDENTIFIER"
                tokens.append(Token(token_type, identifier))
                continue

            # Check for symbols
            symbols = ['+', '-', '*', '/', '=', '%', '<', '>', "!", "|", "&", "^", "~"]
            if char in symbols:
                tokens.append(Token("OPERATOR", char))
                self.current_position += 1
                continue

            # Check for special characters
            special_characters = ['(', ')', '{', '}', ';', '#', '\\', '"', "'",'[', ']']
            if char in special_characters:
                tokens.append(Token("SPECIAL CHARACTER", char))
                self.current_position += 1
                continue

            print(f"Error: Unexpected character '{char}'")
            self.current_position += 1

        return tokens

    def scan_number(self):
        start = self.current_position
        while self.current_position < len(self.source_code) and self.source_code[self.current_position].isdigit():
            self.current_position += 1
        return int(self.source_code[start:self.current_position])

    def scan_identifier(self):
        start = self.current_position
        while self.current_position < len(self.source_code) and (self.source_code[self.current_position].isalnum() or self.source_code[self.current_position] == '_'):
            self.current_position += 1
        return self.source_code[start:self.current_position]

    def scan_line_comment(self):
        while self.current_position < len(self.source_code) and self.source_code[self.current_position] != '\n':
            self.current_position += 1

    def scan_block_comment(self):
        self.current_position += 2  # Skip '/*'
        while self.current_position + 1 < len(self.source_code) and self.source_code[self.current_position:self.current_position + 2] != '*/':
            self.current_position += 1
        self.current_position += 2  # Skip '*/'

# Example usage:
source_code = """
int main() {
    // This is a single-line comment
    if (x == 42) {
        /* This is
           a block
           comment */
        for (int i = 0; i < 10; i++) {
            y = y + i;
        }
    } else {
        y = 3; // Another comment
    }
    return 0;
}
"""

scanner = Scanner(source_code)
tokens = scanner.scan_tokens()

for token in tokens:
    print(token)
