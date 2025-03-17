# Detecção de Sorriso em Tempo Real

Este projeto utiliza a biblioteca **OpenCV** para detectar rostos e identificar sorrisos em tempo real a partir da câmera do dispositivo.

### Funcionalidade

- O sistema detecta rostos em tempo real através da câmera do dispositivo.
- Quando um sorriso é detectado em um rosto, um retângulo verde é desenhado ao redor do sorriso e a palavra "Sorrindo!" é exibida na tela.
- Utiliza classificadores pré-treinados do OpenCV (`haarcascade_frontalface_default.xml` para rostos e `haarcascade_smile.xml` para sorrisos).

### Como Funciona

1. O código utiliza a **cascata de Haar** para detectar rostos e sorrisos.
2. Ele converte os frames capturados pela câmera para escala de cinza para otimizar a detecção.
3. A detecção de sorrisos ocorre dentro da região onde um rosto foi identificado.
4. O programa exibe um retângulo azul em torno do rosto e um retângulo verde em torno do sorriso, caso ele seja detectado.

### Requisitos

- Python 3.x
- OpenCV

### Como Rodar

1. Clone este repositório ou faça o download dos arquivos.
2. Instale o OpenCV, se ainda não o tiver:
   ```bash
   pip install opencv-python
   ```
3. Execute o script Python:
   ```bash
   python nome_do_arquivo.py
