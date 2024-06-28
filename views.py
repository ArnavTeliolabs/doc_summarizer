# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import os
from .forms import DocumentForm
from .abstractive_summarizer import abstractive_summary
from .pdf_handler import extract_text_from_pdf
from .docx_handler import extract_text_from_docx
from .web_page_handler import extract_text_from_web_page
from .qa_handler import get_closest_answer

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_type = file.name.split('.')[-1].lower()
            if file_type in ['pdf', 'docx']:
                temp_file_path = save_temp_file(file)
                text = extract_text(temp_file_path, file_type)
                os.remove(temp_file_path)
            elif file_type == 'html':
                text = extract_text_from_web_page(file)
            else:
                return render(request, 'upload.html', {'form': form, 'error': 'Unsupported file type'})

            if not text:
                return render(request, 'summary.html', {'summary': 'Text is empty or None'})

            summary = abstractive_summary(text)
            # Render summary.html with summary data
            return render(request, 'summary.html', {'summary': summary, 'file_name': file.name})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def save_temp_file(file):
    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, file.name)
    with open(temp_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return temp_file_path

def extract_text(file_path, file_type):
    if file_type == 'pdf':
        return extract_text_from_pdf(file_path)
    elif file_type == 'docx':
        return extract_text_from_docx(file_path)

def get_answer(request):
    query = request.GET.get('query')
    if query:
        closest_answer = get_closest_answer(query)
        return JsonResponse({'answer': closest_answer})
    return JsonResponse({'error': 'No query provided'}, status=400)
