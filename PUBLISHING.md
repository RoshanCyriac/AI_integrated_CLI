# Publishing AI-shell to PyPI

This guide explains how to publish the AI-shell package to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account on [PyPI](https://pypi.org/account/register/)
2. **TestPyPI Account**: Create an account on [TestPyPI](https://test.pypi.org/account/register/)
3. **API Tokens**: Generate API tokens for both PyPI and TestPyPI
4. **Build Tools**: Install required build tools

```bash
pip install build twine
```

## Building the Package

1. **Clean previous builds**:
   ```bash
   make clean
   ```

2. **Run tests**:
   ```bash
   make test
   ```

3. **Build the package**:
   ```bash
   make build
   ```

This creates distribution files in the `dist/` directory:
- `ai_shell-0.1.0.tar.gz` (source distribution)
- `ai_shell-0.1.0-py3-none-any.whl` (wheel distribution)

## Testing on TestPyPI

Before publishing to PyPI, test on TestPyPI:

1. **Upload to TestPyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   ```

2. **Test installation from TestPyPI**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ ai-shell
   ```

3. **Test the installed package**:
   ```bash
   ai-shell --help
   ```

## Publishing to PyPI

1. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

2. **Verify the upload**:
   Visit https://pypi.org/project/ai-shell/

## Version Management

To release a new version:

1. **Update version numbers**:
   - `pyproject.toml`: Update `version = "0.1.0"`
   - `setup.py`: Update `version="0.1.0"`
   - `ai_shell/__init__.py`: Update `__version__ = "0.1.0"`

2. **Update CHANGELOG.md** (if you have one)

3. **Build and publish**:
   ```bash
   make clean build
   twine upload dist/*
   ```

## Package Information

- **Package Name**: `ai-shell`
- **Description**: AI-Powered Interactive Shell - Convert natural language to shell commands
- **Author**: AI-shell Team
- **License**: MIT
- **Python Versions**: 3.8+
- **Dependencies**: requests, rich, python-dotenv

## Entry Points

The package provides two command-line tools:
- `ai-shell`: Main interactive shell
- `ai-shell-demo`: Demo mode without API calls

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Ensure your API tokens are correct
2. **Package Already Exists**: Update version number before publishing
3. **Build Errors**: Check that all required files are included in MANIFEST.in

### Useful Commands

```bash
# Check package contents
tar -tzf dist/ai_shell-0.1.0.tar.gz

# Validate package
twine check dist/*

# Test installation
pip install dist/ai_shell-0.1.0-py3-none-any.whl
```

## Security Notes

- Never commit API keys or sensitive data
- Use environment variables for configuration
- Keep dependencies updated
- Monitor for security vulnerabilities

## Support

For issues with publishing:
- Check PyPI documentation: https://packaging.python.org/
- Review PyPI help: https://pypi.org/help/
- Contact PyPI support if needed 