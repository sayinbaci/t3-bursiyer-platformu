from .models import ScholarshipProgram, MenuItem

def scholarship_programs(request):
    return {
        'scholarships': ScholarshipProgram.objects.all()
    }
def dynamic_menu(request):
    return {
        'menu_items': MenuItem.objects.filter(parent__isnull=True).order_by('order')
    }