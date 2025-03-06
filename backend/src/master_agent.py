from .gemini_realtime_api import GeminiRealtimeAPI  # Import the Gemini API client

class MasterAgent:
    def __init__(self, coder_agent=None, assistant_agent=None, computer_agent=None):
        """
        Initialize the Master Agent with references to the sub-agents and Gemini API client.
        """
        self.gemini = GeminiRealtimeAPI()  # Initialize Gemini API client
        self.coder_agent = coder_agent  # Coder Agent instance
        self.assistant_agent = assistant_agent # assistant Agent instance
        self.computer_agent = computer_agent  # Computer Agent instance

    def process_input(self, user_input: str) -> str:
        """
        Process user input and delegate tasks to the appropriate sub-agent(s).
        """
        try:
            # Step 1: Use Gemini API to understand the task
            task_description = self.gemini.analyze(user_input)

            # Step 2: Check if the task requires collaboration between agents
            if self._requires_collaboration(task_description):
                return self._handle_collaborative_task(task_description)
            else:
                # Step 3: Delegate to a single agent if no collaboration is needed
                return self._delegate_to_single_agent(task_description)
        except Exception as e:
            # Handle errors gracefully
            return f"Error processing input: {str(e)}"

    def _requires_collaboration(self, task_description: str) -> bool:
        """
        Determine if the task requires collaboration between multiple agents.
        """
        # Example logic: Check if the task involves coding, browsing, and system operations
        return (
            "code" in task_description.lower()
            and "assist" in task_description.lower()
            and "computer" in task_description.lower()
        )

    def _handle_collaborative_task(self, task_description: str) -> str:
        """
        Handle tasks that require collaboration between multiple agents.
        """
        print("Handling collaborative task...")

        # Step 1: assistant Agent fetches data
        print("Invoking assistant Agent to fetch data...")
        data_from_assistant = self.assistant_agent.process(task_description)

        # Step 2: Coder Agent processes the fetched data
        print("Invoking Coder Agent to process data...")
        code_result = self.coder_agent.process(data_from_assistant)

        # Step 3: Computer Agent executes the generated code or commands
        print("Invoking Computer Agent to execute commands...")
        final_result = self.computer_agent.process(code_result)

        # Step 4: Return the final result
        return final_result

    def _delegate_to_single_agent(self, task_description: str) -> str:
        """
        Delegate tasks to a single agent if no collaboration is needed.
        """
        if "code" in task_description.lower():
            print("Delegating to Coder Agent...")
            return self.coder_agent.process(task_description)
        elif "browse" in task_description.lower() or "search" in task_description.lower():
            print("Delegating to assistant Agent...")
            return self.assistant_agent.process(task_description)
        elif "computer" in task_description.lower() or "system" in task_description.lower():
            print("Delegating to Computer Agent...")
            return self.computer_agent.process(task_description)
        else:
            # If no sub-agent is needed, respond directly using Gemini API
            print("Responding directly using Gemini API...")
            return self.gemini.generate_response(task_description)