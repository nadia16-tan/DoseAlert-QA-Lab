# BUG-001: Reminder can be missed at the scheduled time

## Bug Description
The medication reminder may not be sent if the Lambda function does not run at the exact same minute as the reminder time.

## Steps to Reproduce
1. Create a medication reminder.
2. Set the reminder time.
3. Wait for the reminder time.
4. Check the Lambda logs.
5. Check the email inbox.

## Expected Result
The user should receive the medication reminder around the scheduled time.

## Actual Result
The reminder can be missed when the Lambda runs a little before or after the scheduled minute.

## Severity
Medium

## Priority
High

## Environment
- AWS Lambda
- DynamoDB
- Amazon SES
- EventBridge Scheduler
- Python

## Status
Open
