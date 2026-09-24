# TC-004: Invalid Email Address

## Test Objective

Check what happens when a user enters an invalid email address.

## Preconditions

* The DoseAlert website is open.
* The user is on the homepage.

## Test Steps

1. Enter a name.
2. Enter a medication name.
3. Enter an invalid email address.
4. Choose a reminder time.
5. Click the Save Reminder button.

## Test Data

Name: Test User
Medication: Panado
Email: test-email
Time: 10:00

## Expected Result

The reminder should not be saved and the user should be asked to enter a valid email address.

## Priority

Medium

## Status

Not Run
