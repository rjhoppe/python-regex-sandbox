import re

def extract_full_names(text):
    # Define a regular expression pattern for full names
    name_pattern = re.compile(r'\b[A-Z][a-zA-Z\'\- ]+\b')

    # Use findall to extract all matches
    full_names = name_pattern.findall(text)

    return full_names

# Example usage:
text = "John Doe, Mary Jane-Smith, and Alex O'Connor went to the event."
full_names = extract_full_names(text)
print(full_names)