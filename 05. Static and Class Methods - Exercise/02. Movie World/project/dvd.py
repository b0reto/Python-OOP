import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def int2mont(self, month):
        month_str = datetime.date(1900, int(month), 1).strftime("%B")
        return month_str


    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        split_date = date.split('.')
        month = cls.int2mont(int(date[1]), date[0])

        return cls(id, name, int(date[1]), month, age_restriction)

    #     day, month, year = split_date
    #     res_date = f"{day}.{month}.{year}"
    #     return cls(id, name, res_date, age_restriction, 11)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.is_rented}"
