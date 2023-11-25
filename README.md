**Title:** Kubernetes Microservice Application for Service Mesh Testing

**Overview:**
This document outlines the architecture of a Kubernetes-based microservice application designed to test a service mesh. The application comprises three primary components: a front-end service, a score service, and a player service.

**Components:**

1. **Front End Service:**
   - Acts as the user interface.
   - Interacts with both the score and player services.

2. **Score Service:**
   - Provides match details.
   - Offers an endpoint to request a list of 10 matches.
   - Each match in the list includes a unique ID.
   - A separate endpoint (`/score/matchID`) allows querying detailed scores of a match, streaming the score from start to end.

3. **Player Service:**
   - Delivers data about individual players.
   - Includes search functionality for players.

**Functionality:**
- Users can view match lists and detailed match scores through the front end.
- The application utilizes a service mesh to manage communications between services, ensuring efficient data transfer and service interaction.

**Purpose:**
- To test and demonstrate the capabilities of a service mesh within a Kubernetes environment.
- To provide a practical example of a microservice architecture in action, particularly in handling distinct service functionalities like player information and real-time match scoring.
