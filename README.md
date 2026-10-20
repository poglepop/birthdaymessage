# birthdaymessage
PHP command line app for bootdev project

# description

Keep track of peoples birthdays, remind me and generate a message for their birthdays.

# entity model

people: collection of people [class or CSV file?]

person: ability to add, delete, edit a person

generate: create a message based on the person

send: send me the msg

# functionality

add person
del person
edit person
check for birthdays that week
generate birthday messages
send birthday messages

# arch

python
csv file to persist people

# UI
None - command line app

# API 
None

# Events
birthdayrun (check, gen, send) as a weekly windows cron job

# Cr
controlled by main

# Safety

No secrets

# Installation and Deployment

Install python3
run files - python birthday_run.py


















