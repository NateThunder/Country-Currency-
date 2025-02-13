print("This program will show you what currency a country uses")
country = input("What country would you like to know the currency of? ").title()


match country:
    # Africa
    case "Ghana":
        print(f"{country} uses Cedi (GHS) as a currency")
    case "Nigeria":
        print(f"{country} uses Naira (NGN) as a currency")
    case "South Africa":
        print(f"{country} uses Rand (ZAR) as a currency")
    case "Egypt":
        print(f"{country} uses Egyptian Pound (EGP) as a currency")
    case "Kenya":
        print(f"{country} uses Kenyan Shilling (KES) as a currency")
    case "Morocco":
        print(f"{country} uses Dirham (MAD) as a currency")
    case "Algeria":
        print(f"{country} uses Dinar (DZD) as a currency")

    # North America
    case "United States":
        print(f"{country} uses US Dollar (USD) as a currency")
    case "Canada":
        print(f"{country} uses Canadian Dollar (CAD) as a currency")
    case "Mexico":
        print(f"{country} uses Peso (MXN) as a currency")
    
    # South America
    case "Brazil":
        print(f"{country} uses Real (BRL) as a currency")
    case "Argentina":
        print(f"{country} uses Peso (ARS) as a currency")
    case "Chile":
        print(f"{country} uses Peso (CLP) as a currency")

    # Europe
    case "United Kingdom"| "England" | "Scotland" | "Wales" | "Northern Ireland":
        print(f"{country} uses Pound Sterling (GBP) as a currency")
    case "Germany" | "France" | "Spain" | "Italy" | "Netherlands"|"Republic Of Irelans":
        print(f"{country} uses Euro (EUR) as a currency")
    case "Switzerland":
        print(f"{country} uses Swiss Franc (CHF) as a currency")
    case "Sweden":
        print(f"{country} uses Krona (SEK) as a currency")

    # Asia
    case "China":
        print(f"{country} uses Yuan (CNY) as a currency")
    case "Japan":
        print(f"{country} uses Yen (JPY) as a currency")
    case "India":
        print(f"{country} uses Rupee (INR) as a currency")
    case "South Korea":
        print(f"{country} uses Won (KRW) as a currency")
    case "Saudi Arabia":
        print(f"{country} uses Riyal (SAR) as a currency")
    case "North Korea":
        print(f"{country} uses North Korean Won (KPW) as a currency")

    # Oceania
    case "Australia":
        print(f"{country} uses Australian Dollar (AUD) as a currency")
    case "New Zealand":
        print(f"{country} uses New Zealand Dollar (NZD) as a currency")

    # Special cases
    case "Iceland":
        print(f"{country} uses Icelandic Króna (ISK) as a currency")
    case "Greenland":
        print(f"{country} uses Danish Krone (DKK) as a currency")
    case "Antarctica":
        print(f"{country} has no official currency")

    # Default case
    case _:
        print(f"{country} is not on our list buddy. Check your spelling please and thank you!")
