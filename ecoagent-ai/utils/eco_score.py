class EcoScoreEngine:
    """
    Generates a sustainability score (0-100) and grade (A-D) 
    based on carbon footprint compared to sustainable targets.
    """
    
    # Yearly target for a sustainable lifestyle is approx 2000kg CO2 per person.
    # Monthly target = 2000 / 12 = ~166kg CO2.
    MONTHLY_TARGET = 166.0 

    @staticmethod
    def calculate_score(total_footprint: float) -> dict:
        """
        Score = 100 - (Footprint / Target * 50) 
        capped at 0 and 100.
        If footprint is exactly target, score is 50.
        """
        if total_footprint == 0:
            return {'score': 100, 'grade': 'A+', 'label': 'Pristine'}
            
        ratio = total_footprint / EcoScoreEngine.MONTHLY_TARGET
        score = max(0, min(100, 100 - (ratio * 30))) # More lenient scoring
        
        if score >= 85:
            grade = 'A'
            label = 'Eco Warrior'
        elif score >= 70:
            grade = 'B'
            label = 'Sustainable'
        elif score >= 50:
            grade = 'C'
            label = 'Needs Improvement'
        else:
            grade = 'D'
            label = 'High Impact'
            
        return {
            'score': round(score, 1),
            'grade': grade,
            'label': label
        }
