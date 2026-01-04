import os
import img2pdf
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Пожалуйста, пришлите фото для конвертации в PDF")


@router.message(F.photo)
async def photo_to_pdf(message: types.Message):
    try:
        await message.answer("⏳Ожидайте...")
        photo = message.photo[-1]
        file_info = await message.bot.get_file(photo.file_id)
        temp_image_path = f"temp_{message.from_user.id}.jpg"
        pdf_path = f"result_{message.from_user.id}.pdf"
        await message.bot.download_file(file_info.file_path, temp_image_path)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(temp_image_path))
        await message.answer_document(FSInputFile(pdf_path))
        if os.path.exists(temp_image_path): os.remove(temp_image_path)
        if os.path.exists(pdf_path): os.remove(pdf_path)
        await message.answer("Готово! Если нужно ещё — присылайте фото.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
