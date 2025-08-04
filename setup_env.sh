#!/bin/bash
# Environment setup script for aish interactive shell

set -e

echo "🔧 Setting up aish interactive shell environment..."

# Check if .env file exists
if [ -f ".env" ]; then
    echo "⚠️  .env file already exists. Backing up to .env.backup"
    cp .env .env.backup
fi

# Create .env file from template
if [ -f "env.example" ]; then
    cp env.example .env
    echo "✅ Created .env file from template"
else
    echo "❌ env.example not found. Creating basic .env file..."
    cat > .env << EOF
# aish Interactive Shell Environment Variables
OPENROUTER_API_KEY=your_openrouter_api_key_here
EOF
fi

echo ""
echo "📝 Please edit .env file and add your Google Gemini API key:"
echo "   nano .env"
echo ""
echo "🔑 Get your API key from: https://makersuite.google.com/app/apikey"
echo ""
echo "💡 After setting your API key, you can:"
echo "   1. Start the shell: python main.py"
echo "   2. Run tests: python test_basic.py"
echo "   3. Install dependencies: pip install -r requirements.txt"
echo ""
echo "🎉 Environment setup complete!" 