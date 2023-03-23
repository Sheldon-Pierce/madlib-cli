import re

print(
    """
    Hello, Welcome to Madlib. You will be prompted to enter different words,
    after that you will receive a story based on the inputted words!
    """
)


def read_template(file):
    with open(file) as file:
        global context
        context = file.read()
        return context


def parse_template(context):
    pattern = r'\{.*?\}'
    template = re.sub(pattern, '{}', context)
    parts = re.findall(pattern, context)
    stripped_parts = list()
    for part in parts:
        stripped_parts.append(part.strip('{}'))

    stripped_parts = tuple(stripped_parts)
    global answers
    answers = template, stripped_parts
    return answers


def inputs():
    global user_words
    user_words = []
    for thing in answers[1]:
        user_words.append(input(f'Please enter a {thing} '))


def merge(user_string, user_choices):
    final_string = user_string.format(*user_choices)
    with open('assets/video_game.copy.txt', 'w') as copied_file:
        copied_file.write(final_string)
    return final_string


if __name__ == '__main__':
    read_template('assets/video_game.txt')
    parse_template(context)
    inputs()
    print(merge(answers[0], user_words))

