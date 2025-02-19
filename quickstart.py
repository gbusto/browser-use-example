from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Go to Apple's website and tell me what products they show on it",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
        #llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()

    # Print the final result as a string
    final_result = result.final_result()

    # Print model "thoughts"
    thoughts = result.model_thoughts()
    print("============ MODEL THOUGHTS =============")
    for thought in thoughts:
        summary = thought.page_summary
        previous_goal = thought.evaluation_previous_goal
        memory = thought.memory
        next_goal = thought.next_goal

        print(f"\nSummary: {summary}")
        print(f"Previous Goal: {previous_goal}")
        print(f"Memory: {memory}")
        print(f"Next Goal: {next_goal}\n")

    print("============ END MODEL THOUGHTS =============")

    # Print model actions
    actions = result.model_actions()
    print("============ MODEL ACTIONS =============")
    for action in actions:
        print(action)
    print("============ END MODEL ACTIONS =============")

    # Print action results
    action_results = result.action_results()
    print("============ ACTION RESULTS =============")
    for action_result in action_results:
        extracted_content = action_result.extracted_content[:100] # Truncated
        error = action_result.error
        in_memory = action_result.include_in_memory
        print(f"Extracted Content: {extracted_content}")
        print(f"Error: {error}")
        print(f"In Memory: {in_memory}")
    print("============ END ACTION RESULTS =============")

    # Read the implementation of AgentHistoryList to see more, including how to save and load this too

asyncio.run(main())