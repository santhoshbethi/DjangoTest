import os
import fitz  # PyMuPDF
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
import json
from django.shortcuts import render
client = OpenAI(api_key=settings.OPENAI_API_KEY)


@require_GET
def list_pdfs(request):
    '''List all PDF files in the assets directory. '''
    files = [f for f in os.listdir(settings.ASSETS_DIR) if f.endswith('.pdf')]
    return JsonResponse({'files': files})


@csrf_exempt
@require_POST
def summarize_pdf(request):
    '''Summarize a PDF file using OpenAI API. '''
    data = json.loads(request.body)
    filename = data.get('filename')

    if not filename:
        return JsonResponse({'error': 'Filename is required'}, status=400)

    file_path = os.path.join(settings.ASSETS_DIR, filename)

    if not os.path.exists(file_path):
        return JsonResponse({'error': 'File not found'}, status=404)

    # Extract text
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()


    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes PDF documents."},
                {"role": "user", "content": f"Summarize this:\n{text[:4000]}"}  # Limit to 4K tokens
            ],
            max_tokens=500
        )
        summary = response.choices[0].message.content
        return JsonResponse({'summary': summary})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




def index(request):
    return render(request, 'index.html')
