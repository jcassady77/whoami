#!/usr/bin/env python3
"""
MCP server launcher that sets up the environment and runs the server.
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Change to project directory
os.chdir(os.path.dirname(__file__))

# Run directly without Poetry to avoid startup delays
from whoami.stdio_server import mcp
mcp.run()