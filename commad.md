Описание:
Главный экран: Отображает текст "Привет, меня зовут Осман!" и кнопку "Нажми на меня!!!".
Смена фона: По нажатию на кнопку цвет фона меняется с белого на черный и обратно. Одновременно меняется и цвет текста.
Kivy: Используем библиотеку Kivy, которая предоставляет удобные компоненты для создания Android-приложений на Python.
Как запустить на Android:
Убедитесь, что у вас установлен buildozer для упаковки приложения в APK:

bash
Копировать код
pip install buildozer
Инициализируйте проект:

bash
Копировать код
buildozer init
Отредактируйте файл buildozer.spec, указав нужные настройки.

Создайте APK:

bash
Копировать код
buildozer -v android debug
Этот код создаст простое приложение, которое можно запустить на Android.

./sdkmanager --install "platform-tools" "platforms;android-29" "build-tools;29.0.3"

sdkmanager --install "platform-tools" "platforms;android-30" "build-tools;30.0.3"


