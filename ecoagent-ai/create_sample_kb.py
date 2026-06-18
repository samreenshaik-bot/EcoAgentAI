from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_sample_kb(folder="knowledge_base"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    filepath = os.path.join(folder, "energy_saving_guide.pdf")
    c = canvas.Canvas(filepath, pagesize=letter)
    c.drawString(100, 750, "Sustainability Guide: Energy & Water Conservation")
    c.drawString(100, 730, "1. Energy Conservation Tips:")
    c.drawString(120, 710, "- Switch to LED bulbs to save 75% more energy.")
    c.drawString(120, 690, "- Unplug devices when not in use to avoid phantom loads.")
    c.drawString(120, 670, "- Use smart thermostats to optimize heating and cooling.")
    c.drawString(100, 640, "2. Water Saving Habits:")
    c.drawString(120, 620, "- Install low-flow showerheads.")
    c.drawString(120, 600, "- Fix leaking faucets immediately; one drip per second = 3000 gallons/year.")
    c.drawString(120, 580, "- Use rain barrels for garden watering.")
    c.drawString(100, 550, "3. Transportation Impact:")
    c.drawString(120, 530, "- Carpooling reduces emissions by 50% per person.")
    c.drawString(120, 510, "- Electric bikes are 10x more efficient than cars for short trips.")
    c.save()
    print(f"Sample PDF created at {filepath}")

if __name__ == "__main__":
    create_sample_kb()
