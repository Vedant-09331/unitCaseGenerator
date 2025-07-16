import os
import google.generativeai as genai
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

# Configure Gemini API
GEMINI_API_KEY = getattr(settings, 'GEMINI_API_KEY', 'AIzaSyDGQltxOD_mGJj2fTwzxrzXnZnVw7AiwLo')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_unit_test_code(prompt):
    """Generate Python unit test code using Gemini AI."""
    try:
        response = model.generate_content(
            f"Generate a Python unit test code snippet for: {prompt}. "
            "Provide only the code (no explanations). Use proper Python syntax and unittest framework."
        )
        time.sleep(1)  # Rate limiting
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def home(request):
    """Render the home page with the test generator interface."""
    return render(request, 'test_generator/home.html')

@csrf_exempt
def generate_test(request):
    """Handle AJAX requests to generate test code."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_prompt = data.get('prompt', '').strip()
            
            if not user_prompt:
                return JsonResponse({
                    'success': False,
                    'error': 'Please enter a valid prompt.'
                })
            
            # Generate the test code
            generated_code = generate_unit_test_code(user_prompt)
            
            return JsonResponse({
                'success': True,
                'code': generated_code,
                'prompt': user_prompt
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Server error: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST requests are allowed.'
    }) 