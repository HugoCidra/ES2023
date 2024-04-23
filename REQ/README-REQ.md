# REQ LIFECYCLE

## 1. CLIENT ANALYSIS

1. User Story is discussed with client.
2. Use Cases are written and aprooved.

## 2. PRE-DEV

1. Use Cases are assigned to a group.
2. Use Cases are assigned to 1 or more people.
3. First stack of tests are written and cover the DoD of the Use Case.

## 3. DEVELOPMENT

1. REQ Development phase: Work in progress ...

On this phase some aspects might / should change:

- More tests can be added to better cover the Use Case
- Small aspects of the Use Case can change

## 4. POS-DEV

1. REQ passes all their tests and it is ready to be deployed :)

--- 

# REQ INFORMATION AND STATUS

### REQ and TEST ISSUES
- Requirements and Tests are ISSUES in Gitlab (Labels REQ and TEST , respectively). 
- It is possible to check Information about an REQ on their Issue
- Test Closed = Test Passes
---
### REQ - TEST RELATION 
- REQs and TESTs Issues Linked = Exists this relation.
- **Developers** are responsible to add the Tests to their Issues
- Developers can change the state of the Test
- All Tests closed = REQ is OK
- At least one Test is not closed = REQ is NOK
---
### REQ AND DEV ISSUES 
- **Title template:** REQX.Y_TaskDescription_DeveloperName
- **Link your DEV (personal) Issue to the REQ you are working on**
- Don't forget to add the /spent and /estimate time

--- 

## HOW TO LINK ISSUES 
1. Click on the Issue
2. On 'Linked items' click 'Add'
3. You can add the Link with #issue_id of the other Issue you want to add

---

## ISSUE TEST CHEAT-SHEET

1. Create an Issue with Title: **TESTX.Y - Test Something**
2. Input the Test description (Given, When, Then Template)
3. On 'Linked items' click 'Add'
4. You can add the Link with #issue_id of the REQ(s)