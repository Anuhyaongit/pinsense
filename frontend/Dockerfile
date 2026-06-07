# Stage 1: Build
# Build your React app
FROM node:18-alpine as build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build for GitHub Pages (with subdirectory)
# If deploying to subdirectory, set PUBLIC_URL
ARG PUBLIC_URL=/pinsense
ENV PUBLIC_URL=$PUBLIC_URL

# Build the application
RUN npm run build

# Stage 2: Production
# Serve the built app with a lightweight server
FROM node:18-alpine

WORKDIR /app

# Install serve to run static files
RUN npm install -g serve

# Copy built files from build stage
COPY --from=build /app/build ./build

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:3000 || exit 1

# Set API URL (can be overridden at runtime)
ENV REACT_APP_API_URL=http://localhost:8000

# Serve the application
CMD ["serve", "-s", "build", "-l", "3000"]
