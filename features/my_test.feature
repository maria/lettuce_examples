Feature: Compute factorial
    In order to learn lettuce
    As a developer
    I'll implement factorial

    Scenario Outline: Factorials for numbers 0-4
        Given I have the number <number>
        When I compute his factorial
        Then I get the number <factorial>

    Examples:
            | number | factorial |
            |0       | 1         |
            |1       | 1         |
            |2       | 2         |

