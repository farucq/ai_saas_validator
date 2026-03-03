# AI SaaS Validator

An intelligent AI-powered tool that validates SaaS startup ideas by analyzing market potential, competitors, monetization strategies, and risks.

## Features

- **Market Research Agent**: Analyzes market size, trends, and target audience
- **Competitor Analysis**: Identifies top competitors with detailed feature comparison tables
- **Monetization Strategy**: Suggests pricing models and revenue streams
- **Risk Assessment**: Evaluates technical, market, and regulatory risks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/farucq/ai_saas_validator.git
cd ai_saas_validator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Or use the core orchestrator directly:
```python
from core.orchestrator import run_agents

result = run_agents("AI-powered Resume Optimizer")
print(result)
```

## API Keys Required

- **Groq API Key**: For LLM interactions (get from https://console.groq.com)
- **Serper API Key**: For web search functionality (get from https://serper.dev)

## Project Structure

```
├── agents/           # Specialized analysis agents
├── core/            # Core orchestration and tools
├── config/          # Configuration settings
├── utils/           # Helper utilities
├── app.py           # Streamlit web interface
└── requirements.txt # Python dependencies
```

## Tech Stack

- **Backend**: Python
- **LLM**: Groq (Llama 3.1)
- **Search**: Serper API
- **UI**: Streamlit
- **Logging**: Python logging with rotation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
