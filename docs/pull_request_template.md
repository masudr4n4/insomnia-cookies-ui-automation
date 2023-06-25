# Code Review Checklist
## General
* [ ] No Commented Code
* [ ] No Duplicated/Copied Code
## Test Cases
* [ ] No Hardcoded Data Points (Ex. Product Names)
* [ ] No Testing Business Logic
### Waits
* [ ] Explicit Waits Used When Possible
* [ ] Implicit Waits Used When Explicit Waits Cannot Be Used
* [ ] Sleep Timers Never Used
### Locators
* [ ] Target by ID/Class, Not Text
## Conventions
* [ ] Single Commit for PR
* [ ] Commit is Linked to a QA Task
* [ ] No Merges on the Branch (Rebase Instead)
## Bootstraping
* [ ] Data Dependencies Are Supplied by Seeders
* [ ] Python Dependencies Are Locked by Version
* [ ] External Dependencies Are Documented (Ex. Selenium, Chromium)
## Exception Handling
* [ ] Error Messages in Human Readable Format
## Testing
* [ ] Passing CI Build
