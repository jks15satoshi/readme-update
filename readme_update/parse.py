import re
from pathlib import Path

root = Path(__file__).parents[1].resolve()


def parse_readme(readme: Path = root / 'README.md') -> None:
    """
    Parse the README file and update the contents.

    Args:
    - `readme (pathlib.Path)`: Path to the README file.
    """
    regex: re.Pattern = re.compile(
        r'(?P<start><!-- (?P<tag>\w{,20}) (starts|begins) -->)'
        r'(?P<contents>.*?)'
        r'(?P<end><!-- (?P=tag) ends -->)',
        flags=re.IGNORECASE | re.DOTALL)

    with readme.open('r+') as file:
        contents = file.read()
        file.seek(0)
        result = regex.sub(_parse_tag, contents)
        file.write(result)


# TODO: logics of updating contents.
def _parse_tag(match: re.Match) -> str:
    """
    Parse tags from the comment blocks and update contents according to the
    tags.

    Args:
    - `match (re.Match)`: Match object.

    Returns:
    - `str`: Contents to be updated.
    """
    delimiter = '\n' if ((contents := match.group('contents')).startswith('\n')
                         or contents.endswith('\n')) else ''
    result = ''
    return ''.join([
        match.group('start'), delimiter, result, delimiter,
        match.group('end')
    ])
