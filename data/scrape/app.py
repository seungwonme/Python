from scrapegraphai.graphs import SmartScraperGraph
import argparse
import json

graph_config = {
    "llm": {
        "model": "ollama/llama3:8b",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "verbose": True,
}

parser = argparse.ArgumentParser(description="Run the smart scraper graph")

# Add the arguments
parser.add_argument(
    "--source",
    "-s",
    type=str,
    default="https://github.com/VinciGit00/Scrapegraph-ai",
    help="The URL to scrape",
)
parser.add_argument(
    "--prompt",
    "-p",
    type=str,
    default="Extract the title, description, and related terms from the page",
    help="The prompt to use",
)
parser.add_argument(
    "--output",
    "-o",
    type=str,
    default="res.json",
    help="The output file",
)

# Parse the arguments
args = parser.parse_args()

smart_scraper_graph = SmartScraperGraph(
    prompt=args.prompt,
    # also accepts a string with the already downloaded HTML code
    source=args.source,
    config=graph_config,
)

result = smart_scraper_graph.run()
# Write the result to a JSON file
with open(args.output, "w") as file:
    json.dump(result, file)
