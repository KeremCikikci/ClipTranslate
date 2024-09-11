from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QLineEdit, QLabel, QSlider, QScrollArea, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QFontMetrics
from googletrans import Translator
import sys
import json

#system tema, kod temizleme, boyut kücültme, exe yapma

app = QApplication(sys.argv)

screen = app.primaryScreen()
screen_geometry = screen.geometry()
screen_width = screen_geometry.width()
screen_height = screen_geometry.height()

# COLORS
GRAY = '#282a35'
WHITE = '#ffffff'
GREEN = '#059862'

COLOR1 = ''
COLOR2 = ''
COLOR3 = ''

# WINDOW
WINDOW_MIN_WIDTH_P = None
WINDOW_MIN_HEIGHT_P = None
WINDOW_DEF_WIDTH_P = None
WINDOW_DEF_HEIGHT_P = None
WINDOW_DEF_X_P = None
WINDOW_DEF_Y_P = None

# SETTINGS WINDOW
SETTINGS_WIN_WIDTH_P = 60
SETTINGS_WIN_HEIGHT_P = 45

SETTINGS_WIN_WIDTH = int(SETTINGS_WIN_WIDTH_P / 100 * screen_width)
SETTINGS_WIN_HEIGHT = int(SETTINGS_WIN_HEIGHT_P / 100 * screen_height)

SETTINGS_HOR_MARGIN_P = .05
SETTINGS_SPACE_P = .1

# FONT
MIN_TEXT_FONT = None
FONT_DEF_SIZE = None

# LANGUAGE
DEF_SOURCE_LAN = None
DEF_TARGET_LAN = None
LAN_LIST = None

# THEME
THEME = None

# USER INTERFACE
TITLEBAR_H_P = None

TOOLBAR_H_P = None

TEXT_HOR_MARGIN_P = None

COMBO_WIDTH_P = None
COMBO_VER_MARGIN_P = None
COMBO_HOR_MARGIN_P = None

SPACE_C_B_P = None

BUTTON_VER_MARGIN_P = None
BUTTON_HOR_MARGIN_P = None

WINDOW_MIN_WIDTH = None
WINDOW_MIN_HEIGHT = None
WINDOW_DEF_WIDTH = None
WINDOW_DEF_HEIGHT = None
WINDOW_DEF_X = None
WINDOW_DEF_Y = None
TITLEBAR_H = None
TOOLBAR_H = None

translator = Translator()

def getParams():
    global WINDOW_MIN_WIDTH_P, WINDOW_MIN_HEIGHT_P, WINDOW_DEF_WIDTH_P, WINDOW_DEF_HEIGHT_P, WINDOW_DEF_X_P, WINDOW_DEF_Y_P, MIN_TEXT_FONT, FONT_DEF_SIZE, DEF_SOURCE_LAN, DEF_TARGET_LAN, LAN_LIST, THEME, TITLEBAR_H_P, TOOLBAR_H_P, TEXT_HOR_MARGIN_P, COMBO_WIDTH_P, COMBO_VER_MARGIN_P, COMBO_HOR_MARGIN_P, SPACE_C_B_P, BUTTON_VER_MARGIN_P, BUTTON_HOR_MARGIN_P, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, WINDOW_DEF_WIDTH, WINDOW_DEF_HEIGHT, WINDOW_DEF_X, WINDOW_DEF_Y, TITLEBAR_H, TOOLBAR_H
    
    with open('settings.json', 'r') as file:
        data = json.load(file)
    
    WINDOW_MIN_WIDTH_P = data["window"]["min_width"]
    WINDOW_MIN_HEIGHT_P = data["window"]["min_height"]
    WINDOW_DEF_WIDTH_P = data["window"]["def_width"]
    WINDOW_DEF_HEIGHT_P = data["window"]["def_height"]
    WINDOW_DEF_X_P = data["window"]["def_x"]
    WINDOW_DEF_Y_P = data["window"]["def_y"]
    MIN_TEXT_FONT = data["font"]["min_size"]
    FONT_DEF_SIZE = data["font"]["def_size"]
    DEF_SOURCE_LAN = data["language"]["def_source"]
    DEF_TARGET_LAN = data["language"]["def_target"]
    LAN_LIST = data["language"]["list"]
    THEME = data["theme"]["theme"]
    TITLEBAR_H_P = data["ui"]["titlebar_h"]
    TOOLBAR_H_P = data["ui"]["toolbar_h"]
    TEXT_HOR_MARGIN_P = data["ui"]["text_hor_margin"]
    COMBO_WIDTH_P = data["ui"]["combo_width"]
    COMBO_VER_MARGIN_P = data["ui"]["combo_ver_margin"]
    COMBO_HOR_MARGIN_P = data["ui"]["combo_hor_margin"]
    SPACE_C_B_P = data["ui"]["space_c_b"]
    BUTTON_VER_MARGIN_P = data["ui"]["button_ver_margin"]
    BUTTON_HOR_MARGIN_P = data["ui"]["button_hor_margin"]

    WINDOW_MIN_WIDTH = int(screen_width * WINDOW_MIN_WIDTH_P)
    WINDOW_MIN_HEIGHT = int(screen_height * WINDOW_MIN_HEIGHT_P)
    WINDOW_DEF_WIDTH = int(screen_width * WINDOW_DEF_WIDTH_P)
    WINDOW_DEF_HEIGHT = int(screen_height * WINDOW_DEF_HEIGHT_P)
    WINDOW_DEF_X = int(screen_width * WINDOW_DEF_X_P)
    WINDOW_DEF_Y = int(screen_height * WINDOW_DEF_Y_P)

    TITLEBAR_H = int(screen_height * TITLEBAR_H_P)

    TOOLBAR_H = int(screen_height * TOOLBAR_H_P)

getParams()

def setTheme(window, isSetting = False):
    if THEME == 'dark':
        pixmap = QPixmap('logo_dark.png')
        COLOR1, COLOR2, COLOR3 = GRAY, WHITE, GREEN

    if THEME == 'light':
        pixmap = QPixmap('logo_light.png')
        COLOR1, COLOR2, COLOR3 = WHITE, GRAY, GREEN

    window.setStyleSheet(f"background-color: {COLOR1}")
    scaled_pixmap = pixmap.scaledToHeight(TITLEBAR_H, Qt.SmoothTransformation)
    window.logo_image.setPixmap(scaled_pixmap)
    window.close_button.setStyleSheet(f"QPushButton {{border: none; background-color: {COLOR1}; color: {COLOR3};}} QPushButton:hover {{background-color: {COLOR3}; color: {COLOR2};}}")

    if isSetting:
        window.settings_text.setStyleSheet(f"QLabel {{color: {COLOR3}}}")
        window.window_title.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.minWidth_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.minWidth_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.minHeight_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.minHeight_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defWidth_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defWidth_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defHeight_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defHeight_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defX_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defX_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defY_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defY_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.font_title.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.minFontText_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.minFontText_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defFont_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defFont_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.lan_title.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defSourceLan_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defSourceLan_list.setStyleSheet(f"QComboBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.defTargetLan_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.defTargetLan_list.setStyleSheet(f"QComboBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.addNewLan_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.addNewLan_text.setStyleSheet(f"QLineEdit {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.addNewLan_button.setStyleSheet(f"QPushButton {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.removeLan_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.removeLan_list.setStyleSheet(f"QComboBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")        
        window.removeLan_button.setStyleSheet(f"QPushButton {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")        
        window.theme_title.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.theme_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.theme_list.setStyleSheet(f"QComboBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.UI_title.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.titleBarHeight_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.titleBarHeight_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.toolBarHeight_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.toolBarHeight_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.textHorMargin_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.textHorMargin_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.listWidth_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.listWidth_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.listVerMargin_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.listVerMargin_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.listHorMargin_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.listHorMargin_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.spaceWidth_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.spaceWidth_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.buttonHorMargin_par.setStyleSheet(f"QLabel {{color: {COLOR2}}}")
        window.buttonHorMargin_spin.setStyleSheet(f"QSpinBox {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR2}}}")
        window.setDef_button.setStyleSheet(f"QPushButton {{border: 1px solid {COLOR2}; background-color: {COLOR3}; color: {COLOR1};}} QPushButton:hover {{color: {COLOR2};}}")
    else:
        window.settings_button.setStyleSheet(f"QPushButton {{border: none; background-color: {COLOR1}; color: {COLOR3};}} QPushButton:hover {{background-color: {COLOR3};}}")
        window.label.setStyleSheet(f"color: {COLOR2}")
        window.source_lang_combo.setStyleSheet(f"QComboBox {{background-color: {COLOR3}; color: {COLOR1};}} QComboBox:hover {{color: {COLOR2};}}")
        window.target_lang_combo.setStyleSheet(f"QComboBox {{background-color: {COLOR3}; color: {COLOR1};}} QComboBox:hover {{color: {COLOR2};}}")
        window.auto_adjust_button.setStyleSheet(f"QPushButton {{background-color: {COLOR3}; color: {COLOR1};}} QPushButton:hover {{color: {COLOR2};}}")
        window.decrease_font_button.setStyleSheet(f"QPushButton {{background-color: {COLOR3}; color: {COLOR1};}} QPushButton:hover {{color: {COLOR2};}}")
        window.increase_font_button.setStyleSheet(f"QPushButton {{background-color: {COLOR3}; color: {COLOR1};}} QPushButton:hover {{color: {COLOR2};}}")
        window.lock_font_button.setStyleSheet(f"QPushButton {{background-color: {COLOR3}; color: {COLOR1};}} QPushButton:hover {{color: {COLOR2};}}")

class DraggableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resizing = False
        self.mousePos = None
        self.resizeDirection = None
        self.clipboard = QApplication.clipboard()
        self.last_text = ""
        self.clipboard.dataChanged.connect(self.onClipboardChanged)
        self.current_font_size = FONT_DEF_SIZE
        self.font_locked = False

        self.is_moving = False
        self.is_resizing = False
        self.resize_direction = None
        self.mousePos = None

        self.border_thickness = 8 

    def initUI(self):
        self.setWindowTitle('ClipTranslate')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(WINDOW_DEF_X, WINDOW_DEF_Y, WINDOW_DEF_WIDTH, WINDOW_DEF_HEIGHT)
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.setWindowIcon(QIcon("logo.png"))
        
        self.settings_button = QPushButton('⚙', self)
        self.settings_button.clicked.connect(self.openSettings)
        
        self.logo_image = QLabel(self)
        
        self.close_button = QPushButton('✕', self)
        self.close_button.clicked.connect(self.closeWindow)

        self.label = QLabel('Copy a text to translate', self)
        #self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(f"border: none")
        self.scroll_area.setWidget(self.label)

        self.source_lang_combo = QComboBox(self)
        self.source_lang_combo.addItems(['auto'] + LAN_LIST)
        self.source_lang_combo.setCurrentText(DEF_SOURCE_LAN)

        self.target_lang_combo = QComboBox(self)
        self.target_lang_combo.addItems(LAN_LIST)
        self.target_lang_combo.setCurrentText(DEF_TARGET_LAN)

        self.auto_adjust_button = QPushButton('⤢', self)
        self.auto_adjust_button.clicked.connect(self.autoAdjustFont)

        self.decrease_font_button = QPushButton('-', self)
        self.decrease_font_button.clicked.connect(self.decreaseFont)

        self.increase_font_button = QPushButton('+', self)
        self.increase_font_button.clicked.connect(self.increaseFont)

        self.lock_font_button = QPushButton('🔒', self)
        self.lock_font_button.clicked.connect(self.lockFont) 

        setTheme(self)

        self.show()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize()
        
    def resize(self):
        TEXT_HOR_MARGIN = int(self.width() * TEXT_HOR_MARGIN_P)

        COMBO_VER_MARGIN = int(TOOLBAR_H * COMBO_VER_MARGIN_P)
        COMBO_WIDTH = int(self.width() * COMBO_WIDTH_P)
        COMBO_HOR_MARGIN = int(self.width() * COMBO_HOR_MARGIN_P)

        BUTTON_VER_MARGIN = COMBO_VER_MARGIN

        SPACE_C_B = int(self.width() * SPACE_C_B_P)
        
        SB_X = 0
        SB_Y = 0
        SB_H = TITLEBAR_H
        SB_W = SB_H

        CB_H = TITLEBAR_H
        CB_W = CB_H
        CB_X = self.width() - CB_W
        CB_Y = 0

        LI_W = self.logo_image.width()
        LI_X = int(self.width() / 2 - LI_W / 3)
        LI_Y = 0

        SA_X = TEXT_HOR_MARGIN
        SA_Y = TITLEBAR_H
        SA_W = self.width() - 2 * TEXT_HOR_MARGIN
        SA_H = self.height() - TITLEBAR_H - TOOLBAR_H
        
        SL_X = COMBO_HOR_MARGIN
        SL_Y = SA_Y + SA_H + COMBO_VER_MARGIN
        SL_W = COMBO_WIDTH
        SL_H = TOOLBAR_H - 2 * COMBO_VER_MARGIN

        TL_X = SL_X + SL_W + COMBO_HOR_MARGIN
        TL_Y = SL_Y
        TL_W = SL_W
        TL_H = SL_H

        AAB_X = TL_X + TL_W + SPACE_C_B
        AAB_Y = SL_Y
        AAB_H = TOOLBAR_H - 2 * BUTTON_VER_MARGIN
        AAB_W = AAB_H

        DFB_X = AAB_X + AAB_W + BUTTON_VER_MARGIN
        DFB_Y = SL_Y
        DFB_H = AAB_H
        DFB_W = DFB_H
        
        IFB_X = DFB_X + DFB_W + BUTTON_VER_MARGIN
        IFB_Y = SL_Y
        IFB_H = AAB_H
        IFB_W = IFB_H

        LFB_X = IFB_X + IFB_W + BUTTON_VER_MARGIN
        LFB_Y = SL_Y
        LFB_H = AAB_H
        LFB_W = LFB_H

        UI_W_SUM = (LFB_X + LFB_W) * 100 / self.width()
        
        if UI_W_SUM > 100:
            print("UI DOES NOT FIT IN THE WINDOW")
    	
        self.settings_button.setGeometry(SB_X, SB_Y, SB_W, SB_H)
        self.logo_image.move(LI_X, LI_Y)
        self.close_button.setGeometry(CB_X, CB_Y, CB_W, CB_H)

        self.scroll_area.setGeometry(SA_X, SA_Y, SA_W, SA_H)
        self.source_lang_combo.setGeometry(SL_X, SL_Y, SL_W, SL_H)
        self.target_lang_combo.setGeometry(TL_X, TL_Y, TL_W, TL_H)

        self.auto_adjust_button.setGeometry(AAB_X, AAB_Y, AAB_W, AAB_H)
        self.decrease_font_button.setGeometry(DFB_X, DFB_Y, DFB_W, DFB_H)
        self.increase_font_button.setGeometry(IFB_X, IFB_Y, IFB_W, IFB_H)
        self.lock_font_button.setGeometry(LFB_X, LFB_Y, LFB_W, LFB_H)

        #if not self.font_locked:
        self.autoAdjustFont()

    def closeWindow(self):
        if hasattr(self, 'settings_window') and self.settings_window is not None:
            self.settings_window.close()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Pencereyi taşımak için
            if not self.is_resizing:
                self.is_moving = True
                self.offset = event.pos()

            # Pencereyi yeniden boyutlandırmak için
            self.mousePos = event.globalPos()
            self.resize_direction = self.getResizeDirection(event.pos())

    def mouseMoveEvent(self, event):
        # Fare kenarlık üzerindeyken imleci değiştirmek
        self.updateCursorShape(event.pos())

        # Pencereyi taşımak için
        if self.is_moving and not self.is_resizing:
            self.move(event.globalPos() - self.offset)

        # Pencereyi yeniden boyutlandırmak için
        if self.is_resizing:
            delta = event.globalPos() - self.mousePos
            self.mousePos = event.globalPos()
            rect = self.geometry()

            if self.resize_direction == 'right':
                rect.setRight(rect.right() + delta.x())
            elif self.resize_direction == 'bottom':
                rect.setBottom(rect.bottom() + delta.y())
            elif self.resize_direction == 'left':
                rect.setLeft(rect.left() + delta.x())
            elif self.resize_direction == 'top':
                rect.setTop(rect.top() + delta.y())
            elif self.resize_direction == 'bottom-right':
                rect.setRight(rect.right() + delta.x())
                rect.setBottom(rect.bottom() + delta.y())
            elif self.resize_direction == 'bottom-left':
                rect.setLeft(rect.left() + delta.x())
                rect.setBottom(rect.bottom() + delta.y())
            elif self.resize_direction == 'top-right':
                rect.setRight(rect.right() + delta.x())
                rect.setTop(rect.top() + delta.y())
            elif self.resize_direction == 'top-left':
                rect.setLeft(rect.left() + delta.x())
                rect.setTop(rect.top() + delta.y())

            self.setGeometry(rect)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_moving = False
            self.is_resizing = False
            self.resize_direction = None

    def getResizeDirection(self, pos):
        """Fare pozisyonuna göre genişletme yönünü belirle"""
        rect = self.rect()
        if pos.x() >= rect.width() - self.border_thickness and pos.y() >= rect.height() - self.border_thickness:
            self.is_resizing = True
            return 'bottom-right'
        elif pos.x() <= self.border_thickness and pos.y() >= rect.height() - self.border_thickness:
            self.is_resizing = True
            return 'bottom-left'
        elif pos.x() >= rect.width() - self.border_thickness and pos.y() <= self.border_thickness:
            self.is_resizing = True
            return 'top-right'
        elif pos.x() <= self.border_thickness and pos.y() <= self.border_thickness:
            self.is_resizing = True
            return 'top-left'
        elif pos.x() >= rect.width() - self.border_thickness:
            self.is_resizing = True
            return 'right'
        elif pos.x() <= self.border_thickness:
            self.is_resizing = True
            return 'left'
        elif pos.y() >= rect.height() - self.border_thickness:
            self.is_resizing = True
            return 'bottom'
        elif pos.y() <= self.border_thickness:
            self.is_resizing = True
            return 'top'
        return None

    def updateCursorShape(self, pos):
        """Fare imlecini genişletme alanına göre değiştir"""
        direction = self.getResizeDirection(pos)
        if direction in ['top-left', 'bottom-right']:
            self.setCursor(Qt.SizeFDiagCursor)
        elif direction in ['top-right', 'bottom-left']:
            self.setCursor(Qt.SizeBDiagCursor)
        elif direction in ['left', 'right']:
            self.setCursor(Qt.SizeHorCursor)
        elif direction in ['top', 'bottom']:
            self.setCursor(Qt.SizeVerCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def onClipboardChanged(self):
        new_text = self.clipboard.text()
        if new_text != self.last_text:
            self.last_text = new_text
            single_line_text = (new_text.replace('\n', ' ').replace('\r', ' ')).strip()

            source_lang = self.source_lang_combo.currentText()
            target_lang = self.target_lang_combo.currentText()

            translate = ""
            try:
                translate = translator.translate(single_line_text, src=source_lang, dest=target_lang).text
            except:
                pass

            if translate != "":
                self.label.setText(translate)
                if not self.font_locked:
                    self.autoAdjustFont()

    def autoAdjustFont(self):
        self.font_locked = False

        widget_width = self.scroll_area.width()
        widget_height = self.scroll_area.height()
        text = self.label.text()

        new_font_size = max(MIN_TEXT_FONT, widget_width // 25)
        font = QFont('Arial', new_font_size)

        self.label.setFont(font)

        while self.label.fontMetrics().boundingRect(0, 0, widget_width, widget_height, Qt.TextWordWrap, text).height() > widget_height:
            new_font_size -= 1
            font.setPointSize(new_font_size)
            self.label.setFont(font)
            if new_font_size <= MIN_TEXT_FONT:
                break

        self.current_font_size = new_font_size

    def decreaseFont(self):
        if self.current_font_size > MIN_TEXT_FONT:
            self.current_font_size -= 1
            self.label.setFont(QFont('Arial', self.current_font_size))
            self.font_locked = False

    def increaseFont(self):
        self.current_font_size += 1
        self.label.setFont(QFont('Arial', self.current_font_size))
        self.font_locked = False

    def lockFont(self):
        self.font_locked = True

    def openSettings(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    
class SettingsWindow(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.initUI()
        setTheme(self, isSetting=True)
        self.widget = widget

    def initUI(self):
        CB_H = TITLEBAR_H
        CB_W = CB_H
        CB_X = SETTINGS_WIN_WIDTH - CB_W
        CB_Y = 0

        self.setWindowTitle('Settings')
        self.setGeometry(int((screen_width - SETTINGS_WIN_WIDTH) / 2), int((screen_height - SETTINGS_WIN_HEIGHT) / 2), SETTINGS_WIN_WIDTH, SETTINGS_WIN_HEIGHT)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        self.settings_text = QLabel('SETTINGS', self)
        adjustFontToHeight(self.settings_text, CB_H, isBold = True)
        self.logo_image = QLabel(self)
        LI_W = self.logo_image.width()
        LI_X = int(self.width() / 2 - LI_W / 3)
        LI_Y = 0
        self.logo_image.move(LI_X, LI_Y)

        self.close_button = QPushButton('✕', self)
        self.close_button.setGeometry(CB_X, CB_Y, CB_W, CB_H)
        self.close_button.clicked.connect(self.closeWindow)


        SETTINGS_HOR_MARGIN = int(self.width() * SETTINGS_HOR_MARGIN_P)
        SETTINGS_SPACE = int(self.width() * SETTINGS_SPACE_P)

        AREA_Y, AREA_H = TITLEBAR_H, self.height() - TITLEBAR_H
        
        ROW_W = int((SETTINGS_WIN_WIDTH - SETTINGS_SPACE) / 2 - SETTINGS_HOR_MARGIN)
        ROW_H = int(AREA_H / 15)

        ### LEFT ###

        # WINDOW
        self.window_title = QLabel("WINDOW", self)
        adjustFontToHeight(self.window_title, ROW_H, isBold = True)
        self.window_title.move(int(SETTINGS_HOR_MARGIN + (ROW_W - self.window_title.width()) / 2), AREA_Y + ROW_H * 0)

        self.minWidth_par = QLabel("Min. Width: ", self)
        adjustFontToHeight(self.minWidth_par, ROW_H * .8)
        adjustLabelWidth(self.minWidth_par)
        self.minWidth_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 1)
        
        self.minWidth_spin = QSpinBox(self)
        self.minWidth_spin.setMinimum(0)
        self.minWidth_spin.setMaximum(100)
        self.minWidth_spin.setValue(WINDOW_MIN_WIDTH_P * 100)
        self.minWidth_spin.setSingleStep(5)
        self.minWidth_spin.valueChanged.connect(self.setParams)
        self.minWidth_spin.setGeometry(self.minWidth_par.x() + self.minWidth_par.width(), self.minWidth_par.y(), ROW_W - self.minWidth_par.width(), int(ROW_H * .9))

        self.minHeight_par = QLabel("Min. Height: ", self)
        adjustFontToHeight(self.minHeight_par, ROW_H * .8)
        adjustLabelWidth(self.minHeight_par)
        self.minHeight_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 2)

        self.minHeight_spin = QSpinBox(self)
        self.minHeight_spin.setMinimum(0)
        self.minHeight_spin.setMaximum(100)
        self.minHeight_spin.setValue(WINDOW_MIN_HEIGHT_P * 100)
        self.minHeight_spin.setSingleStep(5)
        self.minHeight_spin.valueChanged.connect(self.setParams)
        self.minHeight_spin.setGeometry(self.minHeight_par.x() + self.minHeight_par.width(), self.minHeight_par.y(), ROW_W - self.minHeight_par.width(), int(ROW_H * .9))

        self.defWidth_par = QLabel("Def. Width: ", self)
        adjustFontToHeight(self.defWidth_par, ROW_H * .8)
        adjustLabelWidth(self.defWidth_par)
        self.defWidth_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 3)

        self.defWidth_spin = QSpinBox(self)
        self.defWidth_spin.setMinimum(0)
        self.defWidth_spin.setMaximum(100)
        self.defWidth_spin.setValue(WINDOW_DEF_WIDTH_P * 100)
        self.defWidth_spin.setSingleStep(5)
        self.defWidth_spin.valueChanged.connect(self.setParams)
        self.defWidth_spin.setGeometry(self.defWidth_par.x() + self.defWidth_par.width(), self.defWidth_par.y(), ROW_W - self.defWidth_par.width(), int(ROW_H * .9))

        self.defHeight_par = QLabel("Def. Height: ", self)
        adjustFontToHeight(self.defHeight_par, ROW_H * .8)
        adjustLabelWidth(self.defHeight_par)
        self.defHeight_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 4)

        self.defHeight_spin = QSpinBox(self)
        self.defHeight_spin.setMinimum(1)
        self.defHeight_spin.setMaximum(100)
        self.defHeight_spin.setValue(WINDOW_DEF_HEIGHT_P * 100)
        self.defHeight_spin.setSingleStep(5)
        self.defHeight_spin.valueChanged.connect(self.setParams)
        self.defHeight_spin.setGeometry(self.defHeight_par.x() + self.defHeight_par.width(), self.defHeight_par.y(), ROW_W - self.defHeight_par.width(), int(ROW_H * .9))

        self.defX_par = QLabel("Def. X: ", self)
        adjustFontToHeight(self.defX_par, ROW_H * .8)
        adjustLabelWidth(self.defX_par)
        self.defX_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 5)
        
        self.defX_spin = QSpinBox(self)
        self.defX_spin.setMinimum(1)
        self.defX_spin.setMaximum(100)
        self.defX_spin.setValue(WINDOW_DEF_X_P * 100)
        self.defX_spin.setSingleStep(5)
        self.defX_spin.valueChanged.connect(self.setParams)
        self.defX_spin.setGeometry(self.defX_par.x() + self.defX_par.width(), self.defX_par.y(), ROW_W - self.defX_par.width(), int(ROW_H * .9))

        self.defY_par = QLabel("Def. Y: ", self)
        adjustFontToHeight(self.defY_par, ROW_H * .8)
        adjustLabelWidth(self.defY_par)
        self.defY_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 6)

        self.defY_spin = QSpinBox(self)
        self.defY_spin.setMinimum(1)
        self.defY_spin.setMaximum(100)
        self.defY_spin.setValue(WINDOW_DEF_Y_P * 100)
        self.defY_spin.setSingleStep(5)
        self.defY_spin.valueChanged.connect(self.setParams)
        self.defY_spin.setGeometry(self.defY_par.x() + self.defY_par.width(), self.defY_par.y(), ROW_W - self.defY_par.width(), int(ROW_H * .9))

        # FONT
        self.font_title = QLabel("FONT", self)
        adjustFontToHeight(self.font_title, ROW_H, isBold = True)
        self.font_title.move(int(SETTINGS_HOR_MARGIN + (ROW_W - self.font_title.width()) / 2), AREA_Y + ROW_H * 7)

        self.minFontText_par = QLabel("Min. Font: ", self)
        adjustFontToHeight(self.minFontText_par, ROW_H * .8)
        adjustLabelWidth(self.minFontText_par)
        self.minFontText_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 8)

        self.minFontText_spin = QSpinBox(self)
        self.minFontText_spin.setMinimum(1)
        self.minFontText_spin.setMaximum(100)
        self.minFontText_spin.setValue(MIN_TEXT_FONT)
        self.minFontText_spin.setSingleStep(1)
        self.minFontText_spin.valueChanged.connect(self.setParams)
        self.minFontText_spin.setGeometry(self.minFontText_par.x() + self.minFontText_par.width(), self.minFontText_par.y(), ROW_W - self.minFontText_par.width(), int(ROW_H * .9))

        self.defFont_par = QLabel("Def. Font:", self)
        adjustFontToHeight(self.defFont_par, ROW_H * .8)
        self.defFont_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 9)

        self.defFont_spin = QSpinBox(self)
        self.defFont_spin.setMinimum(1)
        self.defFont_spin.setMaximum(100)
        self.defFont_spin.setValue(FONT_DEF_SIZE)
        self.defFont_spin.setSingleStep(1)
        self.defFont_spin.valueChanged.connect(self.setParams)
        self.defFont_spin.setGeometry(self.defFont_par.x() + self.defFont_par.width(), self.defFont_par.y(), ROW_W - self.defFont_par.width(), int(ROW_H * .9))

        # LANGUAGE
        self.lan_title = QLabel("LANGUAGE", self)
        adjustFontToHeight(self.lan_title, ROW_H, isBold = True)
        self.lan_title.move(int(SETTINGS_HOR_MARGIN + (ROW_W - self.font_title.width()) / 2), AREA_Y + ROW_H * 10)

        self.defSourceLan_par = QLabel("Def. Source Lan: ", self)
        adjustFontToHeight(self.defSourceLan_par, ROW_H * .8)
        adjustLabelWidth(self.defSourceLan_par)
        self.defSourceLan_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 11)

        self.defSourceLan_list = QComboBox(self)
        self.defSourceLan_list.addItems(LAN_LIST)
        self.defSourceLan_list.setGeometry(int(self.defSourceLan_par.x() + self.defSourceLan_par.width()), self.defSourceLan_par.y(), ROW_W - self.defSourceLan_par.width(), int(ROW_H * .9))
        self.defSourceLan_list.setCurrentText(DEF_SOURCE_LAN)
        self.defSourceLan_list.currentIndexChanged.connect(self.setParams)

        self.defTargetLan_par = QLabel("Def. Target Lan: ", self)
        adjustFontToHeight(self.defTargetLan_par, ROW_H * .8)
        adjustLabelWidth(self.defTargetLan_par)
        self.defTargetLan_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 12)

        self.defTargetLan_list = QComboBox(self)
        self.defTargetLan_list.addItems(LAN_LIST)
        self.defTargetLan_list.setGeometry(int(self.defTargetLan_par.x() + self.defTargetLan_par.width()), self.defTargetLan_par.y(), ROW_W - self.defTargetLan_par.width(), int(ROW_H * .9))
        self.defTargetLan_list.setCurrentText(DEF_TARGET_LAN)
        self.defTargetLan_list.currentIndexChanged.connect(self.setParams)

        self.addNewLan_par = QLabel("Add New Lan: ", self)
        adjustFontToHeight(self.addNewLan_par, ROW_H * .8)
        adjustLabelWidth(self.addNewLan_par)
        self.addNewLan_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 13)

        self.addNewLan_button = QPushButton("✔", self)
        self.addNewLan_button.clicked.connect(self.addNewLan)
        self.addNewLan_button.setGeometry(self.addNewLan_par.x() + ROW_W - int(ROW_H * .9), self.addNewLan_par.y(), int(ROW_H * .9), int(ROW_H * .9))

        self.addNewLan_text = QLineEdit(self)
        self.addNewLan_text.setPlaceholderText("New Lan")
        self.addNewLan_text.setGeometry(int(self.addNewLan_par.x() + self.addNewLan_par.width()), self.addNewLan_par.y(), ROW_W - self.addNewLan_par.width() - self.addNewLan_button.width(), int(ROW_H * .9))
        
        self.removeLan_par = QLabel("Remove Lan: ", self)
        adjustFontToHeight(self.removeLan_par, ROW_H * .8)
        adjustLabelWidth(self.removeLan_par)
        self.removeLan_par.move(SETTINGS_HOR_MARGIN, AREA_Y + ROW_H * 14)

        self.removeLan_button = QPushButton("✕", self)
        self.removeLan_button.clicked.connect(self.removeLan)
        self.removeLan_button.setGeometry(self.removeLan_par.x() + ROW_W - int(ROW_H * .9), self.removeLan_par.y(), int(ROW_H * .9), int(ROW_H * .9))

        self.removeLan_list = QComboBox(self)
        self.removeLan_list.addItems(LAN_LIST)
        self.removeLan_list.setGeometry(int(self.removeLan_par.x() + self.removeLan_par.width()), self.removeLan_par.y(), ROW_W - self.removeLan_par.width() - self.removeLan_button.width(), int(ROW_H * .9))

        ### RIGHT ###
        self.theme_title = QLabel("THEME", self)
        adjustFontToHeight(self.theme_title, ROW_H, isBold = True)
        self.theme_title.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE + (ROW_W - self.theme_title.width()) / 2), AREA_Y + ROW_H * 0)
        
        self.theme_par = QLabel("Thema: ", self)
        adjustFontToHeight(self.theme_par, ROW_H * .8)
        adjustLabelWidth(self.theme_par)
        self.theme_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 1)

        self.theme_list = QComboBox(self)
        self.theme_list.addItems(['dark', 'light', 'system'])
        self.theme_list.setGeometry(self.theme_par.x() + self.theme_par.width(), self.theme_par.y(), ROW_W - self.theme_par.width(), ROW_H)
        self.theme_list.setCurrentText(THEME)
        self.theme_list.currentIndexChanged.connect(self.setParams)

        self.UI_title = QLabel("USER INTERFACE", self)
        adjustFontToHeight(self.UI_title, ROW_H, isBold = True)
        adjustLabelWidth(self.UI_title)
        self.UI_title.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE + (ROW_W - self.UI_title.width()) / 2), AREA_Y + ROW_H * 2)

        self.titleBarHeight_par = QLabel("Titlebar Height:", self)
        adjustFontToHeight(self.titleBarHeight_par, ROW_H * .8)
        adjustLabelWidth(self.titleBarHeight_par)
        self.titleBarHeight_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 3)

        self.titleBarHeight_spin = QSpinBox(self)
        self.titleBarHeight_spin.setMinimum(1)
        self.titleBarHeight_spin.setMaximum(100)
        self.titleBarHeight_spin.setValue(TITLEBAR_H_P * 100)
        self.titleBarHeight_spin.setSingleStep(5)
        self.titleBarHeight_spin.valueChanged.connect(self.setParams)
        self.titleBarHeight_spin.setGeometry(self.titleBarHeight_par.x() + self.titleBarHeight_par.width(), self.titleBarHeight_par.y(), ROW_W - self.titleBarHeight_par.width(), int(ROW_H * .9))

        self.toolBarHeight_par = QLabel("Toolbar Height:", self)
        adjustFontToHeight(self.toolBarHeight_par, ROW_H * .8)
        adjustLabelWidth(self.toolBarHeight_par)
        self.toolBarHeight_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 4)

        self.toolBarHeight_spin = QSpinBox(self)
        self.toolBarHeight_spin.setMinimum(1)
        self.toolBarHeight_spin.setMaximum(100)
        self.toolBarHeight_spin.setValue(TOOLBAR_H_P * 100)
        self.toolBarHeight_spin.setSingleStep(5)
        self.toolBarHeight_spin.valueChanged.connect(self.setParams)
        self.toolBarHeight_spin.setGeometry(self.toolBarHeight_par.x() + self.toolBarHeight_par.width(), self.toolBarHeight_par.y(), ROW_W - self.toolBarHeight_par.width(), int(ROW_H * .9))

        self.textHorMargin_par = QLabel("Text Hor. Mar:", self)
        adjustFontToHeight(self.textHorMargin_par, ROW_H * .8)
        adjustLabelWidth(self.textHorMargin_par)
        self.textHorMargin_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 5)

        self.textHorMargin_spin = QSpinBox(self)
        self.textHorMargin_spin.setMinimum(0)
        self.textHorMargin_spin.setMaximum(100)
        self.textHorMargin_spin.setValue(TEXT_HOR_MARGIN_P * 100)
        self.textHorMargin_spin.setSingleStep(5)
        self.textHorMargin_spin.valueChanged.connect(self.setParams)
        self.textHorMargin_spin.setGeometry(self.textHorMargin_par.x() + self.textHorMargin_par.width(), self.textHorMargin_par.y(), ROW_W - self.textHorMargin_par.width(), int(ROW_H * .9))
        
        self.listWidth_par = QLabel("List Width:", self)
        adjustFontToHeight(self.listWidth_par, ROW_H * .8)
        adjustLabelWidth(self.listWidth_par)
        self.listWidth_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 6)

        self.listWidth_spin = QSpinBox(self)
        self.listWidth_spin.setMinimum(1)
        self.listWidth_spin.setMaximum(100)
        self.listWidth_spin.setValue(COMBO_WIDTH_P * 100)
        self.listWidth_spin.setSingleStep(5)
        self.listWidth_spin.valueChanged.connect(self.setParams)
        self.listWidth_spin.setGeometry(self.listWidth_par.x() + self.listWidth_par.width(), self.listWidth_par.y(), ROW_W - self.listWidth_par.width(), int(ROW_H * .9))

        self.listVerMargin_par = QLabel("List Ver. Mar:", self)
        adjustFontToHeight(self.listVerMargin_par, ROW_H * .8)
        adjustLabelWidth(self.listVerMargin_par)
        self.listVerMargin_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 7)

        self.listVerMargin_spin = QSpinBox(self)
        self.listVerMargin_spin.setMinimum(1)
        self.listVerMargin_spin.setMaximum(100)
        self.listVerMargin_spin.setValue(COMBO_VER_MARGIN_P * 100)
        self.listVerMargin_spin.setSingleStep(5)
        self.listVerMargin_spin.valueChanged.connect(self.setParams)
        self.listVerMargin_spin.setGeometry(self.listVerMargin_par.x() + self.listVerMargin_par.width(), self.listVerMargin_par.y(), ROW_W - self.listVerMargin_par.width(), int(ROW_H * .9))

        self.listHorMargin_par = QLabel("List Hor. Mar:", self)
        adjustFontToHeight(self.listHorMargin_par, ROW_H * .8)
        adjustLabelWidth(self.listHorMargin_par)
        self.listHorMargin_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 8)

        self.listHorMargin_spin = QSpinBox(self)
        self.listHorMargin_spin.setMinimum(1)
        self.listHorMargin_spin.setMaximum(100)
        self.listHorMargin_spin.setValue(COMBO_HOR_MARGIN_P)
        self.listHorMargin_spin.setSingleStep(5)
        self.listHorMargin_spin.valueChanged.connect(self.setParams)
        self.listHorMargin_spin.setGeometry(self.listHorMargin_par.x() + self.listHorMargin_par.width(), self.listHorMargin_par.y(), ROW_W - self.listHorMargin_par.width(), int(ROW_H * .9))

        self.spaceWidth_par = QLabel("Space Width:", self)
        adjustFontToHeight(self.spaceWidth_par, ROW_H * .8)
        adjustLabelWidth(self.spaceWidth_par)
        self.spaceWidth_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 9)

        self.spaceWidth_spin = QSpinBox(self)
        self.spaceWidth_spin.setMinimum(1)
        self.spaceWidth_spin.setMaximum(100)
        self.spaceWidth_spin.setValue(SPACE_C_B_P * 100)
        self.spaceWidth_spin.setSingleStep(5)
        self.spaceWidth_spin.valueChanged.connect(self.setParams)
        self.spaceWidth_spin.setGeometry(self.spaceWidth_par.x() + self.spaceWidth_par.width(), self.spaceWidth_par.y(), ROW_W - self.spaceWidth_par.width(), int(ROW_H * .9))

        self.buttonHorMargin_par = QLabel("Button Hor. Mar:", self)
        adjustFontToHeight(self.buttonHorMargin_par, ROW_H * .8)
        adjustLabelWidth(self.buttonHorMargin_par)
        self.buttonHorMargin_par.move(int(SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 10)

        self.buttonHorMargin_spin = QSpinBox(self)
        self.buttonHorMargin_spin.setMinimum(1)
        self.buttonHorMargin_spin.setMaximum(100)
        self.buttonHorMargin_spin.setValue(BUTTON_HOR_MARGIN_P * 100)
        self.buttonHorMargin_spin.setSingleStep(5)
        self.buttonHorMargin_spin.valueChanged.connect(self.setParams)
        self.buttonHorMargin_spin.setGeometry(self.buttonHorMargin_par.x() + self.buttonHorMargin_par.width(), self.buttonHorMargin_par.y(), ROW_W - self.buttonHorMargin_par.width(), int(ROW_H * .9))

        self.setDef_button = QPushButton("DEF PARAMS", self)
        adjustFontToHeight(self.setDef_button, ROW_H * .8)
        self.setDef_button.setGeometry(int(30 + SETTINGS_HOR_MARGIN + ROW_W + SETTINGS_SPACE), AREA_Y + ROW_H * 14, ROW_W - 30, ROW_H)
        self.setDef_button.clicked.connect(self.setDef)
    
    def setParams(self):
        global WINDOW_MIN_WIDTH_P, WINDOW_MIN_HEIGHT_P, WINDOW_DEF_WIDTH_P, WINDOW_DEF_HEIGHT_P, WINDOW_DEF_X_P, WINDOW_DEF_Y_P, MIN_TEXT_FONT, FONT_DEF_SIZE, DEF_SOURCE_LAN, DEF_TARGET_LAN, LAN_LIST, THEME, TITLEBAR_H_P, TOOLBAR_H_P, TEXT_HOR_MARGIN_P, COMBO_WIDTH_P, COMBO_VER_MARGIN_P, COMBO_HOR_MARGIN_P, SPACE_C_B_P, BUTTON_VER_MARGIN_P, BUTTON_HOR_MARGIN_P, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT, WINDOW_DEF_WIDTH, WINDOW_DEF_HEIGHT, WINDOW_DEF_X, WINDOW_DEF_Y, TITLEBAR_H, TOOLBAR_H
        
        THEME = self.theme_list.currentText()

        with open('settings.json', 'r') as file:
            data = json.load(file)

        data["window"]["min_width"] = self.minWidth_spin.value() / 100
        data["window"]["min_height"] = self.minHeight_spin.value() / 100
        data["window"]["def_width"] = self.defWidth_spin.value() / 100
        data["window"]["def_height"] = self.defHeight_spin.value() / 100
        data["window"]["def_x"] = self.defX_spin.value() / 100
        data["window"]["def_y"] = self.defY_spin.value() / 100
        data["font"]["min_size"] = self.minFontText_spin.value()
        data["font"]["def_size"] = self.defFont_spin.value()
        data["language"]["def_source"] = self.defSourceLan_list.currentText()
        data["language"]["def_target"] = self.defTargetLan_list.currentText()
        data["language"]["list"] = LAN_LIST
        data["theme"]["theme"] = THEME
        data["ui"]["titlebar_h"] = self.titleBarHeight_spin.value() / 100
        data["ui"]["toolbar_h"] = self.toolBarHeight_spin.value() / 100 + .005
        data["ui"]["text_hor_margin"] = self.textHorMargin_spin.value() / 100
        data["ui"]["combo_width"] = self.listWidth_spin.value() / 100
        data["ui"]["combo_ver_margin"] = self.listVerMargin_spin.value() / 100
        data["ui"]["combo_hor_margin"] = self.listHorMargin_spin.value() / 100
        data["ui"]["space_c_b"] = self.spaceWidth_spin.value() / 100
        data["ui"]["button_ver_margin"] = self.buttonHorMargin_spin.value() / 100
        data["ui"]["button_hor_margin"] = self.buttonHorMargin_spin.value() / 100

        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)

        getParams()
        setTheme(self.widget)
        setTheme(self, isSetting=True)
        self.widget.resize()
    
    def closeWindow(self):
        self.close()  

    def setDef(self):
        with open("defSettings.json", 'r') as src:
            with open("settings.json", 'w') as dst:
                dst.write(src.read())
        
        getParams()
        self.initUI()
    
    def removeLan(self):
        LAN_LIST.remove(self.removeLan_list.currentText())

        with open('settings.json', 'r') as file:
            data = json.load(file)

        data["language"]["list"] = LAN_LIST

        with open('settings.json', 'w') as file:
            json.dump(data, file, indent=4)

        getParams()
        self.initUI()

    def addNewLan(self):
        if len(self.addNewLan_text.text()) >= 2:
            with open('settings.json', 'r') as file:
                data = json.load(file)

            LAN_LIST.append(self.addNewLan_text.text())
            data["language"]["list"] = LAN_LIST

            with open('settings.json', 'w') as file:
                json.dump(data, file, indent=4)

            getParams()
            self.initUI()


def adjustFontToHeight(label, target_height, isBold = False):
        font_size = 8
        font = QFont('Arial', font_size)
        font.setBold(isBold)

        metrics = QFontMetrics(font)
        text_height = metrics.height()

        while text_height < target_height:
            font_size += 1
            font.setPointSize(font_size)
            metrics = QFontMetrics(font)
            text_height = metrics.height()

        label.setFont(font)

def adjustLabelWidth(label):
    font_metrics = label.fontMetrics()
    text_width = font_metrics.horizontalAdvance(label.text())

    label.setFixedWidth(text_width)
        
if __name__ == '__main__':
    ex = DraggableWidget()
    sys.exit(app.exec_())