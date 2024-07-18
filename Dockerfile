# Dockerfile
FROM ubuntu:20.04

# Instalar Squid
RUN apt-get update && \
    apt-get install -y squid && \
    apt-get clean

# Copiar archivo de configuración de Squid personalizado
COPY squid.conf /etc/squid/squid.conf

# Exponer el puerto por defecto de Squid
EXPOSE 3128

# Comando para iniciar Squid
CMD ["squid", "-N", "-d", "1"]
