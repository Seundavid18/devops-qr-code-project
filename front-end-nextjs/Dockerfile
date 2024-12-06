FROM node:18-alpine AS base

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

# Install any needed packages
RUN \
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
    else echo "lockfile not found." && exit 1; \
    fi

# Copy the content of the local src directory to the working directory
COPY . .

# Build the application
RUN npm run build

# Expose on application port
EXPOSE 3000

# Run the application
CMD ["npm", "start"]