<div dir="rtl">
<h1> مسار أساسيات بايثون </h1>
<p>الشيفرة المصدرية الخاصة بمسار أساسيات بايثون ضمن دورة "تطوير التطبيقات باستخدام لغة Python" المقدمة من أكاديمية حسوب</p>

<div>
<a href="https://academy.hsoub.com/learn/Python-application-development/">دورة تطوير التطبيقات باستخدام لغة Python</a>
</div>
<h2> تطبيق Taskaty </h2>
<p>برامج بسيط لإدارة المهام</p>
<h2> طريقة التثبيت </h2>
<ul>
  <li>نسخ المستودع <code>git clone https://github.com/HsoubAcademy/python_basics</code></li>
  <li>الانتقال إلى المجلد <code>cd python_basics</code></li>
  <li>إنشاء بيئة وهمية <code>python -m venv venv</code> أو <code>python3 -m venv venv</code></li>
  <li>تفعيل البيئة الوهمية
    <ul>
      <li>على ويندوز <code>venv\Scripts\activate</code></li>
      <li>على ماك أو لينكس <code>source venv/bin/activate</code></li>
    </ul>
  </li>
  <li>تثبيت التطبيق <code>pip install -e .</code></li>
</ul>
<h2>طريقة الاستخدام</h2>
<p>يمكنك تشغيل التطبيق من سطر الأوامر باستخدام الأمر <code>taskaty</code></p>
<h3>إضافة مهمة</h3>
<pre dir="ltr">taskaty add "Add search bar compoent to the UI"</pre>
<h3>عرض المهام</h3>
<pre dir="ltr">taskaty list</pre>
<h3>إنهاء مهمة</h3>
<pre dir="ltr">taskaty check -t <task_number></pre>
<h3>حذف مهمة</h3>
<pre dir="ltr">taskaty remove -t <task_number></pre>
<h3>حذف كل المهام</h3>
<pre dir="ltr">taskaty reset</pre>
</div>

