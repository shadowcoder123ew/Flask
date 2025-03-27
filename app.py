from flask import Flask, Response
import random
import string

app = Flask(__name__)

def generate_large_file():
    # تعداد حروف در هر بخش
    chunk_size = 1024 * 1024  # هر بخش 1 مگابایت
    num_per_chunk = chunk_size  # هر کاراکتر یک بایت است
    
    # جنریت حروف تصادفی بزرگ
    for _ in range(100):  # به طور کلی 100 مگابایت داده تولید می‌شود
        letters = ''.join(random.choices(string.ascii_letters, k=num_per_chunk))
        yield letters

@app.route('/generate_file')
def generate_file():
    return Response(generate_large_file(), 
                    content_type='text/plain', 
                    status=200, 
                    headers={"Content-Disposition": "attachment;filename=generated_file.txt"})

if __name__ == '__main__':
    app.run(debug=True)
