Feature: Streams
    In order to collect information about my business
    As a customer
    I'll add a new stream

    Background:
        Given I have an account
        And I'm at least an observer
        And I'm logged in uberVU

    Scenario: Add a stream
        Given I can add new streams:
        When I click "add new stream"
        And I fill expression
            | col1    | col2  |
            | company | ceva  |
        But I don't select "no filering options"
        And I click "save stream"
        Then I see the "stream"

    Scenario: Delete stream
        Given I see the "stream"
        When I click "delete stream"
        Then I see the "no stream"

