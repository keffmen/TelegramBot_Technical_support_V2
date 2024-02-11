import logging
import os

from aiogram import Router
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import json_response
from aiogram.types import Message
from aiogram import Bot

router = Router()


async def upload(request: Request):
    data = await request.post()

    # Извлечение отдельных полей формы
    chat_id = data.get('Chat_id')
    id_value = data.get('id')
    name_value = data.get('name')
    org_value = data.get('org')
    phone_value = data.get('phone')
    problem_value = data.get('problem')

    # Process the files (if needed)
    uploaded_files_info = []
    if 'image' in data:
        for file_field in data.getall('image'):
            # Save the uploaded file to a folder (replace 'upload_folder' with your desired folder)
            upload_folder = f'database/{id_value}'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            file_path = os.path.join(upload_folder, file_field.filename)
            with open(file_path, 'wb') as f:
                while True:
                    chunk = file_field.file.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)
            # Store information about the uploaded photo
            uploaded_files_info.append({'filename': file_field.filename, 'path': file_path})

    # Отправка уведомления
    print(f'Получил заявку №{id_value}\n'
          f'Имя: {name_value}\n'
          f'Организация: {org_value}\n'
          f'Номер телефона: {phone_value}\n'
          f'Проблема: {problem_value}\n'
          f'id в TELEGRAM: {chat_id}')
    bot: Bot = request.app['bot']
    await bot.send_message(chat_id=chat_id, text='Мы получили вашу заявку! Вы получите ответ в ближайшее время!')

    # Получите заголовок «Origin» из запроса.
    origin = request.headers.get('Origin', '*')

    # Установить заголовки CORS
    response_data = {'message': f'Upload successful. Request came from origin: {origin}'}
    response = web.json_response(response_data, status=200)
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    return response
