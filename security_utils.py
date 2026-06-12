# app/services/snow_service.py

def calculate_snow_melt(snow_fall, temperature):
    if temperature > 0:
        return snow_fall * 0.1 * temperature
    return 0