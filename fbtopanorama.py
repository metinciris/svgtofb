import tkinter as tk
from tkinter import filedialog, messagebox, Label, ttk, simpledialog
from PIL import Image, ImageTk, ImageFile
import openslide
import os
import io

# Pillow'un büyük görüntüleri işleyebilmesi için limitini artırın
Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

def select_svs_file():
    svs_path = filedialog.askopenfilename(
        title="SVS Dosyasını Seç",
        filetypes=[("SVS Dosyaları", "*.svs"), ("Tüm Dosyalar", "*.*")]
    )
    if svs_path:
        process_svs_to_jpeg(svs_path)

def process_svs_to_jpeg(svs_path):
    try:
        # SVS dosyasını aç
        slide = openslide.OpenSlide(svs_path)
        level = 0  # En yüksek çözünürlük katmanı genellikle 0'dır
        level_dimensions = slide.level_dimensions[level]

        # Görüntüyü oku
        image = slide.read_region((0, 0), level, level_dimensions)
        image = image.convert('RGB')

        # Görüntüyü 2:1 oranında kırp
        width, height = image.size
        new_height = width // 2
        top_crop = (height - new_height) // 2
        image_cropped = image.crop((0, top_crop, width, top_crop + new_height))

        # Görüntüyü Facebook'un boyut sınırlarına göre yeniden boyutlandır
        if width > 30000 or height > 30000 or (width * height) > 128000000:
            scale_factor = min(30000 / width, 30000 / height, (128000000 / (width * height))**0.5)
            new_width = int(width * scale_factor)
            new_height = int(new_height * scale_factor)
            image_cropped = image_cropped.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # İlerlemeyi göstermek için önizleme oluşturma
        preview_image = image_cropped.copy()
        preview_image.thumbnail((800, 400), Image.Resampling.LANCZOS)
        img_preview = ImageTk.PhotoImage(preview_image)
        preview_label.config(image=img_preview)
        preview_label.image = img_preview

        # JPEG kalite ayarı ve dosya boyutu optimizasyonu
        global output_path
        output_path = os.path.splitext(svs_path)[0] + "_panoramic_optimized.jpg"

        quality = 85  # Başlangıç kalitesi 85
        buffer = io.BytesIO()
        image_cropped.save(buffer, format="JPEG", quality=quality)
        size = buffer.tell() / (1024 * 1024)

        while size > 30 and quality > 10:
            quality -= 5  # Kaliteyi 5 birim azalt
            buffer = io.BytesIO()
            image_cropped.save(buffer, format="JPEG", quality=quality)
            size = buffer.tell() / (1024 * 1024)

        # Son olarak dosyayı kaydet
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())

        messagebox.showinfo("Başarılı", f"Görüntü başarıyla {output_path} olarak kaydedildi. Kalite: {quality} - Boyut: {size:.2f} MB")

    except Exception as e:
        messagebox.showerror("Hata", f"Görüntü işlenirken bir hata oluştu: {str(e)}")

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("SVS'den Yüksek Kaliteli JPEG'e Dönüştürücü")
root.geometry("900x600")

output_path = None  # Global değişken

# İlerleme ve önizleme için öğeler
preview_label = Label(root)
preview_label.pack(pady=20)

progress_bar = ttk.Progressbar(root, mode='indeterminate')
progress_bar.pack(fill=tk.X, padx=40, pady=20)

# Dosya seçme butonu
select_button = tk.Button(root, text="SVS Dosyasını Seç ve İşle", command=select_svs_file, font=("Arial", 12))
select_button.pack(expand=True)

root.mainloop()
