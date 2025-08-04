# AI-shell CLI - AI-Powered Interactive Shell

🧠 **AI-shell CLI** is an interactive command-line shell that accepts natural language input and suggests equivalent shell commands using an LLM. It behaves like a real terminal but with AI-powered command generation.

## Features

- 🤖 **AI-powered**: Uses Google Gemini API for intelligent command generation
- 🛡️ **Safety first**: Built-in safety checker to detect potentially dangerous commands
- 📝 **Command logging**: All interactions are logged to `~/.ai_shell_history.log`
- 🎨 **Rich UI**: Beautiful terminal interface with colors and formatting
- 🔍 **Interactive**: Real-time command generation and execution
- 📖 **Help system**: Built-in help and history commands
- 🎮 **Demo mode**: Try without API key using predefined commands

## Installation

### From PyPI (Recommended)

```bash
pip install ai-shell-cli
```

### Quick Start

After installation, you can start the shell with:

```bash
# Main interactive shell (requires API key)
ai-shell-cli

# Demo mode (no API key required)
ai-shell-demo
```

## Usage

### Starting the Shell

```bash
ai-shell-cli
```

You'll see a prompt like:
```
AI-shell> 
```

### Natural Language Queries

Type natural language descriptions of what you want to do:

```bash
AI-shell> find all PDF files larger than 10MB
💡 Suggested: find . -name "*.pdf" -size +10M
Run this command? [y/N]: y
📤 Executing...
✅ Command executed successfully!

📄 Output:
./documents/report.pdf
./downloads/manual.pdf
```

### Special Commands

- `:quit` or `:exit` - Exit the shell
- `:help` - Show help information
- `:history` - Show recent command history
- `:clear` - Clear the screen

### Example Interactions

```bash
AI-shell> delete all .zip files in Downloads
💡 Suggested: rm ~/Downloads/*.zip
Run this command? [y/N]: n
❌ Cancelled

AI-shell> list all python files modified in the last 24 hours
💡 Suggested: find . -name "*.py" -mtime -1
Run this command? [y/N]: y
📤 Executing...
✅ Command executed successfully!

📄 Output:
./main.py
./utils/llm.py
./test_basic.py
```

## API Configuration

### Setting up Google Gemini API

1. **Get an API key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Set the environment variable**:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
3. **Or create a `.env` file**:
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

### Demo Mode (No API Required)

If you don't have an API key, you can try the demo mode:

```bash
ai-shell-demo
```

Demo mode includes predefined commands like:
- "find all pdf files"
- "list all python files"
- "show disk usage"
- "check memory usage"
- "go to downloads folder"

## Project Structure

```
ai-shell-cli/
├── ai_shell/        # Main package
│   ├── main.py      # Interactive shell loop
│   ├── llm.py       # Gemini API integration
│   ├── safety.py    # Safety checker
│   ├── executor.py  # Command execution
│   └── demo_mode.py # Demo mode
├── tests/           # Test files
├── setup.py         # Package configuration
├── pyproject.toml   # Modern packaging
└── README.md        # This file
```

## Safety Features

The shell includes comprehensive safety checks for:

- File deletion commands (`rm -rf`, etc.)
- System modification commands (`sudo`, `chmod 777`, etc.)
- Dangerous redirects (`> /dev/`, `> /etc/`, etc.)
- Shell injection patterns
- Fork bombs and other malicious patterns
- Network commands that pipe to shell

## Command History

All interactions are automatically logged to `~/.ai_shell_history.log` in JSON format:

```json
{
  "timestamp": "2024-01-15T10:30:00",
  "original_query": "find all PDF files",
  "generated_command": "find . -name \"*.pdf\"",
  "working_directory": "/home/user",
  "user": "user"
}
```

## API Configuration

The shell uses Google Gemini API with the following configuration:

- **Model**: `gemini-1.5-flash`
- **Temperature**: 0.1 (for consistent command generation)
- **Max tokens**: 500
- **Timeout**: 30 seconds

### Environment Variables

You can customize the behavior using environment variables in your `.env` file:

```bash
# Required
GEMINI_API_KEY=your_api_key_here

# Optional
GEMINI_MODEL=gemini-1.5-flash
GEMINI_TEMPERATURE=0.1
GEMINI_MAX_TOKENS=500
GEMINI_TIMEOUT=30
AISH_HISTORY_FILE=~/.ai_shell_history.log
AISH_DEBUG=false
```

## Testing

Run the basic tests to verify functionality:

```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

## Error Handling

- Network timeouts and API errors are handled gracefully
- Dangerous commands trigger warnings but don't prevent execution
- Rate limiting is handled with appropriate error messages
- Command execution has a 5-minute timeout
- Failed commands are logged with error details

## Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY environment variable is required"**
   - Set your API key: `export GEMINI_API_KEY=your_key_here`
   - Or create a `.env` file: `echo "GEMINI_API_KEY=your_key_here" > .env`

2. **"429 Too Many Requests"**
   - You've hit the API rate limit
   - Wait a few minutes and try again
   - Or use demo mode: `ai-shell-demo`

3. **"Command not found"**
   - Make sure you installed the package: `pip install ai-shell-cli`
   - Check if it's in your PATH: `which ai-shell-cli`

4. **Demo mode not working**
   - Try: `ai-shell-demo` (not `ai-shell-demo --help`)
   - Demo mode works without any API key

### Getting Help

- Run `:help` inside the shell for built-in help
- Check the command history: `cat ~/.ai_shell_history.log`
- Verify your API key is set: `echo $GEMINI_API_KEY`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Disclaimer

⚠️ **Use at your own risk!** While this tool includes safety checks, it's still possible to generate and execute dangerous commands. Always review generated commands before execution.

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure `OPENAI_API_KEY` is set correctly in `.env`
2. **Import Errors**: Install dependencies with `pip install -r requirements.txt`
3. **Network Issues**: Check your internet connection and API endpoint accessibility

### Getting Help

If you encounter issues:

1. Check the command history: `cat ~/.ai_shell_history.log`
2. Verify your API key is set: `echo $OPENAI_API_KEY`
3. Run tests: `python test_basic.py`
4. Check the help: `:help` in the shell 