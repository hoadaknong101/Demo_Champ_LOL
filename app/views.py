from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Cosplay, SkinGeneral, General, AbilityGeneral, IntroduceGeneral
from django.template import loader
from .form import CosplayForm


def HomeView(request):
    return render(request, "home.html")


def get_General(request):
    list_general = General.objects.all()
    template = loader.get_template('general.html')
    context = {
        'list_general': list_general,
    }
    return HttpResponse(template.render(context, request))


def get_General_With_Name(request, general_name):
    gen = General.objects.all().filter(name=general_name)
    print(gen[0].introducegeneral.role)
    template = loader.get_template('viewgeneral.html')
    context = {
        'name': gen[0].name,
        'image': gen[0].introducegeneral.image,
        'role': gen[0].introducegeneral.role,
        'level': gen[0].introducegeneral.level,
        'diffculty': gen[0].introducegeneral.diffculty,
        'introduction': gen[0].introducegeneral.introduction,
        'video_intro_id': gen[0].introducegeneral.video_intro_id,
        # ability general
        'name_passive': gen[0].abilitygeneral.name_passive,
        'content_passvie': gen[0].abilitygeneral.content_passive,
        'image_passive': gen[0].abilitygeneral.image_passive,

        'name_q': gen[0].abilitygeneral.name_q,
        'content_q': gen[0].abilitygeneral.content_q,
        'image_q': gen[0].abilitygeneral.image_q,

        'name_w': gen[0].abilitygeneral.name_w,
        'content_w': gen[0].abilitygeneral.content_w,
        'image_w': gen[0].abilitygeneral.image_w,

        'name_e': gen[0].abilitygeneral.name_e,
        'content_e': gen[0].abilitygeneral.content_e,
        'image_e': gen[0].abilitygeneral.image_e,

        'name_r': gen[0].abilitygeneral.name_r,
        'content_r': gen[0].abilitygeneral.content_r,
        'image_r': gen[0].abilitygeneral.image_r,

        'video_ability': gen[0].abilitygeneral.video_ability,
        # skin general

        'name_1': gen[0].skingeneral.name_1,
        'image_1': gen[0].skingeneral.image_1,

        'name_2': gen[0].skingeneral.name_2,
        'image_2': gen[0].skingeneral.image_2,

        'name_3': gen[0].skingeneral.name_3,
        'image_3': gen[0].skingeneral.image_3,

        'name_4': gen[0].skingeneral.name_4,
        'image_4': gen[0].skingeneral.image_4,

        'name_5': gen[0].skingeneral.name_5,
        'image_5': gen[0].skingeneral.image_5,
    }
    return HttpResponse(template.render(context, request))


def get_Cosplay(request):
    list_cosplay = Cosplay.objects.all()
    template = loader.get_template('cosplay.html')
    context = {
        'list_cosplay': list_cosplay
    }
    return HttpResponse(template.render(context, request))


def post_Cosplay(request):
    if request.method == 'POST':
        form = CosplayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cosplay/')
    else:
        form = CosplayForm()
    return HttpResponse(loader.get_template('upload.html').render({'form': form}, request))
