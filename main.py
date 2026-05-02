from agent import run_agent

def main():
    print("Simple AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        response = run_agent(user_input)

        print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()