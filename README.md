# Demo Translator

This is a simple project that allows translation of a small set of English ↔ Swahili marketplace phrases.

The application exposes a tiny Django app and an API endpoint that translates a handful of common phrases used in marketplaces. Inputs are normalized (white spaces are trimmed and text is lowercased) before lookup.

Note: If a phrase is not in the built-in dictionary, the API returns `null` for `translatedText`. The template returns the original text.

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

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

### With uv (recommended)

uv manages your virtual environment and dependencies in one step.

1. Install uv if you don't have it:

```powershell
pip install uv
```

2. Install dependencies:

```powershell
uv sync
```

That's it. uv creates the virtual environment and installs everything from `pyproject.toml` automatically.

### With pip

Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Mac/Linux
source .venv/bin/activate
```

## Running the app

```bash
# With uv
uv run python manage.py runserver 1000

# With pip (virtual environment must be active)
python manage.py runserver 1000
```

Open http://127.0.0.1:1000/ in your browser.

## API

Endpoint: `POST /api/v1/translate-text`

Request JSON body:

```json
{ "text": "hello how are you", "targetLanguage": "sw" }
```

- `text`: phrase to translate (string).
- `targetLanguage`: either `sw` (English → Swahili) or `en` (Swahili → English).

Response JSON:

```json
{ "translatedText": "hujambo habari yako" }
```

If a phrase is not found, the API returns:

```json
{ "translatedText": null }
```
