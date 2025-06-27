from django.shortcuts import render, get_object_or_404, redirect
from .models import ScholarshipProgram, HeroSlider, InfographicStep
from ..news.models import NewsArticle
from .forms import ApplicationForm
from ..stories.models import Testimonial, Story
from django.http import HttpResponse

def home_view(request):
    scholarships = ScholarshipProgram.objects.all()
    sliders = HeroSlider.objects.filter(is_active=True)
    important_testimonials = Testimonial.objects.filter(is_featured=True)
    success_stories = Story.objects.all()
    infographic_steps = InfographicStep.objects.filter(is_active=True)
    news = NewsArticle.objects.order_by('-created_at')[:7]

    context = {
        'scholarships': scholarships,
        'testimonials': important_testimonials,
        'stories': success_stories,
        'news': news,
        'sliders': sliders,
        'infographic_steps': infographic_steps,
    }
    return render(request, 'main/home.html', context)

def scholarship_program_list(request):
    """
    Tüm burs programlarını listeler ve ilgili template'e gönderir.
    """
    scholarships = ScholarshipProgram.objects.all()
    return render(request, 'main/scholarship_program_list.html', {'scholarships': scholarships})

def scholarship_program_detail(request, slug):
    """
    Belirli bir burs programının detay sayfasını gösterir.
    - Program bilgileri
    - Başvuru kriterleri
    - İlgili testimoniallar (etikete göre)
    - SSS (sıkça sorulan sorular)
    """
    scholarship = get_object_or_404(ScholarshipProgram, slug=slug)
    testimonials = Testimonial.objects.filter(tag=scholarship.tag)
    faqs = scholarship.faqs.all()
    return render(request, 'main/scholarship_program_detail.html', {
        'scholarship': scholarship,
        'testimonials': testimonials,
        'faqs': faqs
    })

def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            identity = form.cleaned_data['identity_number']
            email = form.cleaned_data['email']

            already_exists = ApplicationForm.Meta.model.objects.filter(
                identity_number=identity,
                email=email
            ).exists()

            if already_exists:
                form.add_error(None, "Bu bilgilerle daha önce başvuru yapılmış.")
            else:
                form.save()
                return render(request, 'main/application_success.html')

    else:
        form = ApplicationForm()

    return render(request, 'main/application_form.html', {'form': form})

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:/admin/",
        "Sitemap: http://127.0.0.1:8000/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
