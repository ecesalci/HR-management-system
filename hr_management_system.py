# Project: HR Recruitment and Management System
# Purpose: To automate the candidate filtering process based on skill, experience, and GPA.

# Data Structure: [Company, Position, Required_Skill, Min_Experience_Months, Is_Open]
jobs = [
    ["Tech Solutions", "AL Developer", "al", 24, True],
    ["Tech Solutions", "Python Developer", "python", 12, True],
    ["Tech Solutions", "Junior Python Developer", "python", 0, True],
    ["Apex Corporation", "Data Scientist", "data", 36, True],
    ["Value Enterprises", "Intern", "any", 0, True],
    ["Value Enterprises", "Junior AL Developer", "al", 0, True]
]

current_year = 2026
valid_skills = ["python", "al", "data", "any"]

while True:
    # Separator for a cleaner terminal interface
    print("\n" + "="*60)
    print("--- Welcome to the HR Management System ---")
    
    # Input candidate name
    name_input = input("\nPlease enter your name (type 'exit' to close the system): ").strip()
    
    if name_input.lower() == 'exit':
        print("\nExiting the system. Goodbye.\n")
        break
        
    if name_input == "":
        print("\nInvalid input. Name cannot be empty. Restarting process.")
        continue

    name = name_input

    # Input primary skill
    print("\nWelcome, " + name + ". Let's begin by assessing your primary skill.")
    skill_input = input("\nEnter your primary skill (e.g., python, al, data, any, or 'exit' to quit): ").strip().lower()
    
    if skill_input == 'exit':
        print("\nExiting the system. Goodbye.\n")
        break
        
    if skill_input == "":
        print("\nInvalid input. Skill cannot be empty. Restarting process.")
        continue

    if skill_input not in valid_skills:
        print("\nInvalid skill entered. Please enter a valid skill (python, al, data, any). Restarting process.")
        continue

    skill = skill_input
    
    # Check for available positions
    is_position_available = False
    for job in jobs:
        if job[4] == True and (job[2] == skill or job[2] == "any"):
            is_position_available = True
            break 
            
    if not is_position_available:
        print("\nUnfortunately, there are currently no available positions or all positions are filled for the '" + skill + "' skill.")
        
        # Display alternative job openings if the requested skill is unavailable
        alternatives = []
        for job in jobs:
            if job[4] == True:
                alternatives.append("- " + job[1] + " at " + job[0] + " (Requires: " + job[2] + ", Min Experience: " + str(job[3]) + " months)")
        
        if len(alternatives) > 0:
            print("\nHowever, we still have the following open positions across our companies:")
            for alt in alternatives:
                print(alt)
        else:
            print("\nIn fact, all positions across all departments are currently filled.")
            
        continue 

    # Input graduation year
    grad_year_input = input("\nPlease enter your graduation year (e.g., 2023, 2026, or 'exit' to quit): ").strip()
    
    if grad_year_input.lower() == 'exit':
        print("\nExiting the system. Goodbye.\n")
        break
        
    if not grad_year_input.isdigit():
        print("\nInvalid input. Please enter a valid numeric year. Restarting process.")
        continue
        
    graduation_year = int(grad_year_input)
    years_passed = current_year - graduation_year
    is_hired = False

    # Logic for experienced candidates (Graduated more than 1 year ago)
    if years_passed > 1:
        exp_input = input("\nPlease enter your total months of professional experience (or 'exit' to quit): ").strip()
        
        if exp_input.lower() == 'exit':
            print("\nExiting the system. Goodbye.\n")
            break
            
        if not exp_input.isdigit():
            print("\nInvalid input. Please enter experience in months as an integer. Restarting process.")
            continue
            
        experience = int(exp_input)

        for job in jobs:
            if job[4] == True and (job[2] == skill or job[2] == "any") and experience >= job[3]:
                print("\nCongratulations, " + name + "! You have been hired as a " + job[1] + " at " + job[0] + ".")
                job[4] = False 
                is_hired = True
                break 

    # Logic for recent graduates (1 year or less since graduation)
    else:
        has_entry_role = False
        other_entry_roles = []
        
        for job in jobs:
            if job[4] == True and job[3] == 0: 
                if job[2] == skill or job[2] == "any":
                    has_entry_role = True
                else:
                    other_entry_roles.append("- " + job[1] + " at " + job[0] + " (Requires: " + job[2] + ")")
                    
        if not has_entry_role:
            print("\nBad news, " + name + ". All entry-level and intern positions for '" + skill + "' are currently filled.")
            if len(other_entry_roles) > 0:
                print("\nHowever, we still have the following entry-level positions available in other domains:")
                for role in other_entry_roles:
                    print(role)
            else:
                print("\nIn fact, all of our entry-level positions across all departments are currently filled.")
            continue 

        # GPA input validation loop (Keeps asking until valid input)
        is_gpa_valid = False
        while not is_gpa_valid:
            gpa_input = input("\nSince you are a recent graduate, please enter your GPA (e.g., 4/3.7 or 5/2.3, or 'exit' to quit): ").strip()
            
            if gpa_input.lower() == 'exit':
                break

            gpa_parts = gpa_input.split("/")
            
            if len(gpa_parts) != 2:
                print("\nInvalid input format. Please follow the requested format (e.g., 4/3.7).")
                continue
                
            sys_part = gpa_parts[0].strip()
            score_part = gpa_parts[1].strip()

            if not sys_part.replace(".", "", 1).isdigit() or not score_part.replace(".", "", 1).isdigit():
                print("\nInvalid input format. Please use numeric values.")
                continue

            gpa_system = float(sys_part) 
            gpa_score = float(score_part)  
            
            if gpa_system == 0:
                print("\nInvalid input. GPA system cannot be zero.")
                continue
            
            is_gpa_valid = True
            
        if gpa_input.lower() == 'exit':
            print("\nExiting the system. Goodbye.\n")
            break

        gpa_ratio = gpa_score / gpa_system
        
        # Hiring logic for entry-level positions based on GPA
        for job in jobs:
            if job[4] == True and (job[2] == skill or job[2] == "any") and job[3] == 0:
                
                # Manual if-else logic for GPA ratios as requested
                if job[2] == "any":
                    min_ratio = 2.5 / 4.0
                else:
                    min_ratio = 3.0 / 4.0
                
                if gpa_ratio >= min_ratio:
                    print("\nCongratulations, " + name + "! With your academic performance, you have been hired as a " + job[1] + " at " + job[0] + ".")
                    job[4] = False 
                    is_hired = True
                    break 
                    
        if not is_hired:
            print("\nWe regret to inform you that your GPA does not meet the requirements for our entry-level or intern positions.")
            is_hired = True 

    if not is_hired:
        print("\nUnfortunately, you do not meet the minimum requirements for the available positions at this time.")