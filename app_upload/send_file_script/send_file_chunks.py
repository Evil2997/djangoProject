import os
import requests


def send_file_in_chunks(file_path, chunk_size=50 * 1024 * 1024, upload_id="some_unique_id"):
    """Разделяем файл на части и отправляем через POST запросы"""
    total_size = os.path.getsize(file_path)
    num_chunks = total_size // chunk_size + (1 if total_size % chunk_size != 0 else 0)

    with open(file_path, 'rb') as file:
        for chunk_index in range(num_chunks):
            chunk_data = file.read(chunk_size)
            files = {'file': chunk_data}
            data = {
                'chunk_index': chunk_index,
                'upload_id': upload_id
            }
            response = requests.post('https://second-server.com/upload_chunk/', files=files, data=data)
            if response.status_code == 200:
                print(f"Часть {chunk_index} успешно отправлена.")
            else:
                print(f"Ошибка отправки части {chunk_index}: {response.text}")
