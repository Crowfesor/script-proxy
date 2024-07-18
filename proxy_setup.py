import os

# Nombre de la imagen y del contenedor
IMAGE_NAME = "squid_proxy"
CONTAINER_NAME = "squid_proxy_container"

def build_docker_image():
    os.system(f"docker build -t {IMAGE_NAME} .")

def run_docker_container():
    os.system(f"docker run -d --name {CONTAINER_NAME} -p 3128:3128 {IMAGE_NAME}")

def main():
    print("Construyendo la imagen Docker...")
    build_docker_image()
    print("Ejecutando el contenedor Docker...")
    run_docker_container()
    print(f"Proxy Squid corriendo en el contenedor {CONTAINER_NAME} y escuchando en el puerto 3128.")

if __name__ == "__main__":
    main()
