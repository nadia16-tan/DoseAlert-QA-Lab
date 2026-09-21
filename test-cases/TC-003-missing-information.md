# TC-003: Save reminder with missing information

## Test Objective
Check what happens when the user does not fill in all the required fields.

## Preconditions
- The DoseAlert website is open.
- The user is on the homepage.

## Test Steps
1. Enter a name.
2. Leave the medication name empty.
3. Enter an email address.
4. Choose a reminder time.
5. Click the Save Reminder button.

## Test Data
Name: Test User  
Medication: Leave empty  
Email: test@example.com  
Time: 10:00

## Expected Result
The reminder should not be saved and the user should be asked to enter the missing medication name.

## Priority
High

## Status
Not Run