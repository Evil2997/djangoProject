# views.py
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


@csrf_exempt
def upload_chunk(request):
    if request.method == "POST":
        file = request.FILES['file']
        chunk_index = int(request.POST['chunk_index'])
        upload_id = request.POST['upload_id']

        # Сохраняем часть файла
        chunk_filename = f"{upload_id}_chunk_{chunk_index}"
        file_path = os.path.join('uploaded_chunks/', chunk_filename)
        with default_storage.open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return JsonResponse({'status': 'Chunk uploaded successfully', 'chunk_index': chunk_index})
    return JsonResponse({'error': 'Invalid request'}, status=400)
