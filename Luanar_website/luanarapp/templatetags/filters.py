# filters.py

from django import template
from django.utils.html import mark_safe
import re

register = template.Library()

@register.filter
def highlight_search(text, query):
    # Use regular expression to find and replace the searched word with the highlighted version
    highlighted_text = re.sub(
        re.escape(query),
        lambda match: f'<span class="highlight">{match.group()}</span>',
        text,
        flags=re.IGNORECASE  # Ignore case for case-insensitive search
    )
    return mark_safe(highlighted_text)
