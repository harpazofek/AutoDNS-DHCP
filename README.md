# AutoDNS-DHCP
1. main.py (Your main program)
2. logging_config.py (Logging configuration)
3. group_name_resolver.py (GroupNameResolver class)
4. dns_group.py (DNSGroup class)
5. name_to_ip_mapper.py (NameToIPMapper class)
6. dhcp_server.py (DHCP server configuration and MyDhcpApp class)

Tests:
To run the tests for all the modules, navigate to the root directory of your project in the terminal and execute the following command:
'python -m unittest discover tests'

7. tests/test_name_to_ip_mapper.py (Test cases for the NameToIPMapper class)
8. tests/test_group_name_resolver.py
9. tests/test_dns_group.py
10. tests/test_dhcp_server.py

Testing the main.py module can be a bit different from testing other modules, as it usually involves running the entire application and checking its behavior. However, you can still write tests for the components of the main.py module.

Here's how you might approach testing the main.py module:

Isolate Testable Components: First, you should identify the different parts of your main.py module that can be isolated and tested separately. These could be individual functions, classes, or methods.

Use Dependency Injection: If your main module heavily relies on external services or components (like the classes you've mentioned), consider using dependency injection to inject mock or test versions of those components during testing.

Focus on Functionality: Since the main.py module likely orchestrates the interactions between various components, focus on testing its primary functionality. This could involve simulating different scenarios and checking if the expected behavior occurs.

Mocking External Services: If your main.py interacts with external services or resources (e.g., network services, databases), you should mock these services during testing to isolate the behavior of your code.



