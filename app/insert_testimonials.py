from app.models import Testimonial
from app.testimonials import testimonials

def insertTestimonials():
    for testimonial in testimonials:
        t = Testimonial(
            author_name=testimonial['author_name'],
            author_position=testimonial['author_position'],
            author_company=testimonial['author_company'],
            content=testimonial['content'],
            image=testimonial['image'],
        )
        t.save()