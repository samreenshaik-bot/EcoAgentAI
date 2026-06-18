import pandas as pd

class CarbonCalculator:
    """
    Handles carbon footprint calculations for electricity, water, and travel.
    Units:
    - Electricity: kWh
    - Water: Liters
    - Travel: km
    - Carbon Footprint: kg CO2e
    """
    
    # Emission Factors (approximated global averages)
    EMISSION_FACTORS = {
        'electricity': 0.475,  # kg CO2e per kWh
        'water': 0.0003,       # kg CO2e per liter
        'transport': {
            'car': 0.192,      # kg CO2e per km (average petrol car)
            'bus': 0.089,      # kg CO2e per km
            'train': 0.035,    # kg CO2e per km
            'bike': 0.021      # kg CO2e per km (electric/maintenance)
        }
    }

    @staticmethod
    def calculate_electricity_emissions(kwh: float) -> float:
        return kwh * CarbonCalculator.EMISSION_FACTORS['electricity']

    @staticmethod
    def calculate_water_emissions(liters: float) -> float:
        return liters * CarbonCalculator.EMISSION_FACTORS['water']

    @staticmethod
    def calculate_travel_emissions(km: float, mode: str) -> float:
        factor = CarbonCalculator.EMISSION_FACTORS['transport'].get(mode.lower(), 0.192)
        return km * factor

    @classmethod
    def calculate_total_footprint(cls, electricity_kwh, water_liters, travel_km, transport_mode):
        elec_emissions = cls.calculate_electricity_emissions(electricity_kwh)
        water_emissions = cls.calculate_water_emissions(water_liters)
        travel_emissions = cls.calculate_travel_emissions(travel_km, transport_mode)
        
        total = elec_emissions + water_emissions + travel_emissions
        
        return {
            'total': round(total, 2),
            'breakdown': {
                'Electricity': round(elec_emissions, 2),
                'Water': round(water_emissions, 2),
                'Travel': round(travel_emissions, 2)
            }
        }
