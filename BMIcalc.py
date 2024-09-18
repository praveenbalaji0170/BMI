# BMI calculator with dietary plan and water intake suggestion

def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height (m^2)
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def dietary_plan(bmi):
    # Provide dietary plan based on BMI category
    if bmi < 18.5:
        plan = "Underweight: High-calorie, nutrient-rich diet with healthy fats and proteins."
    elif 18.5 <= bmi < 24.9:
        plan = "Normal weight: Balanced diet with a mix of proteins, carbs, and healthy fats."
    elif 25 <= bmi < 29.9:
        plan = "Overweight: Low-carb, high-protein diet with fiber-rich foods."
    else:
        plan = "Obese: Focus on low-calorie, low-fat foods, rich in proteins and fiber."
    return plan

def water_intake(weight):
    # General rule: Drink 35 ml of water per kg of body weight
    water_needed = weight * 35  # in milliliters
    return round(water_needed / 1000, 2)  # Convert to liters

def weekly_schedule():
    # Schedule suggestion for each day of the week
    schedule = {
        "Monday": "Start with a balanced breakfast (eggs, fruits), light lunch, and a protein-rich dinner.",
        "Tuesday": "Oats or smoothie for breakfast, salad for lunch, and grilled chicken or fish for dinner.",
        "Wednesday": "Scrambled eggs or toast for breakfast, sandwich or wrap for lunch, and a vegetable stir-fry for dinner.",
        "Thursday": "Greek yogurt and fruits for breakfast, quinoa or brown rice for lunch, and lentils for dinner.",
        "Friday": "Whole-grain cereal for breakfast, a healthy wrap for lunch, and grilled veggies with tofu for dinner.",
        "Saturday": "Pancakes or waffles for breakfast, a balanced lunch, and a cheat meal for dinner with moderation.",
        "Sunday": "Smoothie or fruit salad for breakfast, a light lunch, and a vegetable-based dinner."
    }
    return schedule

def bmi_calculator():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    print(f"\nYour BMI is: {bmi}")

    # Provide dietary plan based on BMI
    plan = dietary_plan(bmi)
    print(f"\nDietary Plan: {plan}")

    # Suggest water intake based on weight
    water_needed = water_intake(weight)
    print(f"\nYou should drink approximately {water_needed} liters of water daily.")

    # Display weekly schedule
    print("\nHere's a suggested dietary schedule for the week:")
    schedule = weekly_schedule()
    for day, meals in schedule.items():
        print(f"{day}: {meals}")

# Run the BMI calculator
bmi_calculator()
