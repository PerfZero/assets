import re
import os

def convert_css_to_vw_vh(css_content, base_width=1920, base_height=1080):
    """
    Улучшенная конвертация CSS размеров в vw/vh
    """
    
    # Свойства, которые лучше конвертировать в vh
    vh_properties = {
        'height', 'min-height', 'max-height', 'top', 'bottom',
        'margin-top', 'margin-bottom', 'padding-top', 'padding-bottom',
        'line-height'
    }
    
    # Свойства, которые лучше оставить в px (мелкие детали)
    px_properties = {
        'border-width', 'border-radius', 'box-shadow', 'text-shadow',
        'letter-spacing', 'word-spacing', 'outline-width'
    }
    
    # Свойства, которые лучше конвертировать в vw
    vw_properties = {
        'width', 'max-width', 'min-width', 'left', 'right',
        'margin-left', 'margin-right', 'padding-left', 'padding-right',
        'font-size', 'border-left-width', 'border-right-width'
    }
    
    def convert_value(value, unit, target_unit, base_size):
        """Конвертирует значение в нужную единицу"""
        if unit == 'px':
            if target_unit == 'vw':
                return (float(value) / base_width) * 100
            elif target_unit == 'vh':
                return (float(value) / base_height) * 100
        elif unit == 'rem':
            # 1rem = 16px
            px_value = float(value) * 16
            if target_unit == 'vw':
                return (px_value / base_width) * 100
            elif target_unit == 'vh':
                return (px_value / base_height) * 100
        elif unit == 'em':
            # 1em = 16px
            px_value = float(value) * 16
            if target_unit == 'vw':
                return (px_value / base_width) * 100
            elif target_unit == 'vh':
                return (px_value / base_height) * 100
        return float(value)
    
    def process_declaration(match):
        """Обрабатывает CSS декларацию"""
        property_name = match.group(1).strip()
        value = match.group(2).strip()
        
        # Пропускаем свойства, которые должны остаться в px
        if property_name in px_properties:
            return match.group(0)
        
        # Конвертируем значения
        if property_name in vh_properties:
            # Конвертируем в vh
            if 'px' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)px', 
                    lambda m: f"{convert_value(m.group(1), 'px', 'vh', base_height):.4f}vh", value)
                return f"{property_name}: {new_value}"
            elif 'rem' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)rem', 
                    lambda m: f"{convert_value(m.group(1), 'rem', 'vh', base_height):.4f}vh", value)
                return f"{property_name}: {new_value}"
            elif 'em' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)em', 
                    lambda m: f"{convert_value(m.group(1), 'em', 'vh', base_height):.4f}vh", value)
                return f"{property_name}: {new_value}"
        
        elif property_name in vw_properties:
            # Конвертируем в vw
            if 'px' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)px', 
                    lambda m: f"{convert_value(m.group(1), 'px', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
            elif 'rem' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)rem', 
                    lambda m: f"{convert_value(m.group(1), 'rem', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
            elif 'em' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)em', 
                    lambda m: f"{convert_value(m.group(1), 'em', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
        
        # Для остальных свойств конвертируем в vw
        else:
            if 'px' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)px', 
                    lambda m: f"{convert_value(m.group(1), 'px', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
            elif 'rem' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)rem', 
                    lambda m: f"{convert_value(m.group(1), 'rem', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
            elif 'em' in value:
                new_value = re.sub(r'(\d+(?:\.\d+)?)em', 
                    lambda m: f"{convert_value(m.group(1), 'em', 'vw', base_width):.4f}vw", value)
                return f"{property_name}: {new_value}"
        
        return match.group(0)
    
    # Обрабатываем CSS декларации
    pattern = r'([a-zA-Z-]+):\s*([^;]+);'
    converted_css = re.sub(pattern, process_declaration, css_content)
    
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
        
        # Статистика
        original_px = len(re.findall(r'\d+px', css_content))
        converted_vw = len(re.findall(r'\d+\.\d+vw', converted_css))
        converted_vh = len(re.findall(r'\d+\.\d+vh', converted_css))
        
        print(f"📊 Статистика:")
        print(f"   Исходных px: {original_px}")
        print(f"   Конвертировано в vw: {converted_vw}")
        print(f"   Конвертировано в vh: {converted_vh}")
        
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
    print("1. Запустите скрипт: python convert_to_vw_advanced.py")
    print("2. Получите адаптивный CSS файл: style_adaptive.css")
    print("3. Замените ссылку в HTML на новый файл")
    print("\n💡 Особенности:")
    print("- Высотные свойства конвертируются в vh")
    print("- Ширинные свойства конвертируются в vw")
    print("- Мелкие детали (border, shadow) остаются в px")
    print("- Размеры шрифтов конвертируются в vw")
