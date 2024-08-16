from typing import Optional

class FontManager:
    header_font: str = '<strong style="font-size: 14pt; color: {color};">'  # For larger header fonts
    subheader_font: str = '<strong style="font-size: 14pt; color: {color};">'  # For subheader fonts
    label_font: str = '<strong><span style="font-size: 14px; color: {color};">'  # For smaller label fonts
    end_strong: str = '</strong>'
    end_span_strong: str = '</span></strong>'
    
    collapse_all_label: str = "<span style='font-size: 14px; color: {color};'>Collapse all</span>"
    expand_all_label: str = "<span style='font-size: 14px; color: {color};'>Expand all</span>"
    
    @staticmethod
    def get_header_font(text: str, color: str = 'black') -> str:
        """Return formatted header font."""
        return f'{FontManager.header_font.format(color=color)}{text}{FontManager.end_strong}'
    
    @staticmethod
    def get_subheader_font(text: str, color: str = 'black') -> str:
        """Return formatted subheader font."""
        return f'{FontManager.subheader_font.format(color=color)}{text}{FontManager.end_strong}'
    
    @staticmethod
    def get_label_font(text: str, color: str = 'black') -> str:
        """Return formatted label font."""
        return f'{FontManager.label_font.format(color=color)}{text}{FontManager.end_span_strong}'
    
    @staticmethod
    def get_closed_symbol(symbol: str = '&#x25B6;', color: str = 'red', size: str = '20px') -> str:
        """Return formatted closed symbol (right triangle)."""
        return f"<span style='font-size: {size}; color: {color};'>{symbol}</span>"

    @staticmethod
    def get_opened_symbol(symbol: str = '&#x25BC;', color: str = 'green', size: str = '20px') -> str:
        """Return formatted opened symbol (down triangle)."""
        return f"<span style='font-size: {size}; color: {color};'>{symbol}</span>"

    @staticmethod
    def get_collapse_all_label(color: str = 'red') -> str:
        """Return formatted 'Collapse all' label."""
        return FontManager.collapse_all_label.format(color=color)
    
    @staticmethod
    def get_expand_all_label(color: str = 'green') -> str:
        """Return formatted 'Expand all' label."""
        return FontManager.expand_all_label.format(color=color)

