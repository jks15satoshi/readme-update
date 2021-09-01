import re
from pathlib import Path


def parse_readme() -> None:
    """
    Parse the README file and update the contents.
    """
    regex: re.Pattern = re.compile(
        r'(?P<start><!-- (?P<tag>\w*) (starts|begins) -->).*?'
        r'(?P<end><!-- (?P=tag) ends -->)',
        flags=re.IGNORECASE | re.DOTALL)

    with (Path(__file__).parents[1] / 'README.md').open('r+') as file:
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
    result = ''
    return ''.join([match.group('start'), f'\n{result}\n', match.group('end')])
