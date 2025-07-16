devops_tools = ["Docker ", "Git", "Jenkins", "k8s"]

for tools in devops_tools:
    print(tools)


for  i in range(len(devops_tools)):
    print(f"Index {i}  --> Value {devops_tools[i]}")

count = 0
while count < 3:
    print(f"tool is {devops_tools[count]}")
    count += 1