from collections import ChainMap


class UserProfile:
    def __init__(self, display_name: str):
        self.display_name = display_name

    def __getitem__(self, item: str):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)


class UserAccount:
    def __init__(self, iban: str, balance: int):
        self.iban = iban
        self.balance = balance

    def __getitem__(self, item: str):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)


if __name__ == "__main__":
    user_profile = UserProfile("John Doe")
    user_account = UserAccount("GB71BARC20031885581746", 3000)
    user = ChainMap(user_profile, user_account)
    print(f"name:    {user['display_name']}")
    print(f"iban:    {user['iban']}")
    print(f"balance: {user['balance']}")
