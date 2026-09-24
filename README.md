# DoseAlert QA Lab

This repository is for testing my DoseAlert medication reminder application.

The purpose of this project is to practise software testing and show my understanding of QA through manual testing, automated testing and bug reporting.

## Application Being Tested

DoseAlert is a medication reminder application that allows a user to:

* Enter their name
* Enter a medication
* Enter an email address
* Set a reminder time
* Save the reminder

The application uses Flask, DynamoDB, AWS Lambda, Amazon SES and EventBridge.

## Testing

The QA testing in this repository includes:

* Manual test cases
* Automated tests using Python and Pytest
* Positive testing
* Negative testing
* API/route testing
* Regression testing
* Bug reports

## Project Structure

```text
DoseAlert-QA-Lab/
│
├── tests/
│   └── test_homepage.py
│
├── test-cases/
│   ├── TC-001-homepage.md
│   ├── TC-002-save-reminder.md
│   └── TC-003-missing-information.md
│
├── bug-reports/
│   └── BUG-001-reminder-time.md
│
├── requirements.txt
└── README.md
```

## Tools Used

* Python
* Pytest
* Requests
* Git
* GitHub
* PowerShell
* AWS

## Current Testing

The first automated test checks that the DoseAlert homepage is available and returns a successful HTTP response.

More test cases and automated tests will be added as the project continues.

## Verification

WeThinkCode_ Verification Code:

**WTC-HBBCA77C**
## youtube link: https://youtu.be/mj-9JfQGM7c

## Goal

The goal of this project is to build my QA skills by testing a real application, finding problems and documenting the results.

