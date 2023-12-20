class Cparser:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.tokens = [self.parse_token(token) for token in file.read().split('\n')]
            print(self.tokens)
        self.current_token = 0

    def parse_token(self, token_str):
        # Assuming token_str is in the format "Token<KEYWORD, int>"
        # print(token_str)
        startInd = 6
        endInd = len(token_str)-1
        token_str = token_str[startInd:endInd:1]
        # print(token_str)
        parts = token_str.split(", ")
        #print(parts)
        # token_type = parts[0]
        # value = parts[1]

        return parts
        # print(token_type)
        # print(value)
        #return Token(token_type, value)

    def parse(self):
        while self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
            if token[0] == 'KEYWORD' and token[1] == 'int':
                self.parse_function_declaration()
            elif token[0] == 'KEYWORD' and token[1] == 'if':
                self.parse_if_statement()
            elif token[0] == 'KEYWORD' and token[1] == 'else':
                self.parse_else_statement()
            elif token[0] == 'KEYWORD' and token[1] == 'for':
                self.parse_for_loop()
            elif token[0] == 'KEYWORD' and token[1] == 'return':
                self.parse_return_statement()
            else:
                self.current_token += 1

    def match(self, expected_type, expected_value=None):
        token = self.tokens[self.current_token]
        if token[0] == expected_type and (expected_value is None or token[1] == expected_value):
            self.current_token += 1
            return True
        return False

    def parse_function_declaration(self):
        if self.match('KEYWORD', 'int') and self.match('KEYWORD', 'main') and self.match('SPECIAL CHARACTER', '(') and self.match('SPECIAL CHARACTER', ')') and self.match('SPECIAL CHARACTER', '{'):
            print("Function declaration: int main()")
            self.current_token -= 1
            self.parse_code_block()

    def parse_if_statement(self):
        if self.match('KEYWORD', 'if') and self.match('SPECIAL CHARACTER', '('):
            print("If statement:")
            #self.parse_expression()
            self.check_operand()
            # self.match('IDENTIFIER')
            self.check_operator()
            # self.match('OPERATOR')
            # self.match('OPERATOR', '=')
            self.check_operand()
            # self.match('IDENTIFIER')
            # self.match('NUMBER')
            self.match('SPECIAL CHARACTER', ')')
            self.parse_code_block()
            print("weselna ???")
            if self.match('KEYWORD', 'else'):
                print("Else statement:")
                self.parse_code_block()

    def check_operand(self):
        return self.match('IDENTIFIER') or self.match('Number')

    def check_operator(self):
        token = self.tokens[self.current_token]
        pre_equal = token[1] == '=' or token[1] == '>' or token[1] == '<' or token[1] == '!' 
        test_not = token[1]
        first_op = self.match('OPERATOR')
        second_op = False
        if pre_equal:
            second_op = self.match('OPERATOR', '=')
        return ((first_op and test_not != '!') or (test_not == '!' and second_op))
    #    >         flag = true      test_not = >       flag1 = true       flag2 = false        
    #   >=  
    #   != 
    #    ==         


    
    def parse_else_statement(self):
        if self.match('KEYWORD', 'else'):
            print("Else statement:")
            self.parse_code_block()

    def parse_for_loop(self):
        print("zoooooom")
        if self.match('KEYWORD', 'for') and self.match('SPECIAL CHARACTER', '('):
            print("For loop:")
            self.parse_expression()
            self.match('SPECIAL CHARACTER', ';')
            self.parse_expression()
            self.match('SPECIAL CHARACTER', ';')
            self.parse_expression()
            self.match('SPECIAL CHARACTER', ')')
            self.parse_code_block()

    def parse_return_statement(self):
        if self.match('KEYWORD', 'return'):
            print("Return statement:")
            self.parse_expression()
            self.match('SPECIAL CHARACTER', ';')

    def parse_expression(self):
        # Simplified expression parsing for demonstration purposes
        while not self.match('SPECIAL CHARACTER', ';'):
            self.current_token += 1

    def parse_code_block(self):
        if self.match('SPECIAL CHARACTER', '{'):
            #print("betege ???")
            while not self.match('SPECIAL CHARACTER', '}'):
                self.parse()
            print("End of code block")


# Example usage:
file_path = "tst.txt"
parser = Cparser(file_path)
parser.parse()
print("Parsing successful!")
