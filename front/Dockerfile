FROM node:20-alpine

WORKDIR /app

COPY ./front/package*.json ./

RUN npm install

COPY ./front /app

EXPOSE 8080

CMD npm run serve