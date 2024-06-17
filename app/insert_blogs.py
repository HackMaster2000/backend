from app.models import BlogPost
from app.blogs import blogs

def insertBlogs():
    for blog in blogs:
        b = BlogPost(
            title=blog['title'],
            author=blog['author'],
            content=blog['content'],
            publish_date=blog['publish_date'],
            image=blog['image'],
        )
        b.save()