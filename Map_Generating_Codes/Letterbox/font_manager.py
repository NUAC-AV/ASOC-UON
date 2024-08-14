class FontManager:
    header_font = '<strong style="font-size: 18pt; color: {color};">'  # For larger header fonts
    subheader_font = '<strong style="font-size: 16pt; color: {color};">'  # For subheader fonts
    label_font = '<strong><span style="font-size: 18px; color: {color};">'  # For smaller label fonts
    end_strong = '</strong>'
    end_span_strong = '</span></strong>'
    
    collapse_all_label = '<span style="font-size: 14px; color: {color};">Collapse all</span>'
    expand_all_label = '<span style="font-size: 14px; color: {color};">Expand all</span>'
    
    @staticmethod
    def get_header_font(text, color='black'):
        return f'{FontManager.header_font.format(color=color)}{text}{FontManager.end_strong}'
    
    @staticmethod
    def get_subheader_font(text, color='black'):
        return f'{FontManager.subheader_font.format(color=color)}{text}{FontManager.end_strong}'
    
    @staticmethod
    def get_label_font(text, color='black'):
        return f'{FontManager.label_font.format(color=color)}{text}{FontManager.end_span_strong}'
    
    @staticmethod
    def get_closed_symbol(symbol='&#9654;', color='black', size='18px'):
        return f'<span style="font-size: {size}; color: {color};">{symbol}</span>'
    
    @staticmethod
    def get_opened_symbol(symbol='&#9662;', color='black', size='18px'):
        return f'<span style="font-size: {size}; color: {color};">{symbol}</span>'
    
    @staticmethod
    def get_collapse_all_label(color='black'):
        return FontManager.collapse_all_label.format(color=color)
    
    @staticmethod
    def get_expand_all_label(color='black'):
        return FontManager.expand_all_label.format(color=color)
