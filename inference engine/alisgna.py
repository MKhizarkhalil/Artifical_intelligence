import pandas as pd

# Sample data for employee performance
employee_data = [
    {'employee_id': 1, 'name': 'khizar', 'kpi_score': 80, 'completed_projects': 5, 'peer_reviews': 4.5, 'attendance': 95},
    {'employee_id': 2, 'name': 'jaweria', 'kpi_score': 70, 'completed_projects': 3, 'peer_reviews': 3.8, 'attendance': 90},
    {'employee_id': 3, 'name': 'sufiyan', 'kpi_score': 90, 'completed_projects': 7, 'peer_reviews': 4.9, 'attendance': 98},
    {'employee_id': 4, 'name': 'Alishba', 'kpi_score': 10, 'completed_projects': 0, 'peer_reviews': 1, 'attendance': 10}
    # Add more employee data as needed
]

# Store the data in a structured format
df = pd.DataFrame(employee_data)

# Inference Engine to evaluate performance
def evaluate_performance(employee):
    strengths = []
    weaknesses = []
    
    if employee['kpi_score'] > 85:
        strengths.append('High KPI score')
    else:
        weaknesses.append('Low KPI score')
    
    if employee['completed_projects'] > 5:
        strengths.append('High number of completed projects')
    else:
        weaknesses.append('Low number of completed projects')
    
    if employee['peer_reviews'] > 4.0:
        strengths.append('Positive peer reviews')
    else:
        weaknesses.append('Average peer reviews')
    
    if employee['attendance'] > 95:
        strengths.append('Excellent attendance')
    else:
        weaknesses.append('Needs improvement in attendance')
    
    return strengths, weaknesses

# Generate personalized feedback
def generate_feedback(employee, strengths, weaknesses):
    feedback = f"Feedback for {employee['name']}:\n\n"
    
    if strengths:
        feedback += "Strengths:\n"
        for strength in strengths:
            feedback += f"- {strength}\n"
    
    if weaknesses:
        feedback += "\nAreas for Improvement:\n"
        for weakness in weaknesses:
            feedback += f"- {weakness}\n"
    
    feedback += "\nDevelopment Plan:\n"
    if 'Low KPI score' in weaknesses:
        feedback += "- Attend KPI improvement workshops.\n"
    if 'Low number of completed projects' in weaknesses:
        feedback += "- Take project management training.\n"
    if 'Average peer reviews' in weaknesses:
        feedback += "- Enhance teamwork and collaboration skills.\n"
    if 'Needs improvement in attendance' in weaknesses:
        feedback += "- Improve time management and punctuality.\n"
    
    return feedback

# Mock function to integrate with HR system
def integrate_with_hr_system(employee, feedback):
    print(f"Integrating feedback for {employee['name']} with HR system.")
    print("Feedback:", feedback)

# Function to show feedback for input employee name
def show_feedback(employee_name):
    employee = df[df['name'] == employee_name].iloc[0]
    strengths, weaknesses = evaluate_performance(employee)
    feedback = generate_feedback(employee, strengths, weaknesses)
    integrate_with_hr_system(employee, feedback)

# Example: Show feedback for employee named "Alice"
show_feedback("Alishba")
