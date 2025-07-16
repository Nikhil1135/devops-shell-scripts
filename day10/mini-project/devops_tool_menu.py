# devops_tool_menu.py

# Dictionary to hold DevOps tools and their descriptions
devops_tools = {
    "Docker": "A platform for containerizing applications.",
    "Git": "A version control system to track code changes.",
    "Jenkins": "An automation server used for CI/CD pipelines.",
    "Kubernetes": "An orchestration tool for managing containers.",
    "Terraform": "An IaC tool for provisioning cloud infrastructure."
}

def show_menu():
    print("\n=== DevOps Tools Menu ===")
    for idx, tool in enumerate(devops_tools.keys(), 1):
        print(f"{idx}. {tool}")
    print(f"{len(devops_tools) + 1}. Exit")

def show_description(choice):
    tool_list = list(devops_tools.keys())
    if 1 <= choice <= len(tool_list):
        selected_tool = tool_list[choice - 1]
        print(f"\n🔹 {selected_tool}: {devops_tools[selected_tool]}")
    else:
        print("❌ Invalid choice. Please try again.")

# Main logic
while True:
    show_menu()
    try:
        user_input = int(input("Enter your choice: "))
        if user_input == len(devops_tools) + 1:
            print("👋 Exiting. Thanks for learning!")
            break
        else:
            show_description(user_input)
    except ValueError:
        print("⚠️ Please enter a valid number.")
