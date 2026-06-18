"""
Goals and Progress Tracking system for EcoAgent AI
"""
import json
from datetime import datetime
from pathlib import Path

class GoalsManager:
    """Manages user sustainability goals and progress tracking"""
    
    GOALS_FILE = "data/user_goals.json"
    
    @classmethod
    def _ensure_data_dir(cls):
        """Ensure data directory exists"""
        Path("data").mkdir(exist_ok=True)
    
    @classmethod
    def _load_goals(cls):
        """Load goals from file"""
        cls._ensure_data_dir()
        if Path(cls.GOALS_FILE).exists():
            with open(cls.GOALS_FILE, 'r') as f:
                return json.load(f)
        return {
            "monthly_target": 100,  # kg CO2e
            "annual_target": 1200,  # kg CO2e
            "goals": [],
            "history": []
        }
    
    @classmethod
    def _save_goals(cls, goals):
        """Save goals to file"""
        cls._ensure_data_dir()
        with open(cls.GOALS_FILE, 'w') as f:
            json.dump(goals, f, indent=2)
    
    @classmethod
    def set_monthly_target(cls, target_kg):
        """Set monthly carbon target"""
        goals = cls._load_goals()
        goals["monthly_target"] = target_kg
        cls._save_goals(goals)
    
    @classmethod
    def set_annual_target(cls, target_kg):
        """Set annual carbon target"""
        goals = cls._load_goals()
        goals["annual_target"] = target_kg
        cls._save_goals(goals)
    
    @classmethod
    def add_goal(cls, title, target_reduction_percent, deadline):
        """Add a new sustainability goal"""
        goals = cls._load_goals()
        goal = {
            "id": len(goals["goals"]) + 1,
            "title": title,
            "target_reduction": target_reduction_percent,
            "deadline": deadline,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }
        goals["goals"].append(goal)
        cls._save_goals(goals)
        return goal
    
    @classmethod
    def log_monthly_data(cls, month, footprint_kg, notes=""):
        """Log monthly footprint data"""
        goals = cls._load_goals()
        entry = {
            "month": month,
            "footprint": footprint_kg,
            "notes": notes,
            "date": datetime.now().isoformat()
        }
        goals["history"].append(entry)
        cls._save_goals(goals)
    
    @classmethod
    def get_progress(cls, baseline_footprint):
        """Calculate progress towards goals"""
        goals = cls._load_goals()
        history = goals["history"]
        
        if not history:
            return {"reduction_percent": 0, "months_tracked": 0, "trend": "neutral"}
        
        latest = history[-1]["footprint"]
        reduction = ((baseline_footprint - latest) / baseline_footprint * 100) if baseline_footprint > 0 else 0
        
        return {
            "reduction_percent": round(reduction, 2),
            "months_tracked": len(history),
            "current_footprint": latest,
            "baseline_footprint": baseline_footprint,
            "trend": "positive" if reduction > 0 else "negative"
        }
    
    @classmethod
    def get_all_goals(cls):
        """Get all user goals"""
        goals = cls._load_goals()
        return goals


class EcoTipsProvider:
    """Provides personalized eco-tips based on usage patterns"""
    
    TIPS_DATABASE = [
        {
            "category": "electricity",
            "tip": "💡 Switch to LED bulbs to reduce electricity consumption by up to 75%",
            "impact": "High"
        },
        {
            "category": "electricity",
            "tip": "🔌 Unplug devices when not in use to reduce phantom power consumption",
            "impact": "Medium"
        },
        {
            "category": "water",
            "tip": "🚿 Install a low-flow showerhead to save 2700+ gallons per year",
            "impact": "High"
        },
        {
            "category": "water",
            "tip": "💧 Fix leaky faucets - one dripping tap can waste 3,000 gallons annually",
            "impact": "High"
        },
        {
            "category": "travel",
            "tip": "🚴 Try biking for short trips instead of driving - save 4.6 metric tons annually",
            "impact": "High"
        },
        {
            "category": "travel",
            "tip": "🚌 Use public transport to reduce carbon emissions by 45% compared to driving",
            "impact": "High"
        },
        {
            "category": "general",
            "tip": "♻️ Buy products with minimal packaging to reduce waste",
            "impact": "Medium"
        },
        {
            "category": "general",
            "tip": "🌱 Plant trees - one tree absorbs ~48 lbs of CO2 per year",
            "impact": "Medium"
        },
        {
            "category": "electricity",
            "tip": "❄️ Set thermostat 2°C lower in winter to save 7% on heating",
            "impact": "High"
        },
        {
            "category": "general",
            "tip": "🛒 Buy local and seasonal produce to reduce transport emissions",
            "impact": "Medium"
        },
    ]
    
    @classmethod
    def get_tips_for_category(cls, category, limit=3):
        """Get tips for a specific usage category"""
        tips = [t for t in cls.TIPS_DATABASE if t["category"] == category]
        return tips[:limit]
    
    @classmethod
    def get_personalized_tips(cls, footprint_breakdown):
        """Get tips based on user's highest emission categories"""
        sorted_categories = sorted(
            footprint_breakdown.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        recommendations = []
        for category, value in sorted_categories[:2]:
            category_key = category.lower().replace(" ", "_")
            tips = cls.get_tips_for_category(category_key, limit=2)
            recommendations.extend(tips)
        
        # Add general tips
        general_tips = cls.get_tips_for_category("general", limit=1)
        recommendations.extend(general_tips)
        
        return recommendations[:5]
    
    @classmethod
    def get_random_tips(cls, limit=5):
        """Get random eco-tips"""
        import random
        return random.sample(cls.TIPS_DATABASE, min(limit, len(cls.TIPS_DATABASE)))


class AchievementBadges:
    """Badge/achievement system for user milestones"""
    
    BADGES = {
        "first_step": {
            "name": "First Step",
            "description": "Created your first carbon footprint profile",
            "icon": "🌱"
        },
        "eco_champion": {
            "name": "Eco Champion",
            "description": "Achieved 50% reduction in carbon footprint",
            "icon": "🏆"
        },
        "sustainable_month": {
            "name": "Sustainable Month",
            "description": "Stayed below monthly target for a full month",
            "icon": "📈"
        },
        "water_saver": {
            "name": "Water Saver",
            "description": "Reduced water consumption by 30%",
            "icon": "💧"
        },
        "energy_efficient": {
            "name": "Energy Efficient",
            "description": "Reduced electricity consumption by 30%",
            "icon": "⚡"
        },
        "green_commuter": {
            "name": "Green Commuter",
            "description": "Switched to sustainable transport for 10+ trips",
            "icon": "🚴"
        },
        "carbon_neutral": {
            "name": "Carbon Neutral",
            "description": "Achieved monthly footprint at or below 100 kg CO2e",
            "icon": "🌍"
        }
    }
    
    @classmethod
    def check_achievements(cls, user_data):
        """Check which achievements user has unlocked"""
        earned_badges = []
        
        # Handle None or missing footprint
        footprint_data = user_data.get('footprint')
        if not footprint_data:
            return earned_badges
        
        if isinstance(footprint_data, dict):
            earned_badges.append("first_step")
        
        total_footprint = footprint_data.get('total', 0) if isinstance(footprint_data, dict) else footprint_data
        progress = GoalsManager.get_progress(total_footprint)
        if progress.get('reduction_percent', 0) >= 50:
            earned_badges.append("eco_champion")
        
        return earned_badges
