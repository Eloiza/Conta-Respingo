import contarespingo
import cv2          #openCV - biblioteca p/ manipular imagens
import numpy as np  #numpy  - biblioteca p/ manipulação de vetores/matrizes 

def main():
  img = cv2.imread("./Imagens/MOD_C_45.jpg")

  width = round(img.shape[1] * 0.10)
  height = round(img.shape[0] * 0.10)

  #diminuindo tamanho da imagem original p/ melhor visualização
  print("Tamanho Original:", img.shape)
  img = cv2.resize(img, (width,height), interpolation = cv2.INTER_AREA)
  print("Tamanho Novo:",img.shape)

  print("Imagem Original")

  cv2_imshow(img)
  #deteccao de bordas ussando filtro de canny, usado p/ detectar rosto 
  canny = edge_detection(img)

  #realce e reducao de ruido no canny
  kernel = np.ones((3,3), np.uint8)
  canny = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

  #encontra roi e retorna roi da img original + mascara nova
  roi, mask = find_roi(img, canny)

  #conta area ocupada pelo vermelho no manequim
  total_area = count_red(roi, mask)
  total_area = total_area + '%'
  
  #escrevendo area total na imagem de entrada
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(roi, total_area, (30,50), font, 1, (0,255,0), 2, cv2.LINE_AA)
  print("Imagem Final")
  cv2_imshow(roi)

  #salvando imagem com o resultado
  # img_name2 = img_name.split("/")[2] 
  # dir_name = img_name.split("/")[1]
  # print(dir_name + "/result_" + img_name2)
  # cv2.imwrite(dir_name + "/result_" + img_name2, roi)
  # cv2.waitKey(0)

if(__name__ == '__main__'):
	main()