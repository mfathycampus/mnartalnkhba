from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import logging

# إعداد التطبيق
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # يمكن تغييره لاحقًا

# إعداد الخدمات (تُستخدم في الصفحة الرئيسية)
services = [
    {
        'title': 'أنظمة المراقبة',
        'description': 'تركيب وصيانة كاميرات المراقبة بأحدث التقنيات.',
        'image': 'security_cameras.jpg'
    },
    {
        'title': 'الشبكات',
        'description': 'بناء شبكات داخلية وربط الفروع بخبرة عالية.',
        'image': 'servers_networks.jpg'
    },
    {
        'title': 'البصمة والحضور',
        'description': 'أنظمة البصمة لإدارة حضور الموظفين.',
        'image': 'fingerprint_system.jpg'
    },
    {
        'title': 'الدعم الفني',
        'description': 'دعم فني دائم للحلول التقنية وتحديث الأنظمة.',
        'image': 'maintenance.jpg'
    },
    {
        'title': 'التوريد',
        'description': 'توريد جميع التجهيزات التقنية والمعدات بأعلى جودة.',
        'image': 'keyboard_mouse.jpg'
    }
]

# ✅ إعدادات البريد باستخدام SMTP الخاص بـ Hostinger
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 993
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'info@manrtalnkhba.com'
app.config['MAIL_PASSWORD'] = 'M@$ter2030'

# تفعيل تسجيل الأخطاء
logging.basicConfig(level=logging.DEBUG)

# إنشاء كائن البريد
mail = Mail(app)

# ✅ الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', services=services)

# ✅ معالجة إرسال الرسائل من نموذج الاتصال
@app.route('/send', methods=['POST'])
def send():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f'رسالة جديدة من {name}',
            sender=app.config['info@manrtalnkhba.com'],  # يجب أن يكون نفس بريد الإرسال
            recipients=['info@manrtalnkhba.com'],
            body=f'''
            الاسم: {name}
            البريد الإلكتروني: {email}

            الرسالة:
            {message}
            '''
        )

        mail.send(msg)
        flash('✅ تم إرسال رسالتك بنجاح', 'success')
    except Exception as e:
        flash('❌ فشل إرسال الرسالة. تأكد من إعدادات البريد أو اتصل بالدعم', 'danger')
        print(f"⚠️ خطأ أثناء الإرسال: {e}")

    return redirect('/#contact')

# ✅ تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
