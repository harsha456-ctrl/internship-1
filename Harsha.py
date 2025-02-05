import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Lazy", "Charming", "Fierce", "Bright"]
nouns = ["Tiger", "Dragon", "Panther", "Eagle", "Shark", "Wizard", "Phoenix"]

def generate_username(include_numbers, include_special, length=None):
    # Combine a random adjective and noun
    username = random.choice(adjectives) + random.choice(nouns)
    
    # Optionally add numbers or special characters
    if include_numbers:
        username += str(random.randint(0, 999))
    if include_special:
        username += random.choice(string.punctuation)
    
    # Adjust username length if specified
    if length and length > len(username):
        extra_length = length - len(username)
        username += ''.join(random.choices(string.ascii_letters + string.digits, k=extra_length))
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")

def main():
    print("Welcome to the Random Username Generator!")
    
    usernames = []
    while True:
        try:
            # User preferences
            include_numbers = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
            include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            length = input("Specify username length (optional, press Enter to skip): ").strip()
            length = int(length) if length.isdigit() else None
            
            # Generate username
            username = generate_username(include_numbers, include_special, length)
            print(f"Generated Username: {username}")
            usernames.append(username)
            
            # Save option
            save_option = input("Would you like to save this username? (yes/no): ").strip().lower()
            if save_option == "yes":
                save_usernames_to_file(usernames)
                print(f"Usernames saved to 'usernames.txt'")
            
            # Continue or exit
            another = input("Generate another username? (yes/no): ").strip().lower()
            if another != "yes":
                break
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print("Thank you for using the Random Username Generator!")

if __name__ == "__main__":
    main()