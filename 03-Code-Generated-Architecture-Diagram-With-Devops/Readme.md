Greetings to my fellow Technology Advocates and Specialists.

In this Session, I will demonstrate __How to Create Azure Solutions Architecture Diagram by Code using Azure Devops.__

| __AUTOMATION OBJECTIVES:-__ |
| --------- |

| __#__ | __TOPICS__ |
| --------- | --------- |
| 1. | __Example #1:__ Create "Basic Azure App Service Architecture Diagram" by Code using Azure Devops. |
| 2. | __Example #2:__ Create "Gaming Architecture Diagram" by Code using Azure Devops. |

| IMPORTANT NOTE:- |
| --------- |

The YAML Pipeline is tested on __WINDOWS BUILD AGENT__ Only!!!

| __REQUIREMENTS:-__ |
| --------- |

1. Azure Subscription.
2. Azure DevOps Organisation and Project.
3. System Access Token Configured for Pipeline.
4. Service Principal with Required RBAC ( Contributor) applied on Subscription or Resource Group(s).
5. Azure Resource Manager Service Connection in Azure DevOps.

| __REFERENCE LINKS:-__ |
| --------- |
| 1. [Diagram as Code](https://diagrams.mingrammer.com/) |
| 2. [Diagram as Code - Installation](https://diagrams.mingrammer.com/docs/getting-started/installation) |
| 3. [Diagram as Code - Examples](https://diagrams.mingrammer.com/docs/getting-started/examples) |
| 4. [Diagram as Code - List of Azure Providers](https://diagrams.mingrammer.com/docs/nodes/azure) |

| __PRE-REQUISITES:-__ |
| --------- |
| 1. Python 3.6 or higher. |
| 2. Graphviz |
| 3. pip |

| HOW DOES MY CODE PLACEHOLDER LOOKS LIKE:- |
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/obzibe3xil9evgkjwlav.jpg) |

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

Now, we proceed in __Creating Architecture Diagram__ using Diagrams, Python and Azure Devops.

| __EXAMPLE #1:__ | 
| --------- |

__Create "Basic Azure App Service Architecture Diagram" by Code.__

| __CONSTRUCT OF THE PYTHON CODE TO CREATE ARCHITECTURE DIAGRAM:-__ |
| --------- |
| 1. Import Diagram, Cluster and Edge. |
| 2. Import the Provider Icons for creating diagrams. |
| 3. Creating the building blocks using Nodes and Cluster. |
| 4. Connect the building blocks using Edges. |

| PYTHON CODE SNIPPET:- | 
| --------- |

| PYTHON CODE (Generate-Basic-Azure-App-service-Arch-Diagram.py):- |
| --------- |

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

| __CONSTRUCT OF AZURE DEVOPS PIPELINE TO EXECUTE PYTHON CODE TO CREATE ARCHITECTURE DIAGRAM:-__ |
| --------- |
| 1. Generate Solution Architecture Diagram using Diagrams, Python and Azure Devops. |
| 2. Commit the Solution Architecture Diagram created to GIT repository. |
| 3. The Pipeline has 2 stages. |
| 4(a). __Stage #1__ performs below:- |
| 4(b). Install Requisites in the build agent.  |
| 4(c). Generate Solution Architecture diagram. |
| 4(d). Copy Generated Solution Architecture diagram to Artifacts staging directory. |
| 4(e). Publish Generated Solution Architecture diagram as Artifacts. |
| 5(i). __Stage #2__ performs below:- |
| 5(ii). Download Artifacts. |
| 5(iii). Commit Generated Solution Architecture diagram to Azure Devops GIT repository. |
| 5(iv). __System Access Token__ is configured to run the build. |

| PIPELINE CODE SNIPPET:- | 
| --------- |

| AZURE DEVOPS YAML PIPELINE (azure-pipelines-diagram-as-code-v1.0.yml):- |
| --------- |

```
####################################
# Automation Scope:-
#####################
# 1. Generate Diagrams by Code.
# 2. Commit 2 Git.
####################################

################################################################################################################################
# Important to Note:-
#####################
# 1. The Consumers only need to change the value which are commented in the "Declare Variables" Section.
# 2. If you are changing the value of "pythonCode" Variable, then make sure, you change the value of "DiagramName" Variable. 
################################################################################################################################

trigger:
  none

#######################
# Declare Variables:-
#######################
variables:
  ServiceConnection: 'amcloud-cicd-service-connection' # Please replace with your Service Connection!
  BuildAgent: 'windows-latest' # Please replace with your Build Agent. You can continue to use this as this is Microsoft Hosted Windows Build Agent!
  envName: 'NonProd' # Please replace with your Azure Devops Environment Name
  pythonCode: 'Generate-Basic-Azure-App-service-Arch-Diagram.py' # Please replace with your script name kept in the "Code" Directory! 
  RootWorkingFolderName: 'Digram-As-Code-With-Devops' # Please replace with your Root Working Folder Name!
  ChildWorkingFolderName1: 'Code' # Please replace with your Child Working Folder Name!
  ChildWorkingFolderName2: 'Diagrams' # Please replace with your Child Working Folder Name!
  WorkingDir: '$(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)' 
  TargetFolderName: 'AMDaC' # Please replace with your naming convention!
  Target: '$(build.artifactstagingdirectory)\$(TargetFolderName)'
  Artifact: 'DaC' # Please replace with your naming convention!
  DiagramName: 'basic_azure_app_service_architecture.png' # Please replace with the name, you have mentioned inside your Python Script!
  DevopsOrgName: 'ArindamMitra0251' # Please replace with your Azure Devops Organisation Name!
  DevopsPrjName: 'AMCLOUD' # Please replace with your Azure Devops Project Name!
  DevopsRepoName: 'YAML-v1.0' # Please replace with your Azure Devops Repository Name!
  DevOpsGITUser: 'AM' # Please replace with your Custom GIT Username!
  DevOpsGITEmail: 'arindam0310018@gmail.com' # Please replace with your GIT user email address!

######################
# Declare Build Agent:-
######################
pool:
  vmImage: '$(BuildAgent)'

#############################
# Declare Stages:-
# Generate Diagrams by Code
#############################
stages:

- stage: Diagram_As_Code
  jobs:
  - job: Diagram_As_Code
    displayName: Diagram As Code
    steps:
    - task: AzureCLI@2
      displayName: Diagram As Code
      inputs:
        azureSubscription: $(ServiceConnection)
        scriptType: ps
        scriptLocation: inlineScript
        inlineScript: |
          echo "##########################################################"
          $choco_ver = choco -v
          echo "The latest chocolatey version installed is: $choco_ver"
          echo "##########################################################"
          python --version
          echo "#######################################"
          pip --version
          echo "#######################################"
          echo "Installing Graphiz...!"
          echo "#######################################"
          choco install graphviz -y
          echo "#######################################"
          echo "Validate graphviz Installation..."
          echo "########################################"
          sleep 10
          dot -V
          echo "########################################"
          pip install diagrams
          echo "########################################"
          cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\
          dir
          echo "########################################"
          python $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\$(pythonCode)   
          cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\
          dir
          $outputPath = "$(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\$(DiagramName)"
          if (Test-Path $outputPath) {
             Write-Host "$(DiagramName) created successfully."
             } 
          else {
                Write-Host "$(DiagramName) was NOT created."
                exit 1
                }
          echo "########################################"

###############################################
# Copy Files to Artifacts Staging Directory:-
###############################################
    - task: CopyFiles@2
      displayName: Copy Files Artifacts Staging Directory
      inputs:
        SourceFolder: '$(workingDir)'
        Contents: |
          **/*.png
        TargetFolder: '$(Target)'

# ########################
# # Publish Artifacts:-
# ########################
    - task: PublishBuildArtifacts@1
      displayName: Publish Artifacts
      inputs:
        targetPath: '$(Target)'
        artifactName: '$(Artifact)'     

#############################
# Stage: Commit 2 Code
#############################

- stage: Commit_2_Git
  condition: succeeded('Diagram_As_Code')
  jobs:
  - deployment: 
    displayName: Commit_2_Git
    environment: $(envName)
    pool:
      vmImage: '$(BuildAgent)'
    strategy:
      runOnce:
        deploy:
          steps:
          - checkout: self 
            persistCredentials: true

#########################
# Download Artifacts:-
#########################
          - task: DownloadBuildArtifacts@0
            displayName: Download Artifacts
            inputs:
              buildType: 'current'
              downloadType: 'single'
              artifactName: '$(Artifact)'
              downloadPath: '$(System.ArtifactsDirectory)'

#########################################
# Commit 2 Git:-
# Authentication - System Access Token
#########################################
          - task: PowerShell@2
            displayName: GIT Commit 
            inputs:
              targetType: 'inline'
              script: |
                cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName2)
                cp $(System.ArtifactsDirectory)\$(Artifact)\$(TargetFolderName)\$(DiagramName) . 
                echo "#####################"
                echo "Diagram copied!"
                echo "Listing the contents in the current directory:-"
                dir
                echo "#####################"
                git remote -v
                echo "#####################"
                git remote set-url origin https://$(System.AccessToken)@dev.azure.com/$(DevopsOrgName)/$(DevopsPrjName)/_git/$(DevopsRepoName)
                echo "#####################"
                git ls-remote origin
                echo "#####################"
                git config --global user.email "$(DevOpsGITEmail)"
                git config --global user.name "$(DevOpsGITUser)"
                git config --global --unset https.proxy
                git checkout -b $(Build.SourceBranchName)
                git add .
                git commit -m "Output Architecture Diagram"
                git push origin $(Build.SourceBranchName)
            env:
              SYSTEM_ACCESSTOKEN: $(System.AccessToken)
```

| __IMPORTANT TO NOTE:-__ | 
| --------- |
| 1. The users only need to change the value which are commented in the __"Declare Variables"__ Section. |
| 2. If you are changing the value of __"pythonCode"__ Variable, then make sure, you change the value of __"DiagramName"__ Variable. |

| __OUTPUT OF EXAMPLE #1:-__ | 
| --------- |
| 1. Configure System Access Token. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e0lsqbq85rq4ovqo9hsa.jpg) |
| 2. Successful Pipeline run. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hxzikakx8mk7hnvj3fyj.jpg) |
| 3. Generated Solutions Architecture Diagram as Artifacts Uploaded in Azure Devops. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q7u741s9lld1sz9vf2o6.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2daeqhenxwxr2uvilrgi.jpg) |
| 4. Solutions Architecture Diagram Generated is Committed in Azure Devops Repo. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0e8dt4e1z9h8iprmshnj.jpg) |

| __EXAMPLE #2:__ | 
| --------- |

__Create "Gaming Architecture Diagram" by Code.__

| __CONSTRUCT OF THE PYTHON CODE TO CREATE ARCHITECTURE DIAGRAM:-__ |
| --------- |
| 1. Import Diagram, Cluster and Edge. |
| 2. Import the Provider Icons for creating diagrams. |
| 3. Creating the building blocks using Nodes and Cluster. |
| 4. Connect the building blocks using Edges. |

| PYTHON CODE SNIPPET:- | 
| --------- |

| PYTHON CODE (Generate-Gaming-Arch-Diagrams.py):- |
| --------- |

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

| __CONSTRUCT OF AZURE DEVOPS PIPELINE TO EXECUTE PYTHON CODE TO CREATE ARCHITECTURE DIAGRAM:-__ |
| --------- |
| 1. Generate Solution Architecture Diagram using Diagrams, Python and Azure Devops. |
| 2. Commit the Solution Architecture Diagram created to GIT repository. |
| 3. The Pipeline has 2 stages. |
| 4(a). __Stage #1__ performs below:- |
| 4(b). Install Requisites in the build agent.  |
| 4(c). Generate Solution Architecture diagram. |
| 4(d). Copy Generated Solution Architecture diagram to Artifacts staging directory. |
| 4(e). Publish Generated Solution Architecture diagram as Artifacts. |
| 5(i). __Stage #2__ performs below:- |
| 5(ii). Download Artifacts. |
| 5(iii). Commit Generated Solution Architecture diagram to Azure Devops GIT repository. |
| 5(iv). __System Access Token__ is configured to run the build. |

| PIPELINE CODE SNIPPET:- | 
| --------- |

| AZURE DEVOPS YAML PIPELINE (azure-pipelines-diagram-as-code-v1.0.yml):- |
| --------- |

```
####################################
# Automation Scope:-
#####################
# 1. Generate Diagrams by Code.
# 2. Commit 2 Git.
####################################

################################################################################################################################
# Important to Note:-
#####################
# 1. The Consumers only need to change the value which are commented in the "Declare Variables" Section.
# 2. If you are changing the value of "pythonCode" Variable, then make sure, you change the value of "DiagramName" Variable. 
################################################################################################################################

trigger:
  none

#######################
# Declare Variables:-
#######################
variables:
  ServiceConnection: 'amcloud-cicd-service-connection' # Please replace with your Service Connection!
  BuildAgent: 'windows-latest' # Please replace with your Build Agent. You can continue to use this as this is Microsoft Hosted Windows Build Agent!
  envName: 'NonProd' # Please replace with your Azure Devops Environment Name
  pythonCode: 'Generate-Gaming-Arch-Diagrams.py' # Please replace with your script name kept in the "Code" Directory! 
  RootWorkingFolderName: 'Digram-As-Code-With-Devops' # Please replace with your Root Working Folder Name!
  ChildWorkingFolderName1: 'Code' # Please replace with your Child Working Folder Name!
  ChildWorkingFolderName2: 'Diagrams' # Please replace with your Child Working Folder Name!
  WorkingDir: '$(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)' 
  TargetFolderName: 'AMDaC' # Please replace with your naming convention!
  Target: '$(build.artifactstagingdirectory)\$(TargetFolderName)'
  Artifact: 'DaC' # Please replace with your naming convention!
  DiagramName: 'Gaming_Architecture.png' # Please replace with the name, you have mentioned inside your Python Script!
  DevopsOrgName: 'ArindamMitra0251' # Please replace with your Azure Devops Organisation Name!
  DevopsPrjName: 'AMCLOUD' # Please replace with your Azure Devops Project Name!
  DevopsRepoName: 'YAML-v1.0' # Please replace with your Azure Devops Repository Name!
  DevOpsGITUser: 'AM' # Please replace with your Custom GIT Username!
  DevOpsGITEmail: 'arindam0310018@gmail.com' # Please replace with your GIT user email address!

######################
# Declare Build Agent:-
######################
pool:
  vmImage: '$(BuildAgent)'

#############################
# Declare Stages:-
# Generate Diagrams by Code
#############################
stages:

- stage: Diagram_As_Code
  jobs:
  - job: Diagram_As_Code
    displayName: Diagram As Code
    steps:
    - task: AzureCLI@2
      displayName: Diagram As Code
      inputs:
        azureSubscription: $(ServiceConnection)
        scriptType: ps
        scriptLocation: inlineScript
        inlineScript: |
          echo "##########################################################"
          $choco_ver = choco -v
          echo "The latest chocolatey version installed is: $choco_ver"
          echo "##########################################################"
          python --version
          echo "#######################################"
          pip --version
          echo "#######################################"
          echo "Installing Graphiz...!"
          echo "#######################################"
          choco install graphviz -y
          echo "#######################################"
          echo "Validate graphviz Installation..."
          echo "########################################"
          sleep 10
          dot -V
          echo "########################################"
          pip install diagrams
          echo "########################################"
          cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\
          dir
          echo "########################################"
          python $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\$(pythonCode)   
          cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\
          dir
          $outputPath = "$(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName1)\$(DiagramName)"
          if (Test-Path $outputPath) {
             Write-Host "$(DiagramName) created successfully."
             } 
          else {
                Write-Host "$(DiagramName) was NOT created."
                exit 1
                }
          echo "########################################"

###############################################
# Copy Files to Artifacts Staging Directory:-
###############################################
    - task: CopyFiles@2
      displayName: Copy Files Artifacts Staging Directory
      inputs:
        SourceFolder: '$(workingDir)'
        Contents: |
          **/*.png
        TargetFolder: '$(Target)'

# ########################
# # Publish Artifacts:-
# ########################
    - task: PublishBuildArtifacts@1
      displayName: Publish Artifacts
      inputs:
        targetPath: '$(Target)'
        artifactName: '$(Artifact)'     

#############################
# Stage: Commit 2 Code
#############################

- stage: Commit_2_Git
  condition: succeeded('Diagram_As_Code')
  jobs:
  - deployment: 
    displayName: Commit_2_Git
    environment: $(envName)
    pool:
      vmImage: '$(BuildAgent)'
    strategy:
      runOnce:
        deploy:
          steps:
          - checkout: self 
            persistCredentials: true

#########################
# Download Artifacts:-
#########################
          - task: DownloadBuildArtifacts@0
            displayName: Download Artifacts
            inputs:
              buildType: 'current'
              downloadType: 'single'
              artifactName: '$(Artifact)'
              downloadPath: '$(System.ArtifactsDirectory)'

#########################################
# Commit 2 Git:-
# Authentication - System Access Token
#########################################
          - task: PowerShell@2
            displayName: GIT Commit 
            inputs:
              targetType: 'inline'
              script: |
                cd $(System.DefaultWorkingDirectory)\$(RootWorkingFolderName)\$(ChildWorkingFolderName2)
                cp $(System.ArtifactsDirectory)\$(Artifact)\$(TargetFolderName)\$(DiagramName) . 
                echo "#####################"
                echo "Diagram copied!"
                echo "Listing the contents in the current directory:-"
                dir
                echo "#####################"
                git remote -v
                echo "#####################"
                git remote set-url origin https://$(System.AccessToken)@dev.azure.com/$(DevopsOrgName)/$(DevopsPrjName)/_git/$(DevopsRepoName)
                echo "#####################"
                git ls-remote origin
                echo "#####################"
                git config --global user.email "$(DevOpsGITEmail)"
                git config --global user.name "$(DevOpsGITUser)"
                git config --global --unset https.proxy
                git checkout -b $(Build.SourceBranchName)
                git add .
                git commit -m "Output Architecture Diagram"
                git push origin $(Build.SourceBranchName)
            env:
              SYSTEM_ACCESSTOKEN: $(System.AccessToken)
```

| __IMPORTANT TO NOTE:-__ | 
| --------- |
| 1. The users only need to change the value which are commented in the __"Declare Variables"__ Section. |
| 2. If you are changing the value of __"pythonCode"__ Variable, then make sure, you change the value of __"DiagramName"__ Variable. |

| __OUTPUT OF EXAMPLE #2:-__ | 
| --------- |
| 1. Configure System Access Token. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6zu22h6rcrickvu0suyv.jpg) |
| 2. Successful Pipeline run. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/neqfaai6fvq53wl9dm26.jpg) |
| 3. Generated Solutions Architecture Diagram as Artifacts Uploaded in Azure Devops. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1c4irbo9j97vklwe50fm.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6f9o98znoh07n6sh1kye.jpg) |
| 4. Solutions Architecture Diagram Generated is Committed in Azure Devops Repo. |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qa396l7l2ynbwh0ochep.jpg) |

__Hope You Enjoyed the Session!!!__

__Stay Safe | Keep Learning | Spread Knowledge__
