NAMES_FILENAME = "Input/Names/invited_names.txt"
TEMPLATE_FILENAME = "Input/Letters/starting_letter.txt"
OUTPUT_PREFIX = "Output/ReadyToSend/letter_for_"

with open(TEMPLATE_FILENAME) as template_file:
    template = template_file.read()
    with open(NAMES_FILENAME) as names_file:
        names = names_file.readlines()
        for name in names:
            n = name.strip()
            output = template.replace("[name]", n)
            print(output)
            with open(OUTPUT_PREFIX + n + ".txt", "w") as file:
                file.write(output)
