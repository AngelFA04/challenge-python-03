import re

def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        pattern = re.compile(r'[a-z]+')
        message = f.read()
        message_decoded = pattern.findall(message)
    m = ''.join(message_decoded)
    print(m)


if __name__ == '__main__':
    run()
