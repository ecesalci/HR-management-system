# HR Recruitment and Management System

## Overview

The HR Recruitment and Management System is a terminal-based Python application that simulates an automated candidate screening process. The program evaluates each candidate against a predefined list of open job positions and determines whether they qualify for a role, based on their primary skill, graduation year, professional experience, and academic performance (GPA).

The system maintains an in-memory list of jobs, each defined by a company name, position title, required skill, and minimum experience requirement. As candidates are successfully hired, the corresponding position is marked as filled and is no longer offered to subsequent candidates during the same session.

## How It Works

1. **Candidate Name**
   The program starts by asking for the candidate's name. Empty input is rejected, and the candidate may type `exit` at any point to close the system.

2. **Primary Skill**
   The candidate enters their primary skill, which must be one of: `python`, `al`, `data`, or `any`. The program then checks whether any open position currently requires that skill (or accepts `any` skill). If no matching position exists, the system lists the other currently open positions as alternatives and restarts the process for a new candidate.

3. **Graduation Year**
   The candidate provides their graduation year. The system calculates how many years have passed since graduation (based on the current year) and uses this to decide which evaluation path to follow:

   - **More than 1 year since graduation → Experience-based evaluation**
     The candidate enters their total professional experience in months. The system searches for an open position matching the candidate's skill where the required minimum experience is less than or equal to the candidate's experience. If a match is found, the candidate is hired and the position is closed.

   - **1 year or less since graduation → GPA-based evaluation (recent graduates)**
     The system first checks whether any open entry-level or internship position (minimum experience of 0 months) matches the candidate's skill. If none exists, alternative entry-level openings in other domains are displayed instead.
     If a matching entry-level position exists, the candidate is asked to enter their GPA in the format `system/score` (for example, `4/3.7`), which is converted into a ratio (score divided by system) for evaluation. Positions requiring the `any` skill require a minimum GPA ratio of 2.5/4.0, while all other skill-specific entry-level positions require a minimum ratio of 3.0/4.0. If the candidate's GPA ratio meets or exceeds the required threshold, they are hired and the position is closed; otherwise, the candidate is informed that they do not meet the GPA requirement.

4. **Outcome**
   At the end of each evaluation, the candidate is informed whether they have been hired, including the position and company, or whether they did not meet the requirements for any available role.

5. **Repeating the Process**
   Once a candidate's evaluation is complete, the system loops back to the beginning, allowing a new candidate to be processed. The candidate may exit the program at any input prompt by typing `exit`.

## Running the Program

```bash
python hr_management_system.py
```
