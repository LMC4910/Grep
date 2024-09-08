import sys

# import pyparsing
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    # Handle simple character class patterns
    if pattern == "\\d":
        return any(c.isdigit() for c in input_line)
    elif pattern == "\\w":
        return any(c.isalnum() for c in input_line)
    
    elif '[' in pattern and ']' in pattern:
        if pattern.startswith('[^'):
            start = 2
        else:
            start = 1
        
        end = pattern.index(']')
        value_inside_brackets = pattern[start:end]
        
        if pattern.startswith('[^'):
            return any(char not in value_inside_brackets for char in input_line)
        else:
            return any(char in value_inside_brackets for char in input_line)
    elif '\\' in pattern :
        print(pattern)
        return 0
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")




def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)
    
    print("Logs from your program will appear here!")    
    
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
