import datetime as dt


'''  Main сalculator'''
class Calculator:
    def __init__(self, limit):
    '''Creates a parent class calculator.'''
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        date_now = dt.date.today()
        return sum(
            i.amount
            for i in self.records
            if i.date == date_now
        )

    def get_week_stats(self):
        date_now = dt.date.today()
        laft_week = date_now - dt.timedelta(days=7)
        return sum(
            i.amount
            for i in self.records
            if laft_week <= i.date <= date_now
        )

    def get_today_remained(self):
        return self.limit - self.get_today_stats()


''' Records'''
class Record:
    def __init__(self, amount, comment, date=None):
        '''Creates a class with records.'''
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


''' Calculator for сash'''
class CashCalculator(Calculator):

    EURO_RATE = 77.0
    USD_RATE = 68.6
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        '''Creates a class that counts cash inherited from the main class Calculator.'''
        cash_remained = self.get_today_remained()

        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),            
        }
        currency_name, currency_rate = currencies[currency]        

        today_remained_in_currency = round(cash_remained / currency_rate, 2)

        if not cash_remained:
            return f'Денег нет, держись'
        if today_remained_in_currency > 0:
            return f'На сегодня осталось {today_remained_in_currency} {currency_name}'
        return ('Денег нет, держись: '
               f'твой долг - {abs(today_remained_in_currency)} {currency_name}')


''' Calculator for сalories'''
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        '''Creates a class that counts calories inherited from the main class Calculator.'''
        calories_remained = self.get_today_remained()
        if calories_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {calories_remained} кКал')
        return 'Хватит есть!'


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др",
                                     date="08.11.2019"))