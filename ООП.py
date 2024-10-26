from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, brand, model, color, storage_capacity, battery_life):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage_capacity = storage_capacity
        self.battery_life = battery_life

    @abstractmethod
    def make_call(self, phone_number):
        pass

    @abstractmethod
    def send_message(self, phone_number, message):
        pass

    @abstractmethod
    def browse_internet(self):
        pass


class IPhone(Phone):
    def make_call(self, phone_number):
        return f"Calling {phone_number} on {self.__class__.__name__}."

    def send_message(self, phone_number, message):
        return f"Sending message '{message}' to {phone_number} from {self.__class__.__name__}"

    def browse_internet(self):
        return f"Browsing the internet on {self.__class__.__name__}"


class Android(Phone):
    def make_call(self, phone_number):
        return f"Calling {phone_number} on {self.__class__.__name__}."

    def send_message(self, phone_number, message):
        return f"Sending message '{message}' to {phone_number} from {self.__class__.__name__}"

    def browse_internet(self):
        return f"Browsing the internet on {self.__class__.__name__}"


class IPhone15(IPhone):
    def __init__(self, brand, model, color, storage_capacity, battery_life, camera_quality, serial_number=None):
        super().__init__(brand, model, color, storage_capacity, battery_life)
        self.camera_quality = camera_quality
        self.serial_number = serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_serial_number(self):
        return self.serial_number

    def take_photo(self):
        return f"Taking a photo with {self.__class__.__name__}."


class IPhone4(IPhone):
    def make_call(self, phone_number):
        return f"Calling {phone_number} on {self.__class__.__name__}."

    def send_message(self, phone_number, message):
        return f"Sending message '{message}' to {phone_number} from {self.__class__.__name__}"

    def browse_internet(self):
        return f"Browsing the internet on {self.__class__.__name__}"


# объект IPhone15
iphone_15 = IPhone15(
    brand="Apple",
    model="iPhone 15",
    color="Black",
    storage_capacity="256GB",
    battery_life="20 hours",
    camera_quality="48MP"
)

# объект Android
android_phone = Android(
    brand="Samsung",
    model="Galaxy S23",
    color="Blue",
    storage_capacity="512GB",
    battery_life="24 hours"
)

# Вызов методов для iPhone15
print(iphone_15.make_call("89309197353"))
print(iphone_15.send_message("89309197353", "Hello! How are you?"))
print(iphone_15.browse_internet())
print(iphone_15.take_photo())
iphone_15.set_serial_number("A123B456C789")
print(f"Serial number of iPhone15: {iphone_15.get_serial_number()}")

# Вызов методов для Android
print(android_phone.make_call("01511635178"))
print(android_phone.send_message("01511635178", "Hey, let's meet!"))
print(android_phone.browse_internet())
