# pfai_core.py
# Prototype logic for Personality-Focused Future-Aware AI (PFAI)

def generate_personality(birthdate):
    from hashlib import sha256
    hash_val = sha256(birthdate.encode()).hexdigest()
    return {
        "introversion": int(hash_val[0:2], 16) / 255,
        "empathy": int(hash_val[2:4], 16) / 255,
        "risk_tolerance": int(hash_val[4:6], 16) / 255,
        "expressiveness": int(hash_val[6:8], 16) / 255,
    }

def forecast_tomorrow():
    return {"luck": 0.76, "focus": "communication"}

def suggest_behavior(personality, forecast):
    if forecast["focus"] == "communication":
        if personality["empathy"] > 0.7:
            return "Try connecting with someone dear to you tomorrow."
        else:
            return "Prepare in advance for important conversations tomorrow."
    return "Follow your instincts, and you'll be fine."

# Sample use
if __name__ == "__main__":
    bdate = "1992-07-15"
    p = generate_personality(bdate)
    f = forecast_tomorrow()
    print(suggest_behavior(p, f))
