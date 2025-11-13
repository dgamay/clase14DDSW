# student-service/Dockerfile
FROM node:20-alpine3.18

# Instala dependencias necesarias para compilar sqlite3
RUN apk add --no-cache python3 make g++ sqlite

WORKDIR /app

# Copia solo los archivos de dependencias primero
COPY package*.json ./

# Instala dependencias dentro del contenedor
RUN npm install

# Copia el resto del código (sin node_modules del host)
COPY . .

# Expone el puerto
EXPOSE 3000

# Comando de ejecución
CMD ["npm", "run", "dev"]
