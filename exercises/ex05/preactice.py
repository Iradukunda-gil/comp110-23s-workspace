from __future__ import annotations
class Phone:
    number: str
    name: str
    contacts: list[Phone]
    
    def __init__(self, number: str, name: str):
        self.number = number
        self.name = name
        self.contacts = []
    
    def add_contacts(self, other: Phone) -> None:
        if not(other in self.contacts):
            self.contacts.append(other)
    
    def add_contacts_friends(self, other: Phone) -> None:
        if other in self.contacts:
            print("Now that's quite a circle you're building")
            for contact in other.contacts:
                if not (contact in self.contacts):
                    self.contacts.append(contact)
                else:
                    print(f"Gotta find a way, {self.name}")
    
def main():
    main_character: Phone = Phone("9191995", "Joh")
    new_friend: Phone = Phone("919", "Jame")
    tv_ad: Phone = Phone("877CHAS", "went")
    new_friend.add_contacts(tv_ad)
    main_character.add_contacts(new_friend)
    main_character.add_contacts_friends(new_friend)
    main_character.add_contacts(new_friend)
    main_character.add_contacts_friends(new_friend)

if __name__ == "__main__":
    main()
