from django.db import models
from cms.models import CMSPlugin

from pygments.lexers import get_all_lexers

from pygments import highlight
from pygments.formatters import HtmlFormatter

from pygments.lexers import get_lexer_by_name

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Snippet(CMSPlugin):
    title = models.CharField(max_length=255)
    code = models.TextField()
    formatted_code = models.TextField()
    lexer = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    lines = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        lex = get_lexer_by_name(self.lexer, stripall=True)
        #formatter = HtmlFormatter(linenos=self.lines, cssclass="source")
        self.formatted_code = highlight(self.code, lex, HtmlFormatter())


        super(Snippet, self).save(*args, **kwargs)
