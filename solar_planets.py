import cv2

img = cv2.imread("solar-system.jpg")
sol = cv2.putText(img, "Sol", (100, 80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.5, (0, 150, 255), 2)
mercurio = cv2.putText(img, "Mercurio", (110, 180), cv2.FONT_HERSHEY_PLAIN, 1.2, (160, 160, 160), 1)
venus = cv2.putText(img, "Venus", (185, 270), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 120, 225), 1)
tierra = cv2.putText(img, "Tierra", (280, 270), cv2.FONT_HERSHEY_PLAIN, 1.2, (180, 255, 0), 1)
marte = cv2.putText(img, "Marte", (375, 270), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 0, 255), 1)
jupiter = cv2.putText(img, "Jupiter", (440, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 160, 235), 2)
saturno = cv2.putText(img, "Saturno", (750, 120), cv2.FONT_HERSHEY_PLAIN, 2, (118, 182, 234), 2)
urano = cv2.putText(img, "Urano", (950, 120), cv2.FONT_HERSHEY_PLAIN, 2, (197, 181, 118), 2)
neptuno = cv2.putText(img, "Neptuno", (1075, 120), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)


cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.imwrite("Sistema Solar Etiquetado.jpg", img)