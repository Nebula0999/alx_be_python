task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case priority:
            if priority == "high":
                if time_bound == "yes":
                    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            elif priority == "medium":
                if time_bound == "yes": 
                    print(f"'{task}' is a medium priority task that can be done later today!")
            elif priority == "low":
                if time_bound == "no":
                    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")