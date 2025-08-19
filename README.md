# whoami - Personal Context MCP Server

A local Model Context Protocol (MCP) server that provides your AI agents with comprehensive personal context about who you are, enabling more personalized and contextually aware conversations.

## Overview

The `whoami` MCP server acts as a personal knowledge base that AI agents can query to understand your identity, work situation, preferences, schedule, projects, and goals. Instead of repeatedly explaining your background in every conversation, your AI assistant can automatically access relevant context about you.

## TODO

Add support for custom data categories/generalize tools to handle any data category
Implement RAG/GraphRAG for more advanced context retrieval

## Features

### Information Categories
- **Basic Info**: Name, contact details, location, demographics, personal background
- **Professional Info**: Job title, company, career history, skills, team structure
- **Work Preferences**: Communication style, work habits, meeting preferences, quirks
- **Schedule Patterns**: Daily routines, weekly patterns, availability, optimal times
- **Current Projects**: Active work, responsibilities, deadlines, team information
- **Technical Stack**: Programming languages, frameworks, tools, technical preferences
- **Goals & Objectives**: Short-term and long-term goals, KPIs, development priorities

### Capabilities
- **Read Operations**: Query any category of personal information
- **Update Operations**: Modify and update information as it changes
- **Safe File Handling**: Automatic directory creation and error handling
- **Structured Data**: Organized text files for easy maintenance

## Setup Instructions for Claude Desktop

### Prerequisites
- Python 3.13 or higher
- Poetry (for dependency management)
- Claude Desktop application

### Installation

1. **Clone and setup the project:**
   ```bash
   git clone <your-repo-url>
   cd whoami
   poetry install
   ```

2. **Create your personal data files:**
   Create a `data` directory in the project root and add your personal information:
   ```bash
   mkdir data
   ```
   
   Create these text files with your information:
   - `data/basic_info.txt` - Your name, email, location, age, languages, background
   - `data/professional.txt` - Job title, company, career history, skills, achievements
   - `data/preferences.txt` - Communication style, work preferences, meeting style
   - `data/schedule_patterns.txt` - Daily schedule, weekly patterns, availability
   - `data/projects_current.txt` - Active projects, deadlines, responsibilities
   - `data/technical_stack.txt` - Programming languages, frameworks, tools
   - `data/objectives.txt` - Goals, KPIs, development priorities

3. **Configure Claude Desktop:**
   
   Open your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   
   Add the whoami server configuration:
   ```json
    {
    "mcpServers": {
        "whoami": {
        "command": "python3",
        "args": [
            "/PathToYourWhoamiProject/whoami/mcp_launcher.py"
        ]
        }
    }
    }
   ```
   
   **Important**: Replace `/PathToYourWhoamiProject` with the actual absolute path to your whoami project directory.

4. **Restart Claude Desktop** to load the new MCP server.

### Updating Your Information

You can update your personal information in two ways:

1. **Direct file editing**: Modify the text files in the `data/` directory
2. **Through Claude**: Ask Claude to update specific information, and it will use the update tools to modify the files

## Privacy & Security

- All data is stored locally on your machine
- No information is sent to external servers
- You have complete control over what information is stored
- Data files are plain text for easy review and editing

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - see LICENSE file for details.
