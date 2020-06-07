"""Just project. For more information look README.md"""


def utf_len(text: bytes) -> int:
    """Function"""

    answer = len(text.decode('utf-8'))
    return answer


if __name__ == '__main__':
    print(utf_len(input().encode('utf-8')))
