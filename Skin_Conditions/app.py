from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np
import os
from werkzeug.utils import secure_filename
from disease_data import diseases, disease_info
import tensorflow as tf


app = Flask(__name__)

# İzin verilen dosya uzantıları
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Dosya uzantısını kontrol eden fonksiyon
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Dosya yükleme yolunu ayarla
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model_path = 'C:/Users/burak/OneDrive/Masaüstü\AI-SKIN - PROJE/Skin_Conditions/trained_tf_model.h5'
# Modeli yükle
model = load_model(model_path)

# Tahmini yapmak için gerekli fonksiyon
def predict_disease(image_path):
    # Resmi yükle ve ön işleme
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Model yükleme
    model_path = 'trained_tf_model.h5'
    model = tf.keras.models.load_model(model_path)

    # Tahmin yapma
    predictions = model.predict(img_array)
    class_indices = np.argmax(predictions, axis=1)[0]

    # Hastalık isimleri
    disease_names = ["Acne", "Carcinoma", "Eczema", "Keratosis", "Milia", "Rosacea"]
    prediction = disease_names[class_indices]
    
    # Hastalık ID'sini bul
    for disease_id, disease_data in diseases.items():
        if disease_data['name'] == prediction:
            prediction_id = disease_id
            break
    
    return prediction, disease_info[prediction], prediction_id

# Hastalık adından ID'yi bulan yardımcı fonksiyon
def get_disease_id_by_name(disease_name):
    for disease_id, disease_data in diseases.items():
        if disease_data['name'].lower() == disease_name.lower():
            return disease_id
    return None

# Hastalık ID'sinden adını bulan yardımcı fonksiyon
def get_disease_name_by_id(disease_id):
    disease = diseases.get(disease_id)
    return disease['name'] if disease else None

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/diases')
def diases():
    return render_template('diases.html')

@app.route('/guess')
def guess():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            prediction, info, prediction_id = predict_disease(filepath)
            disease_name = get_disease_name_by_id(prediction_id)
            return render_template('result.html', 
                                image_filename='uploads/' + filename,
                                prediction=prediction, 
                                disease_info=info,
                                disease_name=disease_name)
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")
            return redirect(url_for('guess'))

@app.route('/disease/<string:disease_name>')
def disease_detail(disease_name):
    disease_id = get_disease_id_by_name(disease_name)
    if disease_id is None:
        return redirect(url_for('index'))
    disease = diseases.get(disease_id)
    return render_template('disease-detail.html', disease=disease)

if __name__ == '__main__':
    app.run(debug=True)
