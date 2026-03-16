import datetime

def get_zodiac_sign(day, month):
    # Mapping dates to Zodiac signs
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

def get_zodiac_details(sign):
    # Dictionary containing "A to Z" details for each sign
    details = {
        "Aries": {"Element": "Fire", "Trait": "Brave & Energetic", "Planet": "Mars", "Lucky Color": "Red"},
        "Taurus": {"Element": "Earth", "Trait": "Reliable & Patient", "Planet": "Venus", "Lucky Color": "Green"},
        "Gemini": {"Element": "Air", "Trait": "Curious & Adaptable", "Planet": "Mercury", "Lucky Color": "Yellow"},
        "Cancer": {"Element": "Water", "Trait": "Intuitive & Protective", "Planet": "Moon", "Lucky Color": "White"},
        "Leo": {"Element": "Fire", "Trait": "Confident & Generous", "Planet": "Sun", "Lucky Color": "Gold"},
        "Virgo": {"Element": "Earth", "Trait": "Analytical & Loyal", "Planet": "Mercury", "Lucky Color": "Grey"},
        "Libra": {"Element": "Air", "Trait": "Diplomatic & Artistic", "Planet": "Venus", "Lucky Color": "Pink"},
        "Scorpio": {"Element": "Water", "Trait": "Passionate & Resourceful", "Planet": "Pluto", "Lucky Color": "Black"},
        "Sagittarius": {"Element": "Fire", "Trait": "Optimistic & Funny", "Planet": "Jupiter", "Lucky Color": "Purple"},
        "Capricorn": {"Element": "Earth", "Trait": "Disciplined & Practical", "Planet": "Saturn", "Lucky Color": "Brown"},
        "Aquarius": {"Element": "Air", "Trait": "Original & Independent", "Planet": "Uranus", "Lucky Color": "Blue"},
        "Pisces": {"Element": "Water", "Trait": "Compassionate & Wise", "Planet": "Neptune", "Lucky Color": "Sea Green"},
    }
    return details.get(sign)

def main():
    print("--- Zodiac Discovery System ---")
    try:
        dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d")
        
        sign = get_zodiac_sign(dob.day, dob.month)
        info = get_zodiac_details(sign)
        
        print(f"\n--- Results for {sign} ---")
        for key, value in info.items():
            print(f"**{key}:** {value}")
            
    except ValueError:
        print("Invalid format! Please use YYYY-MM-DD (e.g., 1995-05-20).")

if __name__ == "__main__":
    main()