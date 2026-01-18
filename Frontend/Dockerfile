# ---------- Build stage ----------
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---------- Serve stage ----------
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

# ✅ CORRECT PATH (based on your screenshot)
COPY --from=build /app/dist/Frontend/browser /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
