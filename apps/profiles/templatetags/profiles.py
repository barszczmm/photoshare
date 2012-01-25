from django import template
register = template.Library()


@register.assignment_tag()
def is_profile_fan_of_profile(profile_from, profile_to):
    try:
        if profile_from.fan_of.filter(pk=profile_to.id).count():
            return True
        else:
            return False
    except:
        return False

