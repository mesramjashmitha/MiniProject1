# 🤖 Smart Acne Diagnosis System

An intelligent AI-powered acne detection and diagnosis system that uses deep learning (CNN) and symptom analysis to provide personalized treatment recommendations.

## 📋 Project Overview

This mini project combines:
- **Computer Vision (CNN Model)** - Detects acne types from facial images
- **Symptom Analysis** - Questionnaire-based severity assessment
- **Web Interface (Flask)** - User-friendly web application
- **Medical Database** - Comprehensive medicine and treatment suggestions

### Supported Acne Types
- **Blackheads** - Oil and dirt clogging pores
- **Whiteheads** - Closed pores trapping oil and bacteria
- **Papules** - Small red bumps from inflammation
- **Pustules** - Pus-filled pimples from bacterial infection
- **Cysts** - Deep, painful acne under skin layers

## 🛠️ Technologies Used

- **Python 3.x**
- **TensorFlow/Keras** - Deep learning framework
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **OpenCV** - Image processing
- **Pillow (PIL)** - Image manipulation
- **NumPy** - Numerical computing
- **HTML/JavaScript** - Frontend interface
- **Haar Cascades** - Face detection

## 📁 Project Structure

```
MiniProject1/
├── app.py                          # Flask API for main prediction
├── symptoms.py                     # Symptom analyzer API
├── diagnosis_system.py             # CLI-based diagnosis system
├── acne_cnn_best_model.py         # CNN model training & evaluation
├── final_acne_system.py           # Complete system integration
├── clean_dataset.py               # Data preprocessing
├── label_images.py                # Dataset labeling utility
├── predict.py                     # Prediction script
├── predict_acne.py                # Simple prediction module
├── preprocess.py                  # Image preprocessing
├── index.html                     # Main web interface
├── choose.html                    # Action selection page
├── symptoms.html                  # Symptom questionnaire page
├── haarcascade_frontalface_default.xml  # Face detection model
├── acne_model.keras               # Trained model (Keras format)
├── class_names.npy                # Model class labels
├── classes.json                   # Acne classes configuration
├── data.yaml                      # Data configuration
├── records.json                   # User prediction history
├── new dataset1.xlsx              # Dataset file
├── analysis.jpeg                  # Model analysis visualization
├── history.jpeg                   # Training history chart
├── cyts1.jpg                      # Sample test image
├── static/                        # Static files directory
└── .gitignore                     # Git ignore rules
```

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mesramjashmitha/MiniProject1.git
   cd MiniProject1
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install tensorflow keras flask flask-cors opencv-python pillow numpy
   ```

## 📖 Usage

### Option 1: Web Interface (Recommended)

1. **Start Flask API**
   ```bash
   python app.py
   ```

2. **Open in browser**
   ```
   http://localhost:5000
   ```

3. **Follow these steps:**
   - Upload facial image
   - Enter personal details (name, age, gender)
   - Get AI diagnosis with confidence score
   - View recommended medicines and advice

### Option 2: Symptom Analysis

1. **Start Symptom API**
   ```bash
   python symptoms.py
   ```

2. **Access the API**
   ```
   http://localhost:5000/questions (GET) - Get all questions
   http://localhost:5000/analyze (POST) - Submit answers
   ```

### Option 3: CLI-Based Diagnosis

1. **Run diagnosis system**
   ```bash
   python diagnosis_system.py
   ```

2. **Answer questionnaire prompts**
   - System calculates risk score
   - Provides severity level (MILD/MODERATE/SEVERE)
   - Recommends treatment options

### Option 4: CNN Model Training

1. **Run CNN model**
   ```bash
   python acne_cnn_best_model.py
   ```

## 🤖 AI Model Details

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 224x224 pixels
- **Output**: 5 acne class probabilities
- **Preprocessing**: Normalization (0-1 range)
- **Format**: Keras (.keras) and H5 (.h5)

### Model Classes
```
0: Blackheads
1: Whiteheads
2: Papules
3: Pustules
4: Cysts
```

## 💊 Treatment Recommendations

The system provides 5 severity levels for each acne type:

### Severity Levels
1. **Very Low** - Minimal condition, basic prevention
2. **Low** - Early stage, OTC treatment
3. **Medium** - Moderate condition, topical medication
4. **High** - Serious condition, strong treatment
5. **Severe** - Critical condition, medical consultation required

### Sample Recommendations

**Blackheads - Medium Level:**
- Medicine: Salicylic acid cleanser, Charcoal mask, Adapalene gel
- Advice: Exfoliate regularly and maintain strict skincare routine

**Pustules - Severe Level:**
- Medicine: Oral antibiotics, Strong medication, Dermatologist consultation
- Advice: Immediate medical consultation required

## 📊 Features

✅ **Image-based Detection** - Upload facial images for AI analysis  
✅ **Symptom Questionnaire** - 20-question form for comprehensive assessment  
✅ **Confidence Scoring** - Model predicts with confidence percentage  
✅ **Personalized Treatment** - Medicine and advice based on severity  
✅ **History Tracking** - Save and retrieve user prediction history  
✅ **Web Interface** - User-friendly HTML/JavaScript frontend  
✅ **API Endpoints** - RESTful API for integration  
✅ **Face Detection** - Haar Cascade for face localization  

## 📡 API Endpoints

### Main Prediction API
```
POST /predict
- Input: Image file, name, age, gender
- Output: Disease, confidence, level, recommendations
```

### History API
```
GET /history/<name>
- Returns: All previous predictions for user
```

### Questions API
```
GET /questions
- Returns: All symptom questionnaire questions
```

### Analysis API
```
POST /analyze
- Input: Array of answer scores (0-4)
- Output: Total score and severity level
```

## 🔄 Data Flow

```
User Input (Image)
       ↓
Image Preprocessing (224x224)
       ↓
CNN Model Prediction
       ↓
Confidence Calculation
       ↓
Severity Level Mapping
       ↓
Treatment Database Lookup
       ↓
Personalized Recommendation
       ↓
Save to History
       ↓
JSON Response to Frontend
```

## 📝 Sample Response

```json
{
  "name": "John Doe",
  "age": "25",
  "gender": "Male",
  "disease": "blackheads",
  "confidence": 87.45,
  "level": "High",
  "reason": "Heavy oil buildup is causing deep pore blockage and prominent blackheads.",
  "medicine": [
    "Apply adapalene cream",
    "Use salicylic acid gel",
    "Apply charcoal face mask",
    "Use retinoid cream",
    "Apply oil control serum"
  ],
  "advice": "Avoid touching your face and follow a strict cleansing routine.",
  "image": "/static/upload.jpg"
}
```

## ⚙️ Configuration

### Class Names
```json
["blackheads", "cysts", "papules", "pustules", "whiteheads"]
```

### Severity Thresholds
- Very Low: ≤ 10% confidence
- Low: 10-20% confidence
- Medium: 20-40% confidence
- High: 40-60% confidence
- Severe: > 60% confidence

## 🧠 Model Training Process

1. **Data Collection** - Acne images labeled by type
2. **Data Cleaning** - Remove duplicates and invalid images
3. **Preprocessing** - Resize, normalize, augment
4. **Model Training** - CNN with multiple layers
5. **Validation** - Test on unseen data
6. **Optimization** - Fine-tune hyperparameters

## 📈 Results

- Model outputs predictions with confidence scores
- Generates training history (history.jpeg)
- Analysis reports (analysis.jpeg)
- Tracks user predictions in records.json

## ⚠️ Disclaimer

**This AI system is for educational purposes only.** 

- Not a substitute for professional medical advice
- Always consult a dermatologist for persistent acne
- Recommendations are AI-based suggestions
- Verify medication names and dosages with healthcare providers

## 🐛 Troubleshooting

### Model Not Found
```
Error: Model file not found!
Solution: Ensure acne_model.keras or acne_cnn_best_model.h5 exists
```

### Image Upload Failed
```
Error: No image uploaded
Solution: Select a valid image file before submitting
```

### API Port Already in Use
```
Error: Address already in use
Solution: Change port in app.run(port=5001) or stop other processes
```

## 👥 Author

**Jashmitha Mesram**  
GitHub: [@mesramjashmitha](https://github.com/mesramjashmitha)

## 📄 License

This project is currently unlicensed. Feel free to add a license file as needed.

## 🎓 Educational Purpose

This is a mini project created for learning and development purposes, demonstrating:
- Deep learning with TensorFlow/Keras
- Web development with Flask
- Medical AI applications
- REST API design
- Frontend-backend integration

## 🔗 Related Files

- `data.yaml` - Dataset configuration
- `classes.json` - Acne class definitions
- `records.json` - User history database
- Model weights: `acne_model.keras` or `acne_cnn_best_model.h5`

---

**Version**: 1.0  
**Created**: February 24, 2026  
**Last Updated**: June 10, 2026  
**Language**: Python  
**Status**: Active Development
