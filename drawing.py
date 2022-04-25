import numpy as np
import cv2

# 480x640x3 méretű Numpy tömb létrehozása RGB színes képnek
img = np.ndarray((480, 640, 3), np.uint8)

# Vonalvastagság
line_thickness = 10
min_line_thickness = 5
max_line_thickness = 100
line_thickness_extent = 5

# Vonal színe
line_color = (0, 0, 255)

# Rajzolási kezdőpont x és y
start_point_x = None
start_point_y = None

# Rajzoljon vagy sem (kattintásra fog csak rajzolni)
drawing = False

# Lehetséges vonal színek
line_color_blue = (255, 0, 0)
line_color_green = (0, 255, 0)
line_color_red = (0, 0, 255)
line_color_white = (255, 255, 255)
line_color_black = (0, 0, 0)


def mouse_draw(event, x, y, flags, param):
    global img
    global line_color
    global line_thickness
    global start_point_x
    global start_point_y
    global drawing

    # Bal kattintás -> rajzolás kezdése
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point_x = x
        start_point_y = y

    # Egér mozgatása
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (start_point_x, start_point_y), (x, y), line_color, line_thickness)
            start_point_x = x
            start_point_y = y



    # Bal kattintás felengedése
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (start_point_x, start_point_y), (x, y), line_color, line_thickness)



# Feltöltés ([255, 255, 255]) (fehér) színnel BGR
color_BGR = (255, 255, 255)
color = tuple(reversed(color_BGR))
img[:] = color

cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_draw)

while (1):
    cv2.imshow('image', img)
    pressed_key = cv2.waitKey(1)

    # Piros színű vonal 'r' gomb megnyomásával
    if pressed_key == 114:
        line_color = line_color_red

    # Zöld színű vonal 'g' gomb megnyomásával
    elif pressed_key == 103:
        line_color = line_color_green

    # Fekete színű vonal 'b' gomb megnyomásával
    elif pressed_key == 98:
        line_color = line_color_black

    # Fehér színű vonal 'w' gomb megnyomásával
    elif pressed_key == 119:
        line_color = line_color_white

    # Kék színű vonal 'k' gomb megnyomásával
    elif pressed_key == 107:
        line_color = line_color_blue

    # Vonalvastagság nagyítása '+' gomb megnyomásával
    elif pressed_key == 43:
        if line_thickness < max_line_thickness:
            line_thickness = line_thickness + line_thickness_extent

    # Vonalvastagság csökkentése '-' gomb megnyomásával
    elif pressed_key == 45:
        if line_thickness > min_line_thickness:
            line_thickness = line_thickness - line_thickness_extent

    # Kép mentése 's' gomb megnyomásával
    elif pressed_key == 115:
        cv2.imwrite('SomogyiAttila_ZUZ3GL.png', img)


    elif pressed_key == 116:
        # Feltöltés ([255, 255, 255]) (fehér) színnel BGR
        color_BGR = (255, 255, 255)
        color = tuple(reversed(color_BGR))
        img[:] = color

    # Kilépés 'esc' vagy 'q' gomb megnyomásával
    elif pressed_key == 27 or pressed_key == 113:
        break

# Összes ablak bezárása
cv2.destroyAllWindows()
