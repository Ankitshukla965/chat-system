from app.schemas.error import APIError
def api_error(error_code: str, message: str, details: None):
    return APIError(
    error_code=error_code,
    message=message,
    details=details
    ).model_dump()
    