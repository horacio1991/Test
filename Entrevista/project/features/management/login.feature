Feature: Login

@SVT
Scenario Outline: Create an User with full information
  Given I navigate to website
  When I click on sign-in
  Then I able to login with the followings credentials <email> and <password>

  Examples:
    | email                | password     |
    | "horacios@gmail.com" | "horacio123" |
