import re
import os

def convert_css_to_vw_vh(css_content, base_width=1920, base_height=1080):
    """
    Конвертирует CSS размеры в vw/vh для адаптивности
    base_width - базовая ширина экрана (по умолчанию 1920px)
    base_height - базовая высота экрана (по умолчанию 1080px)
    """
    
    # Паттерны для поиска размеров
    patterns = [
        # px в vw (ширина)
        (r'(\d+(?:\.\d+)?)px', 'px_to_vw'),
        # px в vh (высота для определенных свойств)
        (r'(height|min-height|max-height|top|bottom|margin-top|margin-bottom|padding-top|padding-bottom):\s*(\d+(?:\.\d+)?)px', 'px_to_vh'),
        # rem в vw
        (r'(\d+(?:\.\d+)?)rem', 'rem_to_vw'),
        # em в vw
        (r'(\d+(?:\.\d+)?)em', 'em_to_vw'),
    ]
    
    converted_css = css_content
    
    # Конвертируем px в vw для общих случаев
    def px_to_vw(match):
        px_value = float(match.group(1))
        vw_value = (px_value / base_width) * 100
        return f"{vw_value:.4f}vw"
    
    # Конвертируем px в vh для высотных свойств
    def px_to_vh(match):
        property_name = match.group(1)
        px_value = float(match.group(2))
        vh_value = (px_value / base_height) * 100
        return f"{property_name}: {vh_value:.4f}vh"
    
    # Конвертируем rem в vw
    def rem_to_vw(match):
        rem_value = float(match.group(1))
        # Предполагаем, что 1rem = 16px
        px_value = rem_value * 16
        vw_value = (px_value / base_width) * 100
        return f"{vw_value:.4f}vw"
    
    # Конвертируем em в vw
    def em_to_vw(match):
        em_value = float(match.group(1))
        # Предполагаем, что 1em = 16px
        px_value = em_value * 16
        vw_value = (px_value / base_width) * 100
        return f"{vw_value:.4f}vw"
    
    # Применяем конвертацию
    for pattern, conversion_type in patterns:
        if conversion_type == 'px_to_vh':
            converted_css = re.sub(pattern, px_to_vh, converted_css)
        elif conversion_type == 'px_to_vw':
            converted_css = re.sub(pattern, px_to_vw, converted_css)
        elif conversion_type == 'rem_to_vw':
            converted_css = re.sub(pattern, rem_to_vw, converted_css)
        elif conversion_type == 'em_to_vw':
            converted_css = re.sub(pattern, em_to_vw, converted_css)
    
    return converted_css

def process_css_file(input_file, output_file, base_width=1920, base_height=1080):
    """
    Обрабатывает CSS файл и создает адаптивную версию
    """
    try:
        # Читаем исходный CSS файл
        with open(input_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Конвертируем в vw/vh
        converted_css = convert_css_to_vw_vh(css_content, base_width, base_height)
        
        # Записываем результат
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_css)
        
        print(f"✅ CSS файл успешно конвертирован!")
        print(f"📁 Входной файл: {input_file}")
        print(f"📁 Выходной файл: {output_file}")
        print(f"🖥️  Базовая ширина: {base_width}px")
        print(f"🖥️  Базовая высота: {base_height}px")
        
    except FileNotFoundError:
        print(f"❌ Файл {input_file} не найден!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    # Настройки
    input_css = "assets/style/style.css"
    output_css = "assets/style/style_adaptive.css"
    base_width = 1920  # базовая ширина экрана
    base_height = 1080  # базовая высота экрана
    
    # Запускаем конвертацию
    process_css_file(input_css, output_css, base_width, base_height)
    
    print("\n📝 Использование:")
    print("1. Запустите скрипт: python convert_to_vw.py")
    print("2. Получите адаптивный CSS файл: style_adaptive.css")
    print("3. Замените ссылку в HTML на новый файл")
    print("\n💡 Совет: Проверьте результат и при необходимости настройте base_width/base_height")
