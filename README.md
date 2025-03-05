# AI-Powered Supplier Risk Management

This repository contains the code for an AI-powered supplier risk management.

## Environment Variables
The following environment variables need to be set for the system to function correctly:

- `ACR_ENDPOINT`: The endpoint for Azure Container Registries.
- `ACR_PASSWORD`: The password for Azure Container Registries.
- `ACR_USERNAME`: The username for Azure Container Registries.
- `BOSCHDEVCLOUD_TOKEN`: The token for BoschDevCloud artifactory, used for Modanalit.
- `BOSCHDEVCLOUD_USERNAME`: The username for BoschDevCloud artifactory, used for Modanalit.

## Deployment
To deploy the AI-powered supplier risk management, follow these steps:

1. **Build the Docker Image**: Use the provided Dockerfile to build the Docker image. A GitHub Action is already provided to build the Docker image.
    ```sh
    docker build -t ai-powered-supplier-risk-management .
    ```

2. **Push the Docker Image to Azure Container Registry**: Tag and push the Docker image to your Azure Container Registry. A GitHub Action is already provided to push the Docker image to Azure Container Registry when a release is created.
    ```sh
    docker tag ai-powered-supplier-risk-management <ACR_ENDPOINT>/ai-powered-supplier-risk-management
    docker push <ACR_ENDPOINT>/ai-powered-supplier-risk-management
    ```

3. **Create an Azure Container App**: Use the Azure CLI to create a new Azure Container App.
    ```sh
    az containerapp create --name ai-powered-supplier-risk-management --resource-group <RESOURCE_GROUP> --image <ACR_ENDPOINT>/ai-powered-supplier-risk-management --environment <ENVIRONMENT> --cpu 1 --memory 2Gi --registry-server <ACR_ENDPOINT> --registry-username <ACR_USERNAME> --registry-password <ACR_PASSWORD>
    ```
    ```

4. **Start the Application**: Override the startup command to run the application. The Docker image for the AI-powered supplier risk management is configured to expose port `8080`. This port is used by the application to handle incoming HTTP requests. 
    ```sh
    az containerapp update --name ai-powered-supplier-risk-management --resource-group <RESOURCE_GROUP> --startup-command "modanalit run /app/app/Home.py --server.port=8080 --server.address=0.0.0.0"
    ```

## Technical Documentation

### Initial PoC

#### Agents
1. Supplier Profiling Specialist
    - To gather foundational information about the supplier (industry, size, location, financials, etc.)
    - Expected output:
        - Supplier name
        - Homepage
        - Address
        - Industry / Product Scope
        - Company Size
        - Headquarters / Main Location
        - Financial Data
        - Market Position (Optional)
        - Sources

2. Strategy & Operations Risk Investigator
    - To identify operational and strategic factors that could impair the supplier's delivery capability
    - Expected output:
        - Critical Communications
        - Site or Plant Closures
        - Withdrawal of Certificates
        - Geopolitical Risks
        - Machine Park Conditions

#### Tools
1. Search web content  
    - Searches the web based on a search query for the latest results
    - Expected output:  
        - Url
        - Web contents
2. Similar articles  
    - Searches for similar articles to a given url
    - Expected output:  
        - Url
        - Another related web contents
3. Get web content  
    - Gets the contents of a specific url
    - Expected output:  
        - Url
        - Web contents

The relevant source can be coming from:  
1. Company home pages
2. Linkedin company pages
3. Financial reports
4. News
5. And more other source (government or organization site, blogs, events)

#### Flow
1. User input
    - company name
    - address
    - homepage
2. Agent: Supplier Profiling Specialist
    - To gather foundational information about the supplier.
    - Tools: Search web content
3. Agent: Strategy & Operations Risk Investigator
    - To identify operational and strategic factors that could impair the supplier's delivery capability
    - Tools: Search web content



