from django.shortcuts import render, redirect, get_object_or_404
from .models import Interview, Story, Testimonial
from .forms import TestimonialForm
from django.contrib import messages


def testimonial_view(request):
    testimonials = Testimonial.objects.filter(is_featured=True)
    stories = Story.objects.all()
    interviews = Interview.objects.all()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.is_featured = False
            testimonial.save()
            messages.success(request, "Yorumunuz başarıyla gönderildi, onay sonrası yayınlanacaktır.")
            return redirect('testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'stories/testimonials.html', {
        'testimonials': testimonials,
        'stories': stories,
        'interviews': interviews,
        'form': form
    })

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    return render(request, 'stories/story_detail.html', {'story': story})

