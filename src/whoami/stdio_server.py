from pathlib import Path
from fastmcp import FastMCP

mcp = FastMCP(
    "whoami",
    description="Comprehensive personal context server providing detailed information about the user across multiple categories including identity, work, preferences, schedule, projects, and technical expertise."
)
DATA_DIR = Path(__file__).parent.parent.parent / "data"

def _read_data_file(filename: str) -> str:
    """Helper function to read data files safely."""
    try:
        with open(DATA_DIR / filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return f"{filename} not found"
    except Exception as e:
        return f"Error reading {filename}: {str(e)}"

@mcp.tool(
    name="get_basic_info",
    description="Get core identity information including name, contact details, location, demographics, and personal background. Use when you need to know who you're talking to, how to address them, or basic personal details."
)
def get_basic_info() -> str:
    """Returns user's name, email, location, age, languages, and personal background."""
    return _read_data_file("basic_info.txt")

@mcp.tool(
    name="get_professional_info",
    description="Get detailed professional information including current job, career history, skills, achievements, and team structure. Use when discussing work, career advice, professional topics, or understanding their expertise level."
)
def get_professional_info() -> str:
    """Returns job title, company, career history, skills, team structure, and professional achievements."""
    return _read_data_file("professional.txt")

@mcp.tool(
    name="get_work_preferences",
    description="Get communication style, work preferences, meeting style, and personal quirks. Use when planning interactions, scheduling meetings, or understanding how they like to work and communicate."
)
def get_work_preferences() -> str:
    """Returns communication preferences, work style, meeting preferences, and personal quirks."""
    return _read_data_file("preferences.txt")

@mcp.tool(
    name="get_schedule_patterns",
    description="Get daily schedule, weekly patterns, regular meetings, and time preferences. Use when scheduling meetings, understanding availability, or planning time-sensitive discussions."
)
def get_schedule_patterns() -> str:
    """Returns daily schedule, weekly patterns, regular meetings, and optimal times for different activities."""
    return _read_data_file("schedule_patterns.txt")

@mcp.tool(
    name="get_current_projects",
    description="Get active projects, responsibilities, deadlines, and team information. Use when discussing current work, understanding priorities, or coordinating on project-related topics."
)
def get_current_projects() -> str:
    """Returns current active projects, status, deadlines, team members, and responsibilities."""
    return _read_data_file("projects_current.txt")

@mcp.tool(
    name="get_technical_stack",
    description="Get programming languages, frameworks, tools, and technical preferences. Use when discussing technical topics, code, tools, architecture decisions, or understanding their technical expertise."
)
def get_technical_stack() -> str:
    """Returns programming languages, AI/ML frameworks, development tools, cloud platforms, and preferred tech stack."""
    return _read_data_file("technical_stack.txt")

@mcp.tool(
    name="get_goals_objectives",
    description="Get short-term and long-term goals, objectives, KPIs, and career development plans. Use when discussing future plans, career growth, goal setting, or strategic planning conversations."
)
def get_goals_objectives() -> str:
    """Returns current quarter goals, 2025 objectives, KPIs, and personal development priorities."""
    return _read_data_file("objectives.txt")

if __name__ == "__main__":
    mcp.run()