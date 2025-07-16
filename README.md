# Gemini AI Python Unit Test Generator

A beautiful Django web application that generates Python unit tests using Google's Gemini AI. This project provides a modern, user-friendly interface for creating unit tests based on natural language descriptions.

## Features

- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- 🤖 **AI-Powered**: Uses Google's Gemini AI to generate high-quality unit tests
- 📝 **Easy to Use**: Simple text input with example prompts
- 📋 **Copy to Clipboard**: One-click code copying functionality
- 📱 **Mobile Responsive**: Works perfectly on all device sizes
- ⚡ **Real-time Generation**: Fast, asynchronous test generation

## Screenshots

The application features a clean, modern interface with:
- Gradient background and card-based layout
- Interactive form with placeholder text
- Loading animations during generation
- Syntax-highlighted code output
- Example prompts for quick testing

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project files**

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Gemini API key:**
   
   Create a `.env` file in the project root and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   
   You can get a free API key from: https://ai.google.dev/

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Enter a description** of what you want to test in the text area
2. **Click "Generate Unit Test"** or press Enter
3. **Wait for the AI** to generate your test code
4. **Copy the generated code** using the copy button
5. **Use the example prompts** for quick testing

### Example Prompts

- "a function that calculates the factorial of a number"
- "a class that validates email addresses"
- "a function that finds the maximum value in a list"
- "a class that represents a bank account with deposit and withdraw methods"

## Project Structure

```
gemini_test_generator/
├── gemini_test_generator/     # Django project settings
│   ├── __init__.py
│   ├── settings.py           # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── test_generator/          # Django app
│   ├── __init__.py
│   ├── apps.py             # App configuration
│   ├── views.py            # View logic and Gemini AI integration
│   └── urls.py             # App URL routing
├── templates/              # HTML templates
│   └── test_generator/
│       └── home.html       # Main application interface
├── static/                 # Static files
│   └── css/
│       └── style.css       # Additional CSS styles
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Django Settings

The main configuration is in `gemini_test_generator/settings.py`:
- Debug mode is enabled for development
- Static files are configured
- Database uses SQLite (can be changed for production)

## API Integration

The application uses the `google-generativeai` library to interact with Gemini AI:

```python
import google.generativeai as genai

# Configure the API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content
response = model.generate_content(prompt)
```

## Customization

### Styling

The main styling is in the `home.html` template. You can customize:
- Colors and gradients
- Fonts and typography
- Layout and spacing
- Animations and transitions

### AI Model

You can change the Gemini model in `test_generator/views.py`:
- `gemini-1.5-flash` (fast, good for simple tasks)
- `gemini-1.5-pro` (more capable, slower)

### Prompt Engineering

Modify the prompt in the `generate_unit_test_code` function to get different types of test outputs.

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your Gemini API key is valid and has sufficient quota
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port with `python manage.py runserver 8001`

### Error Messages

- "Please enter a valid prompt": The input field is empty
- "Network error": Check your internet connection
- "Server error": Check the Django logs for details

## Development

### Adding Features

1. **New Models**: Create Django models in `test_generator/models.py`
2. **New Views**: Add views in `test_generator/views.py`
3. **New Templates**: Create HTML files in `templates/test_generator/`
4. **New URLs**: Update `test_generator/urls.py`

### Testing

Run Django tests:
```bash
python manage.py test
```

### Deployment

For production deployment:
1. Set `DEBUG = False` in settings
2. Use a production database (PostgreSQL, MySQL)
3. Configure static file serving
4. Set up environment variables securely
5. Use HTTPS

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the project repository.

---

**Happy Testing! 🧪✨** 