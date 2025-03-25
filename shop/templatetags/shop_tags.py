from django import template

register = template.Library()


@register.filter
def chunker(seq, size):
    """
    Splits the list `seq` into chunks of length `size`.
    """
    try:
        size = int(size)
    except ValueError:
        return seq
    return [seq[i:i + size] for i in range(0, len(seq), size)]
