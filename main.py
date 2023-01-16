import datetime as dt

# Общие замечания:
# * Не хватает описания к классам и функциям.
# * Не хватает аннотации типов
# * Не хватает валидации на данных, получаемых от пользователя.
# * Не хватает "абзацев" между логическими блоками кода.
#   Например, когда идет проверка одного условия, а следом за ним уже другого.


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # Не самый удобочитаемый вариант инициализации поля с датой.
        # Лучше вынести вычисление отдельно.
        # Например: создать приватный метод

        # def _convert_string_to_date(date:str)->dt.datetime.date:
        #     if not date:
        #         return dt.datetime.now().date()
        #     else:
        #         dt.datetime.strptime(date, '%d.%m.%Y').date()

        #  ...

        #     self.date = self.__convert_string_to_date(date)

        self.date = (
            # Некорректный перенос строк.
            # if not является цельным логическим выражением.
            # Его не стоит так дробить
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    # Не хватает комментария docstring с описанием функции
    def add_record(self, record):
        self.records.append(record)

    # Не хватает комментария docstring с описанием функции
    def get_today_stats(self):
        today_stats = 0
        # Несоответствие PEP8. Названия переменных
        # должны быть с маленькой буквы.
        # И общий совет, не стоит называть переменные также как
        # и названия классов или импортируемых пакетов.
        # Могут возникнуть проблемы при выполнении кода
        # с разрешением зависимостей.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    # Не хватает комментария docstring с описанием функции
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # Лишние переносы строк и неправильные отступы.
            # И время можно вычислить в отдельной переменной и
            # использовать ее в условии.
            # Минус проблема, если придется его менять.
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Лучше оформить комментарий в docstring с описанием функции
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            # Несоответствие правилам оформления кода.
            # Вместо \ лучше использовать скобки.
            # Например:
            # (f'Сегодня можно съесть что-нибудь'
            #  f' ещё, но с общей калорийностью не более {x} кКал')
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            # Скобки лишние и тут не нужны
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # Не хватает комментария docstring с описанием функции

    # Согласно заданию, метод должен принимать только currency
    # Как уже говорилось выше, не стоит называть переменные одинаково
    # (USD_RATE=USD_RATE).В данном случае, если хотелось делать
    # ручную корректировку курса, лучше было бы создать отдельные методы/метод
    # на его обновление.
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Для едиообразия можно было бы создать RUB_RATE и
            # перенести коэфициент туда.
            # Не рекомендуется использовать "магические числа" в коде.

            # Скорее всего здесь подразумевалось присвоение.
            # Один из знаков = лишний
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # Несоответствие правилам оформления кода.
            # Вместо \ лучше использовать скобки.
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # Отсутствует возврат значения

    # Зачем переопределять метод, который не планируется изменять?
    def get_week_stats(self):
        super().get_week_stats()
