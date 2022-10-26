import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC

import applicants_example as applicants
# import applicants_private as applicants


def main(applicant):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get('https://dvprogram.state.gov/application.aspx')

    # MANUALLY ENTER CAPTCHA

    wait.WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (by.By.ID, "ContentPlaceHolder1_formApplicant__ctl0_txtLastName")))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl0_txtLastName').send_keys(
        applicant.get('last_name'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl0_txtFirstName').send_keys(
        applicant.get('first_name'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl0_cbxMiddleName').click()

    gender_checkbox_id = 'ContentPlaceHolder1_formApplicant__ctl1_rdoGender{}'.format(
        applicant.get('gender'))
    driver.find_element(by.By.ID, gender_checkbox_id).click()

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl2_txtMonthOfBirth').send_keys(
        applicant.get('month_of_birth'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl2_txtDayOfBirth').send_keys(
        applicant.get('day_of_birth'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl2_txtYearOfBirth').send_keys(
        applicant.get('year_of_birth'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl3_txtBirthCity').send_keys(
        applicant.get('birth_city'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl4_drpBirthCountry').send_keys(
        applicant.get('birth_country'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl7_txtAddress1').send_keys(
        applicant.get('address_street'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl7_txtCity').send_keys(
        applicant.get('address_city'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl7_txtDistrict').send_keys(
        applicant.get('address_region'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl7_txtZipCode').send_keys(
        applicant.get('address_zip'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl7_drpMailingCountry').send_keys(
        applicant.get('address_country'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl8_drpCountry').send_keys(
        applicant.get('current_country'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl9_txtPhoneNumber').send_keys(
        applicant.get('phone'))

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl10_txtEmailAddress').send_keys(
        applicant.get('email'))
    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl10_txtConfEmailAddress').send_keys(
        applicant.get('email'))

    education_id = 'ContentPlaceHolder1_formApplicant__ctl11_rblEducation_{}'.format(
        applicant.get('edu_level'))
    driver.find_element(by.By.ID, education_id).click()

    marital_id = '_ctl0_ContentPlaceHolder1_formApplicant__ctl12_rblMarried_{}'.format(
        applicant.get('marital_level'))
    driver.find_element(by.By.ID, marital_id).click()

    driver.find_element(by.By.ID,
                        'ContentPlaceHolder1_formApplicant__ctl13_txtNumChildren').send_keys(
        applicant.get('children_number'))

    # 2024 Deprecated Passport Section

    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPLastName').send_keys(
    #     applicant.get('last_name'))
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPFirstName').send_keys(
    #     applicant.get('first_name'))
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_cbxPPMiddleName').click()
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPNum').send_keys(
    #     applicant.get('passport_number'))
    #
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPExpMonth').send_keys(
    #     applicant.get('passport_exp_month'))
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPExpDay').send_keys(
    #     applicant.get('passport_exp_day'))
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_txtPPExpYear').send_keys(
    #     applicant.get('passport_exp_year'))
    # driver.find_element(by.By.ID,
    #     'ContentPlaceHolder1_formApplicant__ctl6_drPPCountry').send_keys(
    #     applicant.get('passport_country'))

    child = applicants.APPLICANTS.get(applicant.get('child'))
    if child:
        wait.WebDriverWait(driver, 6000).until(
            EC.presence_of_element_located(
                (by.By.ID,
                 "ContentPlaceHolder1_formChild01_qName_txtLastName")))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qName_txtLastName').send_keys(
            child.get('last_name'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qName_txtFirstName').send_keys(
            child.get('first_name'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qName_cbxMiddleName').click()
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qBirthDate_txtMonthOfBirth').send_keys(
            child.get('month_of_birth'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qBirthDate_txtDayOfBirth').send_keys(
            child.get('day_of_birth'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qBirthDate_txtYearOfBirth').send_keys(
            child.get('year_of_birth'))
        gender_checkbox_id = 'ContentPlaceHolder1_formChild01_qGender_rdoGender{}'.format(
            child.get('gender'))
        driver.find_element(by.By.ID, gender_checkbox_id).click()

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qBirthCity_txtBirthCity').send_keys(
            child.get('birth_city'))

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formChild01_qBirthCountry_drpBirthCountry').send_keys(
            child.get('birth_country'))

    # MANUALLY ADD PHOTO PICTURE FOR MAIN APPLICANT AND PUSH NEXT BUTTON

    spouse = applicants.APPLICANTS.get(applicant.get('spouse'))
    if spouse:
        wait.WebDriverWait(driver, 6000).until(
            EC.presence_of_element_located(
                (by.By.ID,
                 "ContentPlaceHolder1_formSpouse_qName_txtLastName")))

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qName_txtLastName').send_keys(
            spouse.get('last_name'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qName_txtFirstName').send_keys(
            spouse.get('first_name'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qName_cbxMiddleName').click()

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qBirthDate_txtMonthOfBirth').send_keys(
            spouse.get('month_of_birth'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qBirthDate_txtDayOfBirth').send_keys(
            spouse.get('day_of_birth'))
        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qBirthDate_txtYearOfBirth').send_keys(
            spouse.get('year_of_birth'))

        gender_checkbox_id = 'ContentPlaceHolder1_formSpouse_qGender_rdoGender{}'.format(
            spouse.get('gender'))
        driver.find_element(by.By.ID, gender_checkbox_id).click()

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qBirthCity_txtBirthCity').send_keys(
            spouse.get('birth_city'))

        driver.find_element(by.By.ID,
                            'ContentPlaceHolder1_formSpouse_qBirthCountry_drpBirthCountry').send_keys(
            spouse.get('birth_country'))
        # MANUALLY ADD PHOTO PICTURE FOR SPOUSE AND PUSH NEXT BUTTON

    # VERIFY ALL DATA AND CONFIRM APPLICATION
    time.sleep(1000)


if __name__ == '__main__':
    applicant = applicants.APPLICANTS.get(applicants.Applicant.IVAN_IVANOV)
    main(applicant)
