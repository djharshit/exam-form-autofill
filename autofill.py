#!/usr/bin/env python

"""
Form Autofill - degree.rgpvexam.in Basic Details autofill by python selenium

"""

# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import random

# List of options
l = [0, 1, 2, 3, 4]

# Creating a webdriver instance
driver = webdriver.Chrome()

# Maximise the window
driver.maximize_window()

# Window 1 - Opening the login page
driver.get('https://degree.rgpvexam.in/#/login')

# Waiting for the page to load
time.sleep(3)

# Entering the username
driver.find_element(by=By.NAME, value='enrollment_number').send_keys('0201CS201031')

# Entering the password
driver.find_element(by=By.NAME, value='password').send_keys('2sPBj.uz4D*MF//') # 'Omnamashivay@1')

# Click login button
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

# Load the next window
time.sleep(3)

# Window 2 - Filling questionaie
select_ques = [
    'How_much_of_the_syllabus_was_covered_in_the_class',
    'How_well_did_the_teachers_prepare_for_the_classes',
    'The_teachers_approach_to_teaching_can_best_be_described_as',
    'Fairness_of_the_internal_evaluation_process_by_the_teachers',
    'Was_your_performance_in_assignments_discussed_with_you',
    'The_institute_takes_active_interest_in_promoting_internship__student_exchange__field_visit_opportunities_for_students',
    'The_teaching_and_mentoring_process_in_your_institution_facilitates_you_in_cognitive__social_and_emotional_growth',
    'The_institution_provides_multiple_opportunities_to_learn_and_grow',
    'Teachers_inform_you_about_your_expected_competencies__course_outcomes_and_programme_outcomes',
    'Your_mentor_does_a_necessary_follow_up_with_an_assigned_task_to_you',
    'The_teachers_illustrate_the_concepts_through_examples_and_applications',
    'The_teachers_identify_your_strengths_and_encourage_you_with_providing_right_level_of_challenges',
    'Teachers_are_able_to_identify_your_weaknesses_and_help_you_to_overcome_them',
    'The_institution_makes_effort_to_engage_students_in_the_monitoring__review_and_continuous_quality_improvement_of_the_teaching_learning_process',
    'The_institute_or_teachers_use_student_centric_methods__such_as_experiential_learning__participative_learning_and_problem_solving_methodologies_for_enhancing_learning_experiences',
    'Teachers_encourage_you_to_participate_in_extracurricular_activities',
    'Efforts_are_made_by_the_institute_or_teachers_to_inculcate_soft_skills__life_skills_and_employability_skills_to_make_you_ready_for_the_world_of_work',
    'What_percentage_of_teachers_use_ICT_tools_such_as_LCD_projector__Multimedia__etc_while_teaching',
    'The_overall_quality_of_teaching_learning_process_in_your_institute_is_very_good'
]

fill_ques = {
    'Name_of_Student': 'Harshit Mehra',
    'State_of_Domicile': 'Madhya Pradesh',
    'Nationality_if_other_than_Indian': 'Indian',
    'Year_of_Joining': '2020',
}

# Part 1
for key, value in fill_ques.items():
    driver.find_element(by=By.ID, value=key).send_keys(value)

Select(driver.find_element(by=By.ID, value='Please_confirm_this_is_the_first_and_only_time_you_answer_this_survey')).select_by_visible_text('Yes')
Select(driver.find_element(by=By.ID, value='What_degree_program_are_you_pursuing_now')).select_by_visible_text("Bachelor's")
Select(driver.find_element(by=By.ID, value='Category')).select_by_visible_text('SC')

# Part 2
for i in select_ques:
    Select(driver.find_element(by=By.ID, value=i)).select_by_index(random.choice(l))

key = 'Give_three_observation_or_suggestions_to_improve_the_overall_teaching___learning_experience_in_your_institution'
value = 'More use of technology, More doubt sessions, Punctual teachers'
driver.find_element(by=By.ID, value=key).send_keys(value)

# Click the submit button
driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
