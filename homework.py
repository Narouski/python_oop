import datetime as dt




'''
-----------------------
    Main Calculator
-----------------------
'''
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []


    def add_record(self, record):
        self.records.append(record)
        return self.get_today_stats()


    def get_today_stats(self):
        get_today = 0
        for i in self.records:
            if i.date == dt.datetime.now().date():
                get_today += i.amount
        return get_today

    def get_weeks_stats(self):
        count_week = 0
        for i in  self.records:
            if i.date >= dt.date.today() - dt.timedelta(days=7):
                count_week += i.amount
        return self.count_week




'''
-----------------------
        Records
-----------------------
'''
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

    def __str__(self):
        return f'{self.amount} , {self.comment} , {self.date}'




'''
---------------------------
    Calculator for Cash
---------------------------
'''
class CashCalculator(Calculator):

    EURO_RATE = 77.0
    USD_RATE = 68.6
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        remained = self.limit - self.get_today_stats()

        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),            
        }
        currency_name, currency_rate = currencies[currency]        

        today_remained_in_currency = round(remained / currency_rate, 2)

        if today_remained_in_currency > 0:
            return f'На сегодня осталось {today_remained_in_currency} {currency_name}'
        elif remained == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {today_remained_in_currency} {currency_name}'




'''
-------------------------------
    Calculator for Calories
-------------------------------
'''
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if self.get_today_stats <= self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал'
        else:
            return f'Хватит есть!'
