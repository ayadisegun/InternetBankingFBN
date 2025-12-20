from Utilities.json_loader import load_json

class TestData:

    _users = None
    _transfers = None
    _remittance = None
    _smeLoan = None

    @classmethod
    def users(cls):
        if cls._users is None:
            cls._users = load_json("users.json")
        return cls._users

    @classmethod
    def transfers(cls):
        if cls._transfers is None:
            cls._transfers = load_json("transfers.json")
        return cls._transfers

    @classmethod
    def remittance(cls):
        if cls._remittance is None:
            cls._remittance = load_json("remittance.json")
        return cls._remittance

    @classmethod
    def get_user(cls, role: str):
        users = cls.users()
        if role not in users:
            raise ValueError(f"User role '{role}' not found in users.json")
        return users[role]

    @classmethod
    def get_transfer(cls, transfer_type: str, scenario: str):
        transfers = cls.transfers()
        if transfer_type not in transfers:
            raise ValueError(f"Transfer type '{transfer_type}' not found in transfers.json")
        if scenario not in transfers[transfer_type]:
            raise ValueError(f"Scenario '{scenario}' not found under '{transfer_type}' in transfers.json")
        return transfers[transfer_type][scenario]

    @classmethod
    def get_remittance(cls, bill_type: str):
        remittance = cls.remittance()
        if bill_type not in remittance:
            raise ValueError(f"User role '{bill_type}' not found in users.json")
        return remittance[bill_type]

