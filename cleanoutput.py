import re


def clean_and_color_text(input_file_path, output_file_path):
    # Define the regex pattern for ANSI escape sequences
    ansi_escape_pattern = r"\x1B\[[0-?]*[ -/]*[@-~]"

    # Define colors for each agent
    colors = {
        "Batch Process Detection Agent": "red",
        "Documentation Generation Agent": "blue",
        "Documentation Review Agent": "green",
        "Documentation Merger Agent": "purple",
    }

    # Read the input file
    with open(input_file_path, "r") as file:
        text = file.read()

    # Remove ANSI escape sequences
    cleaned_text = re.sub(ansi_escape_pattern, "", text)

    # Function to add color spans for each agent
    def add_color_span(match):
        agent = match.group(1)
        color = colors.get(agent, "black")  # Default to black if agent not found
        return f'<span style="color:{color}">[DEBUG]: == Working Agent: {agent}'

    # Apply color spans to debug lines
    colored_text = re.sub(
        r"\[DEBUG\]: == Working Agent: (Batch Process Detection Agent|Documentation Generation Agent|Documentation Review Agent|Documentation Merger Agent)",
        add_color_span,
        cleaned_text,
    )

    # Handle action blocks and coloring based on the last agent mentioned
    def handle_action_blocks(text):
        # Track the last agent encountered
        last_agent = None
        final_text = ""

        # Split the text into lines for processing
        lines = text.splitlines()

        # Initialize flags and storage for text block
        in_text_block = False
        current_text_block = ""

        for line in lines:
            if '"coworker":' in line:
                # Identify the action block and find the agent
                action_block_match = re.search(
                    r'"coworker": "(Batch Process Detection Agent|Documentation Generation Agent|Documentation Review Agent|Documentation Merger Agent)"',
                    line,
                )
                if action_block_match:
                    last_agent = action_block_match.group(1)

            if "Action:" in line:
                # Start a new text block
                in_text_block = True
                current_text_block = line
            elif in_text_block:
                # Continue accumulating text block
                current_text_block += "\n" + line
                if "> Finished chain." in line:
                    # End of the text block
                    in_text_block = False
                    # Apply the color based on the last agent encountered
                    color = colors.get(last_agent, "black")
                    final_text += (
                        f'<span style="color:{color}">{current_text_block}</span>\n'
                    )
                    current_text_block = ""
            else:
                # Lines outside of text blocks
                final_text += line + "\n"

        return final_text

    # Apply the function to handle action blocks
    colored_text = handle_action_blocks(colored_text)

    # Close the span at the end of the text for HTML validity
    colored_text += "</span>"

    # Bold the "Action: Ask question to co-worker" and its subsequent "Action Input" block
    colored_text = re.sub(
        r"(Action: Ask question to co-worker\s+Action Input: \{[^}]+\})",
        r"<b>\1</b>",
        colored_text,
        flags=re.DOTALL,
    )

    # Adding pre for new line effect
    colored_text = "<pre>" + colored_text + "</pre>"

    # Write the colored text to the output file
    with open(output_file_path, "w") as file:
        file.write(colored_text)


# Example usage
input_file = "conversation.txt"  # Replace with your actual input file path
output_file = "conversation.html"  # Replace with your desired output file path
clean_and_color_text(input_file, output_file)

print(f"Processed text with color coding has been saved to {output_file}")
