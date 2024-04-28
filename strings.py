import secrets
import string

def generate_random_string(length=30):
    alphabet = string.ascii_letters + string.digits + string.punctuation.replace('.', '') # Punkt ausgenommen
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_random_string_with_sections(num_sections=3, min_length=10, max_length=20):
    sections = []
    for _ in range(num_sections):
        section_length = secrets.randbelow(max_length - min_length) + min_length
        sections.append(generate_random_string(section_length))
    return '.'.join(sections)

num_strings = 100000

with open("token.txt", "w") as file:
    for _ in range(num_strings):
        file.write(generate_random_string_with_sections() + "\n")
