from django import template
from blog.models import Post
from home.models import LuxuryPackages


register = template.Library()

@register.simple_tag(name='Last_six_posts')
def Last_six_posts(number:int):
    Last_six_posts = Post.objects.filter(status=True)[:number]
    return Last_six_posts



@register.filter(name='upper')
def Upper(text:str):
    return text.upper()



@register.filter(name='truncates')
def Truncates(text:str,number:int):
    return ' '.join(text.split()[:number])



@register.inclusion_tag('issue.html')
def Issue ():
    pass



@register.inclusion_tag('lux.html')
def lux():
    luxury = LuxuryPackages.objects.all()
    return {'luxury':luxury}
    