Feature: The TRMS Login Feature Works

    Scenario: User Logs in as Employee
        Given The User is on the Log In Page
        When The User types EmployeeBob in the username field
        When The User types passwerd in the password field
        When The User clicks on the login button
        Then the User should be on the Form page

    Scenario: User Logs in as Benco
        Given The User is on the Log in Page
        When The User types BencoBob in the username field
        When the User types passwerd in the password field
        When The User clicks on the login button
        Then the User should be on the Benco Page