# 🌍 EcoTrack AI

An AI-powered Carbon Footprint Awareness Assistant that helps users estimate their carbon emissions based on daily lifestyle habits and provides personalized recommendations to encourage sustainable living.

---

## 📌 Chosen Vertical

**Carbon Footprint Awareness**

---

## 📖 Overview

EcoTrack AI is designed to raise awareness about environmental sustainability by estimating a user's carbon footprint and generating actionable suggestions to reduce emissions. The application analyzes transportation habits, electricity consumption, and dietary preferences to calculate total CO₂ emissions and assign an Eco Score.

---

## ✨ Features

* 🌱 Carbon Footprint Calculator
* 📊 Eco Score Generation
* 🤖 Intelligent Recommendation Engine
* 🚶 Personalized Sustainability Tips
* 📱 Responsive and User-Friendly Interface
* 🧪 Unit Testing for Reliability
* 🔒 Input Validation and Secure Design

---

## 🛠 Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3

### Testing

* Pytest

### Version Control

* Git & GitHub

---

## ⚙ How It Works

1. User enters:

   * Name
   * Transport mode
   * Distance travelled
   * Monthly electricity consumption
   * Dietary preference

2. The system calculates carbon emissions using predefined emission factors.

3. An Eco Score is generated based on the estimated emissions.

4. The recommendation engine provides personalized suggestions to help reduce the user's carbon footprint.

5. Results are displayed in an easy-to-understand format.

---

## 🧠 Project Architecture

User Input
↓
Carbon Calculator
↓
CO₂ Emission Calculation
↓
Eco Score Generation
↓
Recommendation Engine
↓
Result Display

---

## 📂 Project Structure

```
EcoTrack-AI
│
├── app.py
├── carbon_calculator.py
├── recommendation_engine.py
├── requirements.txt
├── README.md
│
├── templates
│     ├── index.html
│     └── result.html
│
├── static
│     └── style.css
│
└── tests
      └── test_calculator.py
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/EcoTrack-AI.git
```

Navigate to the project directory:

```bash
cd EcoTrack-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🔒 Security Considerations

* Input validation is implemented.
* Negative values are prevented.
* No sensitive user information is stored.
* Modular and maintainable code structure.

---

## ♿ Accessibility

* Responsive design
* Simple and intuitive interface
* Mobile-friendly layout
* Readable typography and color scheme

---

## 📌 Assumptions

* Average emission factors are used for transportation.
* Electricity consumption is considered on a monthly basis.
* Dietary habits influence carbon emissions.
* Recommendations are based on predefined sustainability guidelines.

---

## 🌎 Future Enhancements

* AI-powered recommendations using Gemini API
* Carbon footprint history tracking
* Interactive charts and analytics
* Weekly sustainability reports
* Gamification with badges and achievements
* Dark mode support

---

## 👨‍💻 Author

**Rajalakshmi S**
B.E. Computer Science and Engineering
Global Institute of Engineering and Technology

---

### "Small changes today create a greener tomorrow." 🌿
