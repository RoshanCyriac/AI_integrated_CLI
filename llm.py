"""
LLM client for OpenRouter API integration.
Handles command generation and explanation.
"""

import os
import json
import requests
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is required")
        
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")
        self.temperature = float(os.getenv("OPENROUTER_TEMPERATURE", "0.1"))
        self.max_tokens = int(os.getenv("OPENROUTER_MAX_TOKENS", "500"))
        self.timeout = int(os.getenv("OPENROUTER_TIMEOUT", "30"))
        
    def _make_request(self, messages: list) -> Optional[str]:
        """Make a request to OpenRouter API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/aish-shell",
            "X-Title": "aish interactive shell"
        }
        
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except (KeyError, IndexError) as e:
            raise Exception(f"Unexpected API response format: {e}")
    
    def generate_command(self, query: str) -> str:
        """Generate a shell command from natural language query."""
        system_prompt = """You are a helpful assistant that converts natural language requests into safe shell commands.

Rules:
1. Generate ONLY the shell command, no explanations or additional text
2. Use safe, standard Unix/Linux commands
3. Avoid dangerous commands like rm -rf, sudo, or commands that could damage the system
4. Prefer find, ls, grep, awk, sed, and other safe utilities
5. If the request is unclear or potentially dangerous, return "SAFETY_CHECK_FAILED"
6. Keep commands simple and readable
7. Use proper quoting for file paths with spaces
8. For file operations, be conservative and safe

Examples:
- "find all PDF files" → find . -name "*.pdf"
- "list files modified today" → find . -type f -mtime -1
- "show disk usage" → du -sh *
- "search for text in files" → grep -r "text" .
- "delete all files" → SAFETY_CHECK_FAILED (too dangerous)
- "find large files" → find . -type f -size +100M
- "list python files" → find . -name "*.py"
- "show memory usage" → free -h
- "check disk space" → df -h

Query: {query}"""

        messages = [
            {"role": "system", "content": system_prompt.format(query=query)},
            {"role": "user", "content": query}
        ]
        
        result = self._make_request(messages)
        
        if result and result != "SAFETY_CHECK_FAILED":
            # Clean up the response - remove any markdown formatting
            result = result.strip()
            if result.startswith("```"):
                result = result.split("\n", 1)[1]
            if result.endswith("```"):
                result = result.rsplit("\n", 1)[0]
            return result.strip()
        
        raise Exception("Command generation failed safety check")
    
    def explain_command(self, command: str, original_query: str) -> str:
        """Explain what a shell command does."""
        system_prompt = """You are a helpful assistant that explains shell commands in simple terms.

Explain what the command does, what each part means, and what the user can expect to see as output.
Keep explanations clear and beginner-friendly.

Command: {command}
Original request: {original_query}"""

        messages = [
            {"role": "system", "content": system_prompt.format(command=command, original_query=original_query)},
            {"role": "user", "content": f"Please explain this command: {command}"}
        ]
        
        result = self._make_request(messages)
        return result or "Unable to generate explanation." 