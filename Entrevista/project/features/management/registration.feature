Feature: Registration

  @SVT
  Scenario Outline: Create an User with full information
    Given I navigate to website
    When I click on sign-in
    And I click on Register using <email>
    And I filed my personal information <name> <last_name> <password> <email> for <gender>
    And I filed my address information <company> <address> <city> <state> <cp> <country> <home_phone> <mobile_phone> <future_address> <address_2> <comment>
    Then I able to register my profile successfully

    Examples:
      | email                | name      | last_name | password     | gender | company   | address      | city         | state    | cp      | country         | home_phone | mobile_phone | future_address | address_2 | comment   |
      | "horaciosi@gmail.com" | "horacio" | "tovo"    | "horacio123" | "Mr"   | "addidas" | "avellaneda" | "carlos paz" | "Kansas" | "50000" | "United States" | "454425"   | "15641452"   | "colon"        | "lua"     | "bla bla" |

  @SVT
  Scenario Outline: Create an User only with required information
    Given I navigate to website
    When I click on sign-in
    And I click on Register using <email>
    And I filed my personal information <name> <last_name> <password> <email> for <gender>
    And I filed my address information <company> <address> <city> <state> <cp> <country> <home_phone> <mobile_phone> <future_address> <address_2> <comment>
    Then I able to register my profile successfully

    Examples:
      | email               | name      | last_name | password     | gender | company | address      | city         | state    | cp      | country         | home_phone | mobile_phone | future_address | address_2 | comment |
      | "horaciao@gmail.com" | "horacio" | "tovo"    | "horacio123" | "Mr"   | "NO"    | "avellaneda" | "carlos paz" | "Kansas" | "50000" | "United States" | "NO"       | "15641452"   | "colon"        | "NO"      | "NO"    |

