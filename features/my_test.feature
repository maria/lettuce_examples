Feature: Compute factorial
    In order to learn lettuce
    As a developer
    I'll implement factorial

    @important
    Scenario Outline: Factorials for numbers 0-2
        Given I have the number <number>
        When I compute his factorial
        Then I get the number <factorial>

    Examples:
            | number | factorial |
            |0       | 1         |
            |1       | 1         |
            |2       | 2         |

    Scenario Outline: Add the number 3 with 4
        Given I have the numbers <number>, <factorial>
        When I compute addition
        Then I get the sum <sum>

    Examples:
            | number | factorial | sum  |
            |3       | 4         | 7    |
