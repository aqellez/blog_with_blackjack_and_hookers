from django import template
import re
from pygments import lexers, formatters, highlight

register = template.Library()
regex = re.compile(r'<pre(.*?)>(.*?)</pre>', re.DOTALL)


@register.filter(is_safe=True)
def highlighter(value):
    last_end = 0
    to_return = ''
    # found = 0
    for match_obj in regex.finditer(value):
        code_class = match_obj.group(1)
        code_string = match_obj.group(2)
        if code_class.find('class'):
            language = re.split(r'"|\'', code_class)[1]
            lexer = lexers.get_lexer_by_name(language)
        else:
            try:
                lexer = lexers.guess_lexer(str(code_string))
            except ValueError:
                lexer = lexers.PythonLexer()
        pygmented_string = highlight(
            code_string, lexer, formatters.HtmlFormatter())
        to_return = to_return + \
            value[last_end:match_obj.start(0)] + pygmented_string
        last_end = match_obj.end(2)
        # found = found + 1
    to_return = to_return + value[last_end:]
    return to_return
