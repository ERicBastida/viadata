from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView

from django.urls import reverse, reverse_lazy
from django.template.loader import get_template
from django.template import Context
import datetime

from .forms import FilesForm, FilesForm2, FilesForm3
from .models import Files, Files2, Files3
from django.contrib import messages

from django.shortcuts import redirect
import vlc

from django.http import HttpResponse


from .FilesPreviewer import Files_Preview

import sys
#from django.forms import modelformset_factory, formset_factory

#from extra_views import ModelFormSetView

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

"""def upload_and_list_files(request):

    if request.method =="GET":
        files = Files.objects.all()
        return render(request, 'upload_file.html', {
            'files': files
    })
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = FilesForm()
    

    return render(request, 'upload_file.html', {
        'form': form
    })


def files_list(request):
    files = Files.objects.all()
    return render(request, 'files_list.html', {
        'files': files
    })"""


class PreviewFiles(CreateView):
    "Clase encargada de mostrar la vista previsualizadora de contenido."

    template_name = 'preview.html'
    print("------------------akljsdfljasdlfjasjdlfkjasdfkja--------------")
    def get_context_data(self, **kwargs):
        context = super(PreviewFiles, self).get_context_data(**kwargs)
        context['file_to_preview'] = True

        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class UploadFileView(CreateView):
    model = Files
    form_class = FilesForm
    success_url = reverse_lazy('files_list')
    template_name = 'upload_file.html'
    
    def get_context_data(self, **kwargs):
        context = super(UploadFileView, self).get_context_data(**kwargs)
        context['Files'] = Files.objects.all()
        return context

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))

class UploadFileView2(CreateView):
    model = Files2
    form_class = FilesForm2
    success_url = reverse_lazy('files_list2')
    template_name = 'upload_file2.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(UploadFileView2, self).get_context_data(**kwargs)
        context['Files2'] = Files2.objects.all()
        return context
    

    def form_invalid(self, form):
        
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class UploadFileView3(CreateView):
    model = Files3
    form_class = FilesForm3
    success_url = reverse_lazy('files_list3')
    template_name = 'upload_file3.html'
    
    def get_context_data(self, **kwargs):
        
        context = super(UploadFileView3, self).get_context_data(**kwargs)
        context['Files3'] = Files3.objects.all()
        return context
    

    def form_invalid(self, form):
        
        messages.add_message(
            self.request, messages.ERROR, 'the image was not uploaded. Introduce a valid format .png , .tiff or .bmp'
        )
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


# def detail_file(request, pk):
#
#     pass
    # file_to_view = Files_Preview()
    # html_file = file_to_view.view_web_file(pk)
    #
    # response = HttpResponse(html_file, content_type='text/html')
    #
    # return response
#     return redirect('class_preview_files')


# def detail_file(request, pk):
    # now = "13:55"
    # t = get_template('preview.html')
    # html = t.render(Context({'file_to_view': True}))
    # return HttpResponse("AAAAAAAAALOOOOOJAAAAAAAA")
    # return HttpResponse(html)
    # return render(request,'preview.html',{'file_to_view': "yes"})




def delete_file(request, pk):
    if request.method == 'POST':
        file = Files.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file')

def delete_file2(request, pk):
    if request.method == 'POST':
        file = Files2.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file2')

def delete_file3(request, pk):
    if request.method == 'POST':
        file = Files3.objects.get(pk=pk)
        file.delete()
    return redirect('class_upload_file3')


