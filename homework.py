import datetime as dt


'''  Main сalculator


Creates a parent class calculator.
'''
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        count_today = sum(
            i.amount
            for i in self.records
            if i.date == dt.date.today()
        )
        return count_today

    def get_week_stats(self):
        laft_week = dt.date.today() - dt.timedelta(days=7)
        count_week = sum(
            i.amount
            for i in self.records
            if laft_week <= i.date <= dt.date.today()
        )
        return count_week


''' Records


Creates a class with records.
'''
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if not date:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def __str__(self):
        return f'{self.amount} , {self.comment} , {self.date}'

    def __repr__(self):
        return f'("{self.amount}"), ("{self.comment}"), ("{self.date}")'


''' Calculator for сash


Creates a class that counts cash inherited from the main class Calculator.
'''
class CashCalculator(Calculator):

    EURO_RATE = 77.0
    USD_RATE = 68.6
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()

        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),            
        }
        currency_name, currency_rate = currencies[currency]        

        today_remained_in_currency = round(cash_remained / currency_rate, 2)

        if today_remained_in_currency > 0:
            return f'На сегодня осталось {today_remained_in_currency} {currency_name}'
        elif cash_remained == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {abs(today_remained_in_currency)} {currency_name}'


''' Calculator for сalories
    

Creates a class that counts calories inherited from the main class Calculator.
'''
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if self.get_today_stats() <= self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'


if __name__ == '__main__':
    pass