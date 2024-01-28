import random
from .models import Tblguestinfo

def create_id():
    unique_number = 0
    while unique_number == 0:
        random_id = random.randint(1000, 99999999)
        duplicate_info = Tblguestinfo.objects.filter(guestinfoid=random_id).first()
        if not duplicate_info:
            unique_number = random_id
    return unique_number