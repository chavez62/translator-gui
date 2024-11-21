# Language Translation Tool

A desktop application built with Python and Tkinter that provides real-time language translation using OpenAI's GPT-3.5 API. The application offers a clean, user-friendly interface for translating text between multiple languages.

![Translation Tool Interface](https://your-screenshot-url.png)

## Features

- Real-time text translation
- Support for multiple languages (Spanish, French, German, Chinese)
- Clean and intuitive user interface
- Secure API key management using environment variables

## Prerequisites

Before running the application, make sure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/translation-tool.git
cd translation-tool
```

2. Install the required packages:
```bash
pip install openai python-dotenv tkinter
```

3. Create a `.env` file in the project root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Configuration

1. Make sure to add `.env` to your `.gitignore` file to keep your API key secure:
```
.env
```

2. You can customize the supported languages by modifying the `values` list in the `target_lang_menu` configuration.

## Usage

1. Run the application:
```bash
python translator.py
```

2. Enter the text you want to translate in the top text box.

3. Select your target language from the dropdown menu.

4. Click the "Translate" button to see the translation in the bottom text box.

## Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and private
- Regularly rotate your API keys as per security best practices

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3.5 API
- Python Tkinter library for the GUI framework
- python-dotenv for environment variable management

## Support

If you encounter any problems or have suggestions, please open an issue in the GitHub repository.
