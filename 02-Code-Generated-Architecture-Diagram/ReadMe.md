# Code Generated Architecture Diagram:-

Greetings to my fellow Technology Advocates and Specialists.

In this Session, I will demonstrate __How to Create Azure Solutions Architecture Diagram by Code.__

| __AUTOMATION OBJECTIVES:-__ |
| --------- |

| __#__ | __TOPICS__ |
| --------- | --------- |
| 1. | __Example #1:__ Create "Basic Azure App Service Architecture Diagram" by Code. |
| 2. | __Example #2:__ Create "Gaming Architecture Diagram" by Code. |

| __PRE-REQUISITES:-__ |
| --------- |
| 1. Python 3.6 or higher. |
| 2. Graphviz |
| 3. pip |

| __VALIDATE PRE-REQUISITES:-__ |
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9njbv0578vmv921tk07k.jpg) |

| __COMMANDS TO VERIFY:-__ |
| --------- |

```
python --version
dot -V
pip --version
```

| __INSTALL DIAGRAMS:-__ |
| --------- |

__Install "diagrams" using "pip":-__

`pip install diagrams`

| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uyrkrqy8gxccolz4kig9.jpg) |
| --------- |

| __REFERENCE LINKS:-__ |
| --------- |
| 1. [Diagram as Code](https://diagrams.mingrammer.com/) |
| 2. [Diagram as Code - Installation](https://diagrams.mingrammer.com/docs/getting-started/installation) |
| 3. [Diagram as Code - Examples](https://diagrams.mingrammer.com/docs/getting-started/examples) |
| 4. [Diagram as Code - List of Azure Providers](https://diagrams.mingrammer.com/docs/nodes/azure) |

| __CONCEPTS:-__ |
| --------- |

| __I.) DIAGRAMS:-__ |
| --------- |
| 1. Represents a global diagram context. |
| 2. Diagram context can be created with Diagram class. |
| 3. The first parameter of Diagram constructor will be used for output filename. |

| __II.) NODES:-__ |
| --------- |
| 1. Represents a single system component object. |
| 2. A node object consists of three parts: i) Provider, ii) Resource type and iii) Name. |

| __III.) CLUSTERS:-__ |
| --------- |
| 1. Allows you group (or clustering) the nodes. |

| __IV.) EDGES:-__ |
| --------- |
| 1. Represents a connection between Nodes with some additional properties. |

Now, we proceed in __Creating Architecture Diagram__ using Diagrams and Python.

| __CONSTRUCT OF THE PYTHON CODE TO CREATE ARCHITECTURE DIAGRAM:-__ |
| --------- |
| 1. Import Diagram, Cluster and Edge. |
| 2. Import the Provider Icons for creating diagrams. |
| 3. Creating the building blocks using Nodes and Cluster. |
| 4. Connect the building blocks using Edges. |

| __EXAMPLE #1:__ | 
| --------- |

__Create "Basic Azure App Service Architecture Diagram" by Code.__

Below follows the Python Code (Generate-Basic-Azure-App-service-Arch-Diagram.py):-

```
############################################################
## Architecture Diagram: Basic Azure App Service:-

## Components include:-
# 1. User
# 2. Azure Entra ID
# 3. Azure Monitor
# 4. Azure Application Insights
# 5. Azure User Assigned Managed Identity
# 6. Azure Key Vault 
# 7. Azure App Services
# 8. Azure SQL Servers

############################################################

######################################################
# Import Diagram, Cluster and Edge.
# Import the Provider Icons for creating diagrams.
######################################################

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.general import Helpsupport, Servicehealth
from diagrams.azure.devops import ApplicationInsights
from diagrams.azure.security import KeyVaults
from diagrams.azure.identity import ManagedIdentities, ActiveDirectory
from diagrams.azure.compute import AppServices
from diagrams.azure.database import SQLServers

#########################################################
# Creating the building blocks using Nodes and Cluster.
#########################################################

with Diagram("Basic Azure App Service Architecture", show=False, direction="TB"):
    usr = Helpsupport("User")

    with Cluster("Compute"):
        components_webapp = [AppServices("AppServices"), KeyVaults("KV"), ManagedIdentities("UMID")]

    with Cluster("Data"):
        components_db = SQLServers("Azure SQL Database")

    with Cluster("Identity"):
        components_identity = [ActiveDirectory("Microsoft Entra ID")]

    with Cluster("Monitoring"):
        components_monitor = [ApplicationInsights("App Insights"), Servicehealth("Azure Monitor")]

############################################
# Connect the building blocks using Edges.
############################################

    usr >> Edge(color="darkorange") >> components_webapp
    
    components_webapp >> Edge(color="darkgreen") >> components_db

```

| __EXECUTE THE PYTHON CODE:-__ | 
| --------- |

`python.exe .\Generate-Basic-Azure-App-service-Arch-Diagram.py`

| __OUTPUT OF EXAMPLE #1:-__ | 
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r696eis3c7yzeep0g5iu.png) |

| __EXAMPLE #2:__ | 
| --------- |

__Create "Gaming Architecture Diagram" by Code.__

Below follows the Python Code (Generate-Gaming-Arch-Diagrams.py):-

```
############################################################
## Architecture Diagram: Gaming using Azure Cosmos DB:-

## Components include:-
# 1. User
# 2. Azure Traffic Manager
# 3. Azure Content Delivery Network
# 4. Azure Storage
# 5. Azure API Management 
# 6. Azure Cosmos DB
# 7. Azure Databricks
# 8. Azure Functions
# 9. Azure Notification Hubs

############################################################

######################################################
# Import Diagram, Cluster and Edge.
# Import the Provider Icons for creating diagrams.
######################################################

from diagrams import Cluster, Diagram, Edge
from diagrams.azure.general import Helpsupport
from diagrams.azure.network import TrafficManagerProfiles, CDNProfiles
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.integration import APIManagement
from diagrams.azure.database import CosmosDb
from diagrams.azure.analytics import Databricks
from diagrams.azure.compute import FunctionApps
from diagrams.azure.mobile import NotificationHubs

#########################################################
# Creating the building blocks using Nodes and Cluster.
#########################################################

# with Diagram("GAMING ARCHITECTURE", show=False, direction="TB"):
with Diagram("GAMING ARCHITECTURE", show=False):
    usr = Helpsupport("User")

    # atm = TrafficManagerProfiles("Azure Traffic Manager")

    apim = APIManagement("Azure API Apps")

    cosmos = CosmosDb("Azure Cosmos DB")

    dbks = Databricks("Azure Databricks")

    # cdn = CDNProfiles ("Azure CDN")

    # storage = StorageAccounts("Azure Storage (Media Files)")

    functions = FunctionApps("Azure Functions")

    notifyhub = NotificationHubs("Azure Notification Hubs")

    with Cluster(""):
         atm = TrafficManagerProfiles("Traffic Manager")

    with Cluster(""):
         cdn = CDNProfiles ("Azure CDN")

    with Cluster(""):
         storage = StorageAccounts("Azure Storage")

############################################
# Connect the building blocks using Edges.
############################################

    usr >> Edge(color="darkgreen") >> atm
    cdn >> Edge(color="darkblue") >> atm
    storage >> Edge(color="darkpurple") >> cdn
    atm >> Edge(color="darkorange") >> apim
    apim >> Edge(color="darkred") >> cosmos
    cosmos >> Edge(color="darkred") >> apim
    cosmos >> Edge(color="darkblue") >> dbks
    cosmos >> Edge(color="darkblue") >> functions
    functions >> Edge(color="darkbrown") >> notifyhub
```

| __EXECUTE THE PYTHON CODE:-__ | 
| --------- |

`python.exe .\Generate-Gaming-Arch-Diagrams.py`

| __OUTPUT OF EXAMPLE #2:-__ | 
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d4s901itnxal1osjsus3.png) |

__Hope You Enjoyed the Session!!!__

__Stay Safe | Keep Learning | Spread Knowledge__
