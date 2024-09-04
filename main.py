import os, sys

from crewai import Agent, Task, Process, Crew
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import yaml

load_dotenv()


def load_yaml(file_path):
    """Load data from a YAML file."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


agents_config = load_yaml("config/agents.yml")
tasks_config = load_yaml("config/tasks.yml")


def process_legacy_code(code_text, filename, output_template):
    """
    - define agents that are going to analyse and document COBOL code with AI tools

    """
    # batchProcessDetectionAgent = Agent(
    #     config=agents_config["batchProcessDetectionAgent"],
    # )

    documentationGenerationAgent = Agent(
        config=agents_config["documentationGenerationAgent"],
        memory=True,
    )

    documentationReviewAgent = Agent(
        config=agents_config["documentationReviewAgent"],
        memory=True,
    )

    # documentationFinalizerAgent = Agent(
    #     config=agents_config["documentationFinalizerAgent"],
    #     memory=True,
    # )

    # task_batchProcessDetection = Task(
    #     config=tasks_config["task_batchProcessDetection"],
    #     agent=batchProcessDetectionAgent,
    # )

    task_documentationGeneration = Task(
        config=tasks_config["task_documentationGeneration"],
        agent=documentationGenerationAgent,
    )

    task_documentationReview = Task(
        config=tasks_config["task_documentationReview"],
        agent=documentationReviewAgent,
    )

    # task_documentationConclusion = Task(
    #     config=tasks_config["task_documentationConclusion"],
    #     agent=documentationFinalizerAgent,
    # )

    crew = Crew(
        memory=True,
        full_output=True,
        agents=[
            documentationGenerationAgent,
            documentationReviewAgent,
        ],
        tasks=[
            task_documentationGeneration,
            task_documentationReview,
        ],
        verbose=True,
        process=Process.sequential,
        # embedder={
        #     "provider": "google",
        #     "config": {
        #         "model": "models/embedding-001",
        #         "task_type": "retrieval_document",
        #         "title": "Embeddings for Embedchain",
        #     },
        # },
    )

    return crew.kickoff(
        inputs={
            "code_text": code_text,
            "filename": filename,
            "output_template": output_template,
        }
    )

    # return task_parse.execute()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        input_filename = sys.argv[1]
        model_name = sys.argv[2]
        print(f"Processing file: {input_filename}")
        print(f"Using model: {model_name}")

        with open(input_filename, "r") as f:
            code_text = f.read()
        print(code_text)
        print("======== END SOURCE CODE ==========")

        with open("config/template_batch_pl1.md", "r") as template_file:
            output_template = template_file.read()

        # Get your crew to work!
        result = process_legacy_code(code_text, input_filename, output_template)

        # Create the output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)

        # Generate output filename based on the model name
        output_filename = f"output/{model_name}.md"

        # Write the result to the file
        with open(output_filename, "w") as f:
            f.write(result.raw)

        print(f"Result written to: {output_filename}")
        print(result.raw)
    else:
        print("Usage: python main.py <input_filename> <model_name>")
        sys.exit(1)
