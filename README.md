Beta Group JCDS 2404 Final Project
FLOWCHART

Dalam proyek ini, kami melakukan analisis data dan pemodelan machine learning menggunakan dataset Bank Marketing Campaign di Portugal pada tahun 2014. Dataset ini berisi informasi tentang apakah nasabah menerima atau menolak untuk menempatkan deposito berjangka setelah bank melakukan kampanye melalui telemarketing. Kendala dalam dataset kami adalah kampanye memakan waktu untuk memilih orang yang potensial dan biaya yang sangat besar, jika perusahaan salah mengontak orang yang tidak tertarik dengan deposito berjangka. Oleh karena itu dibutuhkan cara yang cepat dan andal yang dapat membantu perusahaan memilih orang yang berpotensi menerima tawaran deposito berjangka.

Berikut adalah tabel ML business formulation 

Pada projek ini, kami akan membantu perusahaan untuk meningkatkan efisiensi kampanye marketing ABANCA PT di Portugal yang berencana untuk meningkatkan Dana Pihak Ketiga melalui produk deposito berjangka dengan kampanye outbound telemarketing. Project ini terbagi menjadi 7 bagian penting, yaitu :

Business Understanding : Pada bagian ini berisikan tentang penjelasan mengenai permasalahan bisnis yang akan diselesaikan, tujuan dilakukan nya analisis data dan pemodelan machine learning, pendekatan analisis yang akan dilakukan, serta menjelaskan metrik yang akan digunakan.
Data Understanding and Cleaning : Pada bagian ini berisikan penjelasan mengenai setiap kolom yang ada pada dataset, serta tata cara data cleaning untuk di analisis maupun untuk pemodelan machine learning.
Exploratory Data Analysis : Pada bagian ini berisikan hasil data analisis terkait distribusi data dan korelasi data dari setiap kolom, hasil data analisis mengenai conversion rate setiap fitur terhadap target(deposit/tidak deposit), serta rekomendasi yang didapatkan setelah melakukan analisis data.
Data Preprocessing for Machine Learning : Pada bagian ini berisikan data cleaning untuk pemodelan machine learning, pendefinisian fitur (X) dan target (y), data splitting, pendefinisian encoder, pendefinisian scaler, serta pendefinisian resampler untuk menangani imbalance data.
Modelling and Hyperparameter Tuning : Pada bagian ini berisikan penggunaan metrik, menentukan model-model mana saja yang akan dituning dari hasil cross-validation, dan mendapatkan model dan parameter terbaik yang akan dijadikan final model.
Interpretable model : Pada bagian ini berisikan analisis features importances, interpretasi dari hasil Odds Ratio,  dan analisis SHAP dari final model yang terpilih.
Probability and Financial Analysis : Pada bagian ini berisikan analisis terkait kelas probabilitas terhadap akurasi hasil prediksi serta analisis keuangan final.
Conclusion and Recommendation : Pada bagian ini berisikan kesimpulan dan rekomendasi baik dari hasil analisis data maupun hasil pemodelan machine learning, serta rekomendasi untuk perusahaan.


Selain itu, kami juga telah membuat dashboard tableau untuk menunjukkan visualisasi yang lebih baik, yang terdiri dari 4 menu navigation mengenai :
Dashboard summary company
Dashboard insight company
Dashboard company campaign performance
Dashboard economic indicators
yang dapat diakses melalui link berikut :
https://public.tableau.com/app/profile/sufriana.ana/viz/Beta_Group_JCDS_2404_FinPro_Bank_Marketing_Campaign/Dash_Summary?publish=yes




Selain itu, kami juga mendeploy hasil pemodelan dengan bantuan streamlit. Ini adalah aplikasi Streamlit untuk Final Project yang berfungsi sebagai alat prediksi kampanye pemasaran bank. Berikut adalah hasil dari program ini: 
Prediksi Positif











Prediksi Negatif





Cara Penggunaan deploy model :


Unduh file `term_deposit_prediction.sav`.
BACA Requirements.txt UNTUK MODEL AGAR DAPAT DI-DEPLOY DAN SESUAIKAN DENGAN VERSI LIBRARY ANDA.
Unduh file `Deposit_Apps.py`.
Untuk Windows: Buka Command Prompt, ketik "cd <direktori lokal tempat file yang diunduh (.sav dan .py)>" dan tekan enter, lalu ketik "streamlit run <nama file .py Anda>.py" dan tekan enter.
Untuk MacOS: Buka Terminal, ketik "cd <direktori lokal tempat file yang diunduh (.sav dan .py)>" dan tekan enter, lalu ketik "streamlit run <nama file .py Anda>.py" dan tekan enter.
Aplikasi akan diarahkan ke localhost Anda. Masukkan informasi data pribadi yang diperlukan untuk memprediksi deposito berjangka.
