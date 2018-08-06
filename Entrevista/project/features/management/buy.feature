Feature: Purchasing Process

  @SVT
  Scenario Outline: Create an User with full information
    Given I navigate to website
    When I click on sign-in
    And I able to login with the followings credentials <email> and <password>
    And I search for <topic> and select the first item
    Then I buy my item


    Examples:
      | email                | password     | topic   |
      | "horacios@gmail.com" | "horacio123" | "short" |
