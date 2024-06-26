# Defining a class to raise when the e-mail is less or equal to 4
class NameTooShortError(Exception):
    def __init__(self):
        super().__init__("Name must be more than 4 characters")


# Defining if the email has '@'
class MustContainAtSymbolError(Exception):
    def __init__(self):
        super().__init__("Email must contain @")


# Defining if the domain matches the ones from VALID_DOMAINS
class InvalidDomainError(Exception):
    def __init__(self):
        super().__init__("Domain must be one of the following: .com, .bg, .org, .net")


MIN_CHARACTERS = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    # Check for '@' symbol
    if "@" not in email:
        raise MustContainAtSymbolError

    # Check name length
    if len(email.split("@")[0]) <= MIN_CHARACTERS:
        raise NameTooShortError

    # Check for domain validity
    domain = email.split(".")[-1]
    if f".{domain}" not in VALID_DOMAINS:
        raise InvalidDomainError

    print("Email is valid")
