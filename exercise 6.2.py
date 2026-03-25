def conert_temperature(temp, unit):
    if unit == "C":
        #Run Fahrenheit conversion
        return f"{(temp * 9/5) + 32}"
    elif unit == "F":
         #Run Celsius conversion
         return f"{(temp - 32) * 5/9}"
    else: return "the converted value"
    
    
        
