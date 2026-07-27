import cv2
import mediapipe as mp

mp_tangan = mp.solutions.hands
deteksi_tangan = mp_tangan.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_gambar = mp.solutions.drawing_utils

def jari_terangkat(id_ujung, id_pangkal, titik_tangan):
    return titik_tangan.landmark[id_ujung].y < titik_tangan.landmark[id_pangkal].y

# main func
def apakah_peace(titik_tangan):
    telunjuk_naik = jari_terangkat(8, 6, titik_tangan)
    tengah_naik = jari_terangkat(12, 10, titik_tangan)
    manis_naik = jari_terangkat(16, 14, titik_tangan)
    kelingking_naik = jari_terangkat(20, 18, titik_tangan)
    
    return telunjuk_naik and tengah_naik and not manis_naik and not kelingking_naik

# Buka kamera utama
kamera = cv2.VideoCapture(0)
print("Kamera aktif! Tunjukkan pose ✌️. Tekan 'q' untuk keluar.")

while True:
    sukses, frame = kamera.read()
    if not sukses:
        break
        
    frame = cv2.flip(frame, 1)
    gambar_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hasil = deteksi_tangan.process(gambar_rgb)
    
    peace_terdeteksi = False
    
    if hasil.multi_hand_landmarks:
        for titik_tangan in hasil.multi_hand_landmarks:
            if apakah_peace(titik_tangan):
                peace_terdeteksi = True
            
            # Gambar rangka tangan di layar
            mp_gambar.draw_landmarks(frame, titik_tangan, mp_tangan.HAND_CONNECTIONS)
            
    # Beri efek blur jika pose peace terdeteksi
    if peace_terdeteksi:
        frame = cv2.GaussianBlur(frame, (99, 99), 0)
        
    cv2.imshow("Sal pribadi ngeblur", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()