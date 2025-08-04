#!/usr/bin/env python3
"""
Build script for AI-shell package
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ {description} failed:")
        print(result.stderr)
        sys.exit(1)
    print(f"✅ {description} completed")
    return result.stdout

def clean_build():
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    print("✅ Clean completed")

def build_package():
    """Build the package."""
    clean_build()
    run_command("python -m build", "Building package")
    print("📦 Package built successfully!")

def test_install():
    """Test installing the package."""
    print("🧪 Testing package installation...")
    run_command("pip install -e .", "Installing package in development mode")
    print("✅ Package installation test completed")

def run_tests():
    """Run the test suite."""
    print("🧪 Running tests...")
    run_command("python -m pytest tests/ -v", "Running test suite")
    print("✅ Tests completed")

def check_quality():
    """Run code quality checks."""
    print("🔍 Running code quality checks...")
    run_command("black --check .", "Checking code formatting")
    run_command("flake8 .", "Running linting")
    print("✅ Code quality checks completed")

def main():
    """Main build function."""
    if len(sys.argv) < 2:
        print("Usage: python build.py [build|test|install|clean|quality|all]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "build":
        build_package()
    elif command == "test":
        run_tests()
    elif command == "install":
        test_install()
    elif command == "clean":
        clean_build()
    elif command == "quality":
        check_quality()
    elif command == "all":
        check_quality()
        run_tests()
        build_package()
        test_install()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main() 