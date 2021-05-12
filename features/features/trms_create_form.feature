Feature: Create a Form Works

    Scenario Outline: Create a Form
        Given The User is on the Create Form Page
        When The User types <date> in the date input
        When The User types <time> in the time input
        When The User types <location> in the location input
        When the User types <course_description> in the course description input
        When the User types <cost> in the cost input
        When the User types <grade> in the grade input
        When the User selects <event> in the event input
        When the User types <justification> in the justification input
        When the User clicks the submit button
        Then the User should see message form added successfully

        Examples:
            | date     | time   | location | course_description | cost | grade | event    | justification |
            | 05/01/21 | 9:00PM | Remote   | Math               | 100  | A     | Seminars | Yes           |