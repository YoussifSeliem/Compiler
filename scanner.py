import sys

class Token:
    # The structure of the token
    def __init__(self, token_type, value, row, column):
        self.type = token_type
        self.value = value
        self.row = row
        self.column = column

    # The format of printing tokens
    def __str__(self):
        return f'Token<{self.type}, {self.value}, {self.row}, {self.column}>'

class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.current_position = 0
        self.row = 1
        self.column = 1

        # Define keywords
        self.keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'char', 'double', 'main', 'return']

    def scan_tokens(self):
        tokens = []

        while self.current_position < len(self.source_code):
            #print(self.row)
            char = self.source_code[self.current_position]
            #print(self.current_position)
            if self.current_position < len(self.source_code) and self.source_code[self.current_position] == '\n':
                #print("test")
                #print(self.row)
                self.row += 1
                self.column = 1
                self.current_position += 1
                continue
            
            # Ignore whitespace
            if char.isspace():
                self.column += 1
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
            if char.isdigit() or (char == '.' and self.current_position + 1 < len(self.source_code) and self.source_code[self.current_position + 1].isdigit()):
                number = self.scan_number()
                tokens.append(Token("NUMBER", number, self.row, self.column))
                continue

            # Check for identifiers or keywords
            if char.isalpha() or char == '_':
                identifier = self.scan_identifier()
                token_type = "KEYWORD" if identifier in self.keywords else "IDENTIFIER"
                tokens.append(Token(token_type, identifier, self.row, self.column))
                continue

            # Check for operators
            symbols = ['+', '-', '*', '/', '=', '%', '<', '>', "!", "|", "&"]
            if char in symbols:
                tokens.append(Token("OPERATOR", char, self.row, self.column))
                self.column += 1
                self.current_position += 1
                continue

            # Check for special characters
            special_characters = ['(', ')', '{', '}', ';', '"', "'",'[', ']']
            if char in special_characters:
                tokens.append(Token("SPECIAL CHARACTER", char, self.row, self.column))
                self.column += 1
                self.current_position += 1
                continue

            print(f"Error: Unexpected character '{char}'")
            #sys.exit()

            self.column += 1
            self.current_position += 1

        return tokens

    # make sure that the number contains only numbers
    def scan_number(self):
        start = self.current_position
        is_float = False

        while self.current_position < len(self.source_code) and (self.source_code[self.current_position].isdigit() or (self.source_code[self.current_position] == '.' and not is_float)):
            if self.source_code[self.current_position] == '.':
                is_float = True
            self.column += 1
            self.current_position += 1

        if is_float:    
            return float(self.source_code[start:self.current_position])
        else:
            return int(self.source_code[start:self.current_position])


    # make sure that the identifier contains letters, numbers or _ 
    def scan_identifier(self):
        start = self.current_position
        while self.current_position < len(self.source_code) and (self.source_code[self.current_position].isalnum() or self.source_code[self.current_position] == '_'):
            self.column += 1
            self.current_position += 1
        return self.source_code[start:self.current_position]

    def scan_line_comment(self):
        while self.current_position < len(self.source_code) and self.source_code[self.current_position] != '\n':
            self.column = 0
            self.current_position += 1
        self.row +=1
        self.current_position += 1

    def scan_block_comment(self):
        self.current_position += 2  # Skip '/*'
        while self.current_position + 1 < len(self.source_code) and self.source_code[self.current_position:self.current_position + 2] != '*/':
            self.column += 1
            self.current_position += 1
            if self.current_position < len(self.source_code) and self.source_code[self.current_position] == '\n':
                # print("test")
                # print(self.row)
                self.row += 1
                self.column = 1
                continue
        self.column += 2
        self.current_position += 2  # Skip '*/'

def read_source_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_tokens_to_file(tokens, output_file):
    try:
        with open(output_file, 'w') as file:
            for token in tokens:
                file.write(str(token) + '\n')
    except Exception as e:
        print(f"Error writing to the output file: {e}")



if len(sys.argv) != 3:
    print("Usage: python scanner.py input_file.c output_file.txt")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

source_code = read_source_code(input_file)
scanner = Scanner(source_code)
tokens = scanner.scan_tokens()
write_tokens_to_file(tokens, output_file)