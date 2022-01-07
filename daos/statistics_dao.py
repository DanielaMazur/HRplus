from models import db
  
def absenteism_cost(total_lost_hours : float,
                    avg_wage : float,
                    supervisors_hours_lost : float,
                    avg_supervisor_wage : float,
                    n_employees : int):
    '''
        This function computes the company's cost of absenteism per employee.
    :param total_lost_hours: float
        The total lost hours due to absenteism.
    :param avg_wage: float
        The average wage of the employees that were absent.
    :param supervisors_hours_lost: float
        The number of hours lost by supervisors due to managing absent employees.
    :param avg_supervisor_wage: float
        The average supervisor wage.
    :param n_employees: int
        The number of employees that work in the company.
    :return: float
        The cost of absenteism per employee.
    '''
    # Computing total compensation.
    total_compensation = avg_wage * total_lost_hours

    # Computing the total supervisor salary lost.
    total_supervisor_salary_lost = supervisors_hours_lost * avg_supervisor_wage

    # Computing the substitute employees cost.
    substitute_employees_cost = avg_wage * total_lost_hours

    # Computing the Total cost of absenteism.
    total_cost_of_absenteism = total_compensation + total_supervisor_salary_lost + substitute_employees_cost

    # Computing the absenteism cost per employee.
    absenteism_cost_per_employee = total_cost_of_absenteism / n_employees

    return absenteism_cost_per_employee

def replacement_cost(advertising_fees_per_termination : float,
                     job_availability_communication_time : float,
                     hr_employees_pay_rate : float,
                     n_turnover : float,
                     preemployment_admin_fun_time : float,
                     avg_hr_pay_rate : float,
                     n_applications : float,
                     interview_time : float,
                     interviewers_pay_rate : float,
                     n_interviews : float,
                     cost_of_materials_per_person : float,
                     cost_of_scoring_per_person : float,
                     n_test_given : float,
                     meeting_time : float,
                     hr_pay_rate : float,
                     dept_representative_pay_rate : float,
                     n_meetings : float,
                     acquiring_and_disseminating_time : float,
                     n_turnover_replace : float):
    '''
        This function computes the replacement cost of the company.
    :param advertising_fees_per_termination: float
        Advertising and employment agency fees per termination.
    :param job_availability_communication_time: float
        Time required for communication of the job availability.
    :param hr_employees_pay_rate: float
        The HR department employees pay rate.
    :param n_turnover: float
        The number of turnovers replaced during period.
    :param preemployment_admin_fun_time: float
        The time required by the HR department for preemployment administrative function.
    :param avg_hr_pay_rate: float
        The average HR department employeement pay rate.
    :param n_applications: float
        The number of applications during period.
    :param interview_time: float
        The time required for interview.
    :param interviewers_pay_rate: float
        The interviewers pay rate.
    :param n_interviews: float
        The number of interviews during period.
    :param cost_of_materials_per_person: float
        The cost of materials spent per interviewed person.
    :param cost_of_scoring_per_person: float
        The cost of scoring spent per interviewed person.
    :param n_test_given: float
        The number of tests given during period.
    :param meeting_time: float
        The time required for meeting.
    :param hr_pay_rate: float
        The HR department employees pay rate.
    :param dept_representative_pay_rate: float
        The department representative pay rate.
    :param n_meetings: float
        The number of meetings during the period.
    :param acquiring_and_disseminating_time: float
        The time required for acquiring and disseminating information.
    :param n_turnover_replace: float
        The number of turnover replacements during period.
    :return: float
        The total replacement cost.
    '''
    # Computing the first component of the replacement cost.
    R1 = (advertising_fees_per_termination + (job_availability_communication_time * hr_employees_pay_rate)) * n_turnover

    # Computing the second component of the replacement cost.
    R2 = preemployment_admin_fun_time * avg_hr_pay_rate * n_applications

    # Computing the third component of the replacement cort.
    R3 = interview_time * interviewers_pay_rate * n_interviews

    # Computing the fourth component of the replacement cost.
    R4 = (cost_of_materials_per_person + cost_of_scoring_per_person) * n_test_given

    # Computing the fifth component of the replacement cost.
    R5 = (meeting_time * (hr_pay_rate + dept_representative_pay_rate)) * n_meetings

    # Computing the sixth component of the replacement cost.
    R6 = acquiring_and_disseminating_time * avg_hr_pay_rate * n_turnover_replace

    # Computing the replacement cost.
    total_replacement_cost = R1 + R2 + R3 + R4 + R5 + R6

    return total_replacement_cost

def training_cost(informational_package_cost : float,
                  n_replacements : float,
                  training_program_length : float,
                  avg_trainers_pay_rate : float,
                  n_programs : float,
                  training_cost_atributed_to_replacement_proportion : float,
                  avg_trainee_pay_rate : float,
                  n_replacement_trained_during_period : float,
                  n_instruction_hours : float,
                  avg_experienced_employees_pay_rate : float,
                  proportional_productivity_reduction : float,
                  n_experienced_employees_assigned : float,
                  new_employees_pay_rate : float,
                  n_instructions : float):
    '''
        This function computes the company's training cost.
    :param informational_package_cost: float
        The cost of informational package.
    :param n_replacements: float
        The number of replacement during period.
    :param training_program_length: float
        The length of training program.
    :param avg_trainers_pay_rate: float
        The average pay rate of trainers.
    :param n_programs: float
        The number of programs conducted.
    :param training_cost_atributed_to_replacement_proportion: float
        The proportion of training costs atributed to replacements.
    :param avg_trainee_pay_rate: float
        The average pay rate per trainee.
    :param n_replacement_trained_during_period: float
        The total number of replacements trained during period.
    :param n_instruction_hours: float
        The number of hours required for instruction.
    :param avg_experienced_employees_pay_rate: float
        The average pay rate of experienced employees.
    :param proportional_productivity_reduction: float
        The proportional reduction in productivity due to training.
    :param n_experienced_employees_assigned: float
        The number of experienced employees assigned to the job training.
    :param new_employees_pay_rate: float
        The new employees pay rate.
    :param n_instructions: float
        The number of instructions during period.
    :return: float
        The total cost of training.
    '''
    # Computing the first component of the Training Cost.
    T1 = informational_package_cost * n_replacements

    # Computing the second component of the Training Cost.
    T2 = training_program_length * avg_trainers_pay_rate * n_programs * training_cost_atributed_to_replacement_proportion
    T2 += avg_trainee_pay_rate * n_replacement_trained_during_period * training_program_length

    # Computing the third component of the Training Cost.
    T3 = avg_experienced_employees_pay_rate * proportional_productivity_reduction * n_experienced_employees_assigned
    T3 += new_employees_pay_rate * n_instructions
    T3 *= n_instruction_hours

    # Computing the total Training Cost.
    total_training_cost = T1 + T2 + T3

    return total_training_cost

def separation_cost(time_required_for_interview : float,
                    weighted_pay_for_terminated_employees : float,
                    n_turnover : float,
                    admin_function_hr_time : float,
                    avg_hr_wage : float,
                    separation_pay_per_employee : float,
                    n_employees_earning_at_least_7000 : float,
                    avg_wage_under_7000 : float,
                    n_employees_earning_under_7000 : float,
                    unemployment_tax_rate : float = 0.6,
                    base_rate : float = 0.54):
    '''
        This function computes the company's separation cost.
    :param time_required_for_interview: float
        The time required for the interview.
    :param weighted_pay_for_terminated_employees: float
        The weighted pay for terminated employees.
    :param n_turnover: float
        The number of turnover during period.
    :param admin_function_hr_time: float
        The time required by the HR department for administrative functions related to termination.
    :param avg_hr_wage: float
        The average HR department employees pay.
    :param separation_pay_per_employee: float
        The amount of separation pay per employee terminated.
    :param n_employees_earning_at_least_7000: float
        The number of employees earning at least 7000.
    :param avg_wage_under_7000: float
        The average of employees wage of the ones earning under 7000.
    :param n_employees_earning_under_7000: float
        The number of employees earning under 7000.
    :param unemployment_tax_rate: float, default = 0.6
        The un-employment tax rate.
    :param base_rate: float, default = 0.54
        The base rate.
    :return: float
        The total separation cost.
    '''
    # Computing the first component of separation cost.
    S1 = time_required_for_interview * weighted_pay_for_terminated_employees * n_turnover

    # Computing the second component of separation cost.
    S2 = admin_function_hr_time * avg_hr_wage * n_turnover

    # Computing the third component of separation cost.
    S3 = separation_pay_per_employee * n_turnover

    # Computing the fourth component of separation cost.
    S4 = (unemployment_tax_rate - base_rate)
    S4 *= ((7000 * n_employees_earning_at_least_7000) + avg_wage_under_7000 * n_employees_earning_under_7000)
    S4 += unemployment_tax_rate * (7000 * n_turnover)

    # Computing the total separation cost.
    total_separation_cost = S1 + S2 + S3 + S4

    return total_separation_cost

 


 