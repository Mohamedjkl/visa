from faker import Faker
import pyfiglet
from termcolor import colored

# إنشاء كائن Faker
fake = Faker()

# توليد نص "b14" بأسلوب ASCII Art باستخدام pyfiglet
ascii_banner = pyfiglet.figlet_format("b14")

# طباعة النص الملون
print(colored(ascii_banner, 'green'))

# طلب عدد البطاقات من المستخدم
num_cards = int(input("Enter the number fake Visa "))

# توليد وطباعة معلومات بطاقات الفيزا الوهمية
for i in range(num_cards):
    card_info = {
        "holder_name": fake.name(),
        "number": fake.credit_card_number(card_type='visa'),
        "expiration_date": fake.credit_card_expire(start='now', end='+5y', date_format='%m/%y'),
        "security_code": fake.credit_card_security_code(card_type='visa'),
        "issuer": fake.credit_card_provider(card_type='visa')
    }

    # طباعة معلومات بطاقة الائتمان الوهمية مع فواصل
    print(f"\nFake Visa Card Information {i+1}:")
    print(f"Card Holder Name: {card_info['holder_name']}")
    print("-" * 40)
    print(f"Card Number: {card_info['number']}")
    print("-" * 40)
    print(f"Expiration Date: {card_info['expiration_date']}")
    print("-" * 40)
    print(f"Security Code: {card_info['security_code']}")
    print("-" * 40)
    print(f"Card Issuer: {card_info['issuer']}")
    print("=" * 40)
