import time

def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    num_chars = sum(len(word) for word in words)
    wpm = (num_words / time_taken) * 60
    cpm = (num_chars / time_taken) * 60
    return wpm, cpm

def find_errors(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    errors = []
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] != typed_words[i]:
            errors.append(i)
    return errors

if __name__ == "__main__":
    print("Welcome to the Typing Speed Calculator and Error Finder App!")
    print("Please type the following text:")
    original_text = "The quick brown fox jumps over the lazy dog."
    print(original_text)
    input("Press Enter when you're ready to start typing.")
    
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm, cpm = calculate_typing_speed(typed_text, time_taken)
    print(f"Your typing speed is: {wpm} words per minute (WPM) and {cpm} characters per minute (CPM).")

    errors = find_errors(original_text, typed_text)
    if errors:
        print("Errors found at the following positions:")
        for error in errors:
            print(f"Position {error + 1}: Expected '{original_text.split()[error]}', Found '{typed_text.split()[error]}'")
    else:
        print("No errors found. Great job!")
