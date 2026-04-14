# Demo Translator

This is a simple project that allows translation of a small set of English ↔ Swahili marketplace phrases.

The application exposes a tiny Django app and an API endpoint that translates a handful of common phrases used in marketplaces. Inputs are normalized (trimmed and lowercased) before lookup.

Note: If a phrase is not in the built-in dictionary, the API returns `null` for `translatedText`.

## Supported Phrases

The app supports the following built-in mappings (English → Swahili):

> - "hello how are you" → "hujambo habari yako"
> - "thank you very much" → "asante sana"
> - "how much is this" → "hii ni bei gani"
> - "i want to buy maize" → "nataka kununua mahindi"
> - "where is the market" → "soko liko wapi"
> - "go to the shop" → "nenda dukani"
> - "please help me" → "tafadhali nisaidie"
> - "i need beans" → "nahitaji maharagwe"
> - "weigh the maize" → "pima mahindi"
> - "look for sorghum" → "tafuta mtama"

You can also translate from Swahili → English (the app builds a reverse lookup of the above phrases).

## Dependencies

- Python (recommended 3.10+; project pyproject lists `requires-python = ">=3.14"`, but typical environments with Python 3.10+ should work for Django 6+)
- `Django>=6.0.4`

Installation can be done with `pip` (instructions below). The project also works in a virtual environment.

## Installation (recommended)

1. Create and activate a virtual environment.

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Or (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install "django>=6.0.4"
# or, if you prefer installing the package in editable mode (PEP 517):
pip install -e .
```

If you maintain a `requirements.txt` you can also use `pip install -r requirements.txt`.

## Running the app

There are two common ways to run the development server shown here.

- Using the `uv` helper (if you have it and used it previously):

```powershell
uv run py manage.py runserver 1000
```

- Using plain Python (recommended / works everywhere):

```powershell
python manage.py runserver 1000
```

Open `http://127.0.0.1:1000/` in your browser to access the UI.

## API

Endpoint: `POST /api/v1/translate-text`

Request JSON body:

```json
{ "text": "hello how are you", "targetLanguage": "sw" }
```

- `text`: phrase to translate (string). Input is trimmed and lowercased before lookup.
- `targetLanguage`: either `sw` (English → Swahili) or `en` (Swahili → English). Defaults to `sw`.

Response JSON:

```json
{ "translatedText": "hujambo habari yako" }
```

If a phrase is not found, the API returns:

```json
{ "translatedText": null }
```
