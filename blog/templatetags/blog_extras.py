from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from blog.models import Post

register = template.Library()
User = get_user_model()

@register.filter
def author_details(author, user = None):
  if author == user:
    return format_html("<strong>me</strong>")
  if isinstance(author, User):
    if author.first_name and author.last_name:
      name = escape(f"{author.first_name} {author.last_name}")
    else:
      name = escape(f"{author.username}")

    if author.email:
      email = escape(author.email)
      #prefix = f'<a href="mailto:{email}">'
      prefix = format_html('<a href="mailto:{}">', author.email)
      suffix = "</a>"
    else:
      prefix = ""
      suffix = ""
    

    return mark_safe(f"{prefix}{name}{suffix}")

@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html("</div>")

@register.simple_tag
def col():
  return format_html('<div class="col">')

@register.simple_tag
def endcol():
  return format_html('</div>')

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  postObj = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": postObj}