import markdown
import pathlib
from pygments.formatters import HtmlFormatter

"""
This class will take in Markdown and correctly render it into HTML.
Output generated can be then piped into Jinja2 style syntax with the following line:

{{ GeneratedOutput|safe }}

Please refer to this Stackoverflow post for more details:

https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2

Written by Jared Dyreson CSUF 2021
"""

class MarkdownIngestor():
    def __init__(self, path: pathlib.Path):
        if(not isinstance(path, pathlib.Path)):
            raise ValueError
        self.path = path
        self.read_contents()
        self.format_contents()

    def read_contents(self):
        with open(self.path, "r") as f:
            self.markdown_contents = f.read()
            
    def format_contents(self):
        markdown_extensions = [
            'markdown.extensions.attr_list',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'codehilite'
        ]

        self.formatted_contents = markdown.markdown(
            self.markdown_contents, 
            output_format = 'html5',
            tab_length = 4,
            extensions = markdown_extensions
        )

    def write_formatted_contents(self):
        with open(f'{self.path.stem}.html', "w") as f:
            f.write(self.formatted_contents)
