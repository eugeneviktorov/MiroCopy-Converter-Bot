from bot.utils.enums import FileDocumentsExtensions


def build_pdf_name(user_id: int, operation_id: str) -> str:
    return f"result_{user_id}_{operation_id}.{FileDocumentsExtensions.PDF}"
