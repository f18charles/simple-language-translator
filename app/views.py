from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST

dictionary = {
    "hello how are you": "hujambo habari yako",
    "thank you very much": "asante sana",
    "how much is this": "hii ni bei gani",
    "i want to buy maize": "nataka kununua mahindi",
    "where is the market": "soko liko wapi",
    "go to the shop": "nenda dukani",
    "please help me": "tafadhali nisaidie",
    "i need beans": "nahitaji maharagwe",
    "weigh the maize": "pima mahindi",
    "look for sorghum": "tafuta mtama",
}

def HomeView(request):
    return render(request, "index.html")

@require_POST
def TranslatorView(request):
    # get the payload from template
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error":"Invalid JSON"}, status=400)
    
    # extract text and language 
    text = data.get("text", "").strip().lower()
    target_language = data.get("targetLanguage", "sw")
    
    # Translate
    if target_language == "sw":
        translated_text = dictionary.get(text, None)
    elif target_language == "en":
        reverse_dictionary = {v: k for k, v in dictionary.items()}
        translated_text = reverse_dictionary.get(text, None)
    else:
        translated_text = None
        
    return JsonResponse({"translatedText": translated_text})