from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(cost, participants):
    """Subtotal calculation
    Args:
        cost: cost of a tour
        participants: number of participants
    Returns:
        subtotal
    """
    return cost * participants