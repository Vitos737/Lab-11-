class Customer:
  _id_counter = 1

  def __init__(self, surname, first_name, patronymic, address, credit_card_number, bank_account_number):
      self._id = Customer._id_counter
      self.surname = surname
      self.first_name = first_name
      self.patronymic = patronymic
      self.address = address
      self.credit_card_number = credit_card_number
      self.bank_account_number = bank_account_number
      Customer._id_counter += 1

  @property
  def id(self):
      return self._id

  @property
  def full_name(self):
      return f"{self.surname} {self.first_name} {self.patronymic}"

  @full_name.setter
  def full_name(self, value):
      names = value.split(' ')
      self.surname, self.first_name, self.patronymic = names

  def __str__(self):
      return f"Customer ID: {self.id}, Name: {self.full_name}, Address: {self.address}, " \
             f"Credit Card: {self.credit_card_number}, Bank Account: {self.bank_account_number}"

class CustomerCollection:
  def __init__(self):
      self.customers = []

  def add_customer(self, customer):
      self.customers.append(customer)

  def get_customer_by_credit_card(self, credit_card_number):
      return next((customer for customer in self.customers if customer.credit_card_number == credit_card_number), None)

# Приклад створення об'єктів та використання класу
collection = CustomerCollection()
collection.add_customer(Customer("Іваненко", "Іван", "Іванович", "вул. Центральна, 1", "1234567890123456", "UA12345678901234567890123456"))
collection.add_customer(Customer("Петренко", "Петро", "Петрович", "вул. Головна, 2", "6543210987654321", "UA65432109876543210987654321"))

# Пошук клієнта за номером кредитної картки
customer = collection.get_customer_by_credit_card("1234567890123456")
print(customer)