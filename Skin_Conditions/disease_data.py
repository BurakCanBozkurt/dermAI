# Hastalık bilgileri sözlüğü
diseases = {
    1: {
        'id': 1,
        'name': 'Carcinoma',
        'icon': 'fa-virus',
        'severity': 'Yüksek',
        'severity_class': 'high',
        'prevalence': 'Sık görülür',
        'overview': 'Carcinoma, cilt veya organlardaki epitel hücrelerinden kaynaklanan bir tür kanserdir. Erken teşhis edildiğinde tedavi şansı yüksektir.',
        'main_image': 'images/diseases/carcinoma/main.jpg',
        'images': [
            'images/diseases/carcinoma/1.jpg',
            'images/diseases/carcinoma/2.jpg',
            'images/diseases/carcinoma/3.jpg',
            'images/diseases/carcinoma/4.jpg'
        ],
        'symptoms': [
            'Ciltte kalıcı, pullu veya kabuğumsu lekeler',
            'Düzensiz şekilli benler',
            'Kanamaya meyilli yaralar',
            'Ciltte renk değişiklikleri'
        ],
        'risk_factors': [
            'Uzun süreli güneş maruziyeti',
            'İleri yaş',
            'Açık ten rengi',
            'Aile öyküsü'
        ],
        'treatments': [
            'Cerrahi müdahale',
            'Radyoterapi',
            'Kemoterapi',
            'İmmünoterapi'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-sun',
                'title': 'Güneş Koruması',
                'description': 'Güneş kremi kullanın ve direkt güneş ışığından kaçının'
            },
            {
                'icon': 'fa-clock',
                'title': 'Düzenli Kontrol',
                'description': 'Düzenli cilt muayenesi yaptırın'
            },
            {
                'icon': 'fa-shield-alt',
                'title': 'Koruyucu Giysi',
                'description': 'UV koruyucu kıyafetler tercih edin'
            }
        ],
        'expert': {
            'name': 'Dr. Ayşe Yılmaz',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-ayse.jpg',
            'opinion': 'Carcinoma vakalarında erken teşhis hayat kurtarıcıdır. Düzenli cilt muayenesi ve güneş koruması en önemli önleyici faktörlerdir.'
        },
        'faqs': [
            {
                'question': 'Carcinoma ne kadar yaygın görülür?',
                'answer': 'Carcinoma, en yaygın görülen cilt kanseri türüdür. Her yıl milyonlarca yeni vaka teşhis edilmektedir.'
            },
            {
                'question': 'Carcinoma tedavi edilebilir mi?',
                'answer': 'Evet, erken teşhis edildiğinde carcinoma yüksek tedavi başarısına sahiptir.'
            },
            {
                'question': 'Carcinoma belirtileri nelerdir?',
                'answer': 'Başlıca belirtiler arasında ciltte pullanma, düzensiz şekilli benler ve kanamaya meyilli yaralar bulunur.'
            }
        ]
    },
    2: {
        'id': 2,
        'name': 'Keratosis',
        'icon': 'fa-allergies',
        'severity': 'Orta',
        'severity_class': 'medium',
        'prevalence': 'Yaygın',
        'overview': 'Keratosis, ciltte kalınlaşma veya sertleşmeye neden olan iyi huylu bir durumdur. Genellikle yaşlanma ile ilişkilidir.',
        'main_image': 'images/diseases/keratosis/main.jpg',
        'images': [
            'images/diseases/keratosis/1.jpg',
            'images/diseases/keratosis/2.jpg',
            'images/diseases/keratosis/3.jpg',
            'images/diseases/keratosis/4.jpg'
        ],
        'symptoms': [
            'Ciltte kalınlaşmış, pürüzlü alanlar',
            'Kahverengi veya pembe lekeler',
            'Kaşıntı',
            'Ciltte kuruluk'
        ],
        'risk_factors': [
            'İleri yaş',
            'Güneş hasarı',
            'Açık ten rengi',
            'Sık güneşlenme'
        ],
        'treatments': [
            'Kriyoterapi',
            'Topikal kremler',
            'Lazer tedavisi',
            'Cerrahi müdahale'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-sun',
                'title': 'Güneş Koruması',
                'description': 'SPF 30 ve üzeri güneş kremi kullanın'
            },
            {
                'icon': 'fa-tint',
                'title': 'Nemlendirme',
                'description': 'Cildinizi düzenli olarak nemlendirin'
            },
            {
                'icon': 'fa-check',
                'title': 'Düzenli Kontrol',
                'description': 'Yılda bir kez cilt muayenesi yaptırın'
            }
        ],
        'expert': {
            'name': 'Dr. Mehmet Demir',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-mehmet.jpg',
            'opinion': 'Keratosis tedavi edilebilir bir durumdur. Erken teşhis ve düzenli bakım ile kontrol altında tutulabilir.'
        },
        'faqs': [
            {
                'question': 'Keratosis bulaşıcı mıdır?',
                'answer': 'Hayır, keratosis bulaşıcı değildir.'
            },
            {
                'question': 'Keratosis kanser belirtisi midir?',
                'answer': 'Hayır, keratosis genellikle iyi huylu bir cilt durumudur.'
            },
            {
                'question': 'Keratosis tedavi edilmezse ne olur?',
                'answer': 'Tedavi edilmezse büyüyebilir ve rahatsızlık verebilir, ancak genellikle ciddi bir sağlık riski oluşturmaz.'
            }
        ]
    },
    3: {
        'id': 3,
        'name': 'Milia',
        'icon': 'fa-dot-circle',
        'severity': 'Düşük',
        'severity_class': 'low',
        'prevalence': 'Yaygın',
        'overview': 'Milia, cilt altında oluşan küçük, beyaz kistlerdir. Genellikle yüz bölgesinde görülür ve zararsızdır.',
        'main_image': 'images/diseases/milia/main.jpg',
        'images': [
            'images/diseases/milia/1.jpg',
            'images/diseases/milia/2.jpg',
            'images/diseases/milia/3.jpg',
            'images/diseases/milia/4.jpg'
        ],
        'symptoms': [
            'Küçük, beyaz kabarcıklar',
            'Yüzde yaygın görülme',
            'Ağrısız kistler',
            'Düzgün yüzeyli lezyonlar'
        ],
        'risk_factors': [
            'Güneş hasarı',
            'Cilt travması',
            'Steroid kremlerin kullanımı',
            'Genetik yatkınlık'
        ],
        'treatments': [
            'Mikro iğneleme',
            'Kriyoterapi',
            'Topikal retinoidler',
            'Manuel ekstraksiyon'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-face-wash',
                'title': 'Cilt Temizliği',
                'description': 'Düzenli ve nazik cilt temizliği yapın'
            },
            {
                'icon': 'fa-cream',
                'title': 'Uygun Ürünler',
                'description': 'Cildinize uygun bakım ürünleri kullanın'
            },
            {
                'icon': 'fa-hand-holding-medical',
                'title': 'Profesyonel Bakım',
                'description': 'Düzenli cilt bakımı yaptırın'
            }
        ],
        'expert': {
            'name': 'Dr. Zeynep Yıldız',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-zeynep.jpg',
            'opinion': 'Milia genellikle zararsızdır ve kendiliğinden geçebilir. Ancak rahatsız edici olduğunda profesyonel müdahale gerekebilir.'
        },
        'faqs': [
            {
                'question': 'Milia kendiliğinden geçer mi?',
                'answer': 'Evet, milia bazen kendiliğinden geçebilir, ancak bu süreç aylar alabilir.'
            },
            {
                'question': 'Milia önlenebilir mi?',
                'answer': 'Düzenli cilt bakımı ve uygun ürün kullanımı ile oluşum riski azaltılabilir.'
            },
            {
                'question': 'Evde milia tedavisi yapılabilir mi?',
                'answer': 'Profesyonel müdahale önerilir, evde yapılan müdahaleler cilt hasarına yol açabilir.'
            }
        ]
    },
    4: {
        'id': 4,
        'name': 'Acne',
        'icon': 'fa-bacteria',
        'severity': 'Orta',
        'severity_class': 'medium',
        'prevalence': 'Çok Yaygın',
        'overview': 'Akne, yağ bezlerinin tıkanması sonucu oluşan yaygın bir cilt problemidir. Özellikle ergenlik döneminde sık görülür.',
        'main_image': 'images/diseases/acne/main.jpg',
        'images': [
            'images/diseases/acne/1.jpg',
            'images/diseases/acne/2.jpg',
            'images/diseases/acne/3.jpg',
            'images/diseases/acne/4.jpg'
        ],
        'symptoms': [
            'Sivilceler',
            'Kızarıklık',
            'İltihaplı kabarcıklar',
            'Yağlı cilt'
        ],
        'risk_factors': [
            'Hormonal değişimler',
            'Genetik faktörler',
            'Stres',
            'Yağlı cilt yapısı'
        ],
        'treatments': [
            'Topikal tedaviler',
            'Oral antibiyotikler',
            'Retinoidler',
            'Kimyasal peeling'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-soap',
                'title': 'Düzenli Temizlik',
                'description': 'Günde iki kez nazik temizleyici ile yüz yıkayın'
            },
            {
                'icon': 'fa-hand-holding-water',
                'title': 'Nemlendirme',
                'description': 'Oil-free nemlendirici kullanın'
            },
            {
                'icon': 'fa-ban',
                'title': 'Dokunmayın',
                'description': 'Sivilceleri sıkmaktan kaçının'
            }
        ],
        'expert': {
            'name': 'Dr. Can Yılmaz',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-can.jpg',
            'opinion': 'Akne tedavi edilebilir bir durumdur. Doğru bakım ve tedavi ile kontrol altına alınabilir.'
        },
        'faqs': [
            {
                'question': 'Akne neden oluşur?',
                'answer': 'Hormonal değişimler, genetik faktörler ve çevresel etkenler akneye neden olabilir.'
            },
            {
                'question': 'Akne izleri kalıcı mıdır?',
                'answer': 'Erken ve doğru tedavi ile akne izleri minimize edilebilir.'
            },
            {
                'question': 'Beslenme akneyi etkiler mi?',
                'answer': 'Bazı besinler akneyi tetikleyebilir, dengeli beslenme önemlidir.'
            }
        ]
    },
    5: {
        'id': 5,
        'name': 'Rosacea',
        'icon': 'fa-fire',
        'severity': 'Orta',
        'severity_class': 'medium',
        'prevalence': 'Yaygın',
        'overview': 'Rosacea, yüzde kızarıklık ve iltihaplanma ile karakterize kronik bir cilt hastalığıdır.',
        'main_image': 'images/diseases/rosacea/main.jpg',
        'images': [
            'images/diseases/rosacea/1.jpg',
            'images/diseases/rosacea/2.jpg',
            'images/diseases/rosacea/3.jpg',
            'images/diseases/rosacea/4.jpg'
        ],
        'symptoms': [
            'Yüzde kalıcı kızarıklık',
            'Görünür kan damarları',
            'Şişlik ve kabarıklık',
            'Yanma ve batma hissi'
        ],
        'risk_factors': [
            'Açık ten rengi',
            'Aile öyküsü',
            'Sıcak yiyecek/içecekler',
            'Güneş maruziyeti'
        ],
        'treatments': [
            'Topikal antibiyotikler',
            'Oral ilaçlar',
            'Lazer tedavisi',
            'Tetikleyicilerden kaçınma'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-temperature-low',
                'title': 'Tetikleyicilerden Kaçının',
                'description': 'Sıcak, baharatlı ve alkollü içeceklerden uzak durun'
            },
            {
                'icon': 'fa-sun-protection',
                'title': 'Güneş Koruması',
                'description': 'Her gün güneş kremi kullanın'
            },
            {
                'icon': 'fa-face-relax',
                'title': 'Stres Yönetimi',
                'description': 'Stresi azaltmak için önlemler alın'
            }
        ],
        'expert': {
            'name': 'Dr. Elif Kaya',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-elif.jpg',
            'opinion': 'Rosacea kronik bir hastalıktır ancak doğru tedavi ve yaşam tarzı değişiklikleri ile kontrol altına alınabilir.'
        },
        'faqs': [
            {
                'question': 'Rosacea bulaşıcı mıdır?',
                'answer': 'Hayır, rosacea bulaşıcı değildir.'
            },
            {
                'question': 'Rosacea tedavi edilebilir mi?',
                'answer': 'Tamamen tedavisi yoktur ancak semptomlar kontrol altına alınabilir.'
            },
            {
                'question': 'Rosaceayı ne tetikler?',
                'answer': 'Sıcak, soğuk, stres, bazı yiyecekler ve güneş tetikleyici olabilir.'
            }
        ]
    },
    6: {
        'id': 6,
        'name': 'Eczema',
        'icon': 'fa-disease',
        'severity': 'Orta',
        'severity_class': 'medium',
        'prevalence': 'Yaygın',
        'overview': 'Egzama, ciltte kaşıntı, kızarıklık ve iltihaplanmaya neden olan kronik bir cilt hastalığıdır.',
        'main_image': 'images/diseases/eczema/main.jpg',
        'images': [
            'images/diseases/eczema/1.jpg',
            'images/diseases/eczema/2.jpg',
            'images/diseases/eczema/3.jpg',
            'images/diseases/eczema/4.jpg'
        ],
        'symptoms': [
            'Şiddetli kaşıntı',
            'Kuru ve pullu cilt',
            'Kızarıklık',
            'Çatlaklar'
        ],
        'risk_factors': [
            'Aile öyküsü',
            'Alerjiler',
            'Stres',
            'Çevresel faktörler'
        ],
        'treatments': [
            'Nemlendiriciler',
            'Topikal kortikosteroidler',
            'Antihistaminikler',
            'Işık tedavisi'
        ],
        'prevention_tips': [
            {
                'icon': 'fa-shower',
                'title': 'Nazik Temizlik',
                'description': 'Ilık su ve yumuşak temizleyiciler kullanın'
            },
            {
                'icon': 'fa-droplet',
                'title': 'Nemlendirme',
                'description': 'Düzenli nemlendirici kullanın'
            },
            {
                'icon': 'fa-temperature-arrow-down',
                'title': 'Tetikleyicilerden Kaçının',
                'description': 'Alerjen ve tahriş edici maddelerden uzak durun'
            }
        ],
        'expert': {
            'name': 'Dr. Ali Yıldız',
            'title': 'Dermatoloji Uzmanı',
            'image': 'images/experts/dr-ali.jpg',
            'opinion': 'Egzama yaşam kalitesini etkileyebilir ancak doğru bakım ve tedavi ile kontrol altına alınabilir.'
        },
        'faqs': [
            {
                'question': 'Egzama bulaşıcı mıdır?',
                'answer': 'Hayır, egzama bulaşıcı değildir.'
            },
            {
                'question': 'Egzama tamamen geçer mi?',
                'answer': 'Kronik bir durumdur ancak semptomlar kontrol altına alınabilir.'
            },
            {
                'question': 'Egzama alevlenmelerini ne tetikler?',
                'answer': 'Stres, alerjiler, hava değişimleri ve bazı kimyasallar tetikleyici olabilir.'
            }
        ]
    }
}

# Hastalık isimleri ve bilgileri
disease_info = {
    "Acne": "Akne, cilt gözeneklerinin tıkanması sonucu ortaya çıkar.",
    "Carcinoma": "Karsinom, ciltteki kanser türlerinden biridir.",
    "Eczema": "Egzama, ciltte kaşıntı ve döküntülere yol açan bir hastalıktır.",
    "Keratosis": "Keratoz, ciltte kabarık lekelerle karakterize edilir.",
    "Milia": "Milia, cilt altında oluşan küçük beyaz kistlerdir.",
    "Rosacea": "Rozasea, yüz bölgesinde kızarıklık ve şişliklere neden olur."
} 