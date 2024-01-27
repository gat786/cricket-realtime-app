# Use an official Node runtime as a parent image
FROM --platform=$BUILDPLATFORM node:21-slim as build

ARG BUILDPLATFORM
# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

ENV PUBLIC_PLAYER_SERVICE_ENDPOINT=http://localhost:8001
ENV PUBLIC_TEAM_SERVICE_ENDPOINT=http://localhost:8002
ENV PUBLIC_SCORE_SERVICE_ENDPOINT=http://localhost:8000
ENV PUBLIC_SCORE_SOCKET_ENDPOINT=ws://localhost:8000
ENV ENVIRONMENT=production

# Install any needed packages specified in package.json
RUN npm install && npm run build

FROM --platform=$BUILDPLATFORM node:latest as deployment
ARG BUILDPLATFORM

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/ ./

EXPOSE 3000

# Add Tini
ENV TINI_VERSION v0.19.0
RUN ARCH=$(echo $BUILDPLATFORM | cut -c 7-); wget https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-${ARCH} -O tini;
RUN chmod +x tini


ENTRYPOINT ["/usr/src/app/tini", "--"]

# CMD [ "node", "build/index.js" ]
