Greetings to my fellow Technology Advocates and Specialists.

In this Session, I will demonstrate __How to Create FlowChart Using Mermaid: A Step-by-Step Guide with Cloud Designations as Example.__

| __AUTOMATION OBJECTIVES:-__ |
| --------- |

| __#__ | __TOPICS__ |
| --------- | --------- |
| 1. | Create FlowChart. |
| 2. | Create FlowChart using Subgraph. |

| __REQUIREMENTS:-__ |
| --------- |
| 1. [Mermaid Live Editor](https://mermaid.live/) |

| __REFERENCE LINKS:-__ |
| --------- |
| 1. [Overall Mermaid Documentation](https://mermaid.js.org/intro/) |
| 2. [Mermaid FlowChart Basic Syntax](https://mermaid.js.org/syntax/flowchart.html) |

| __WHAT IS MERMAID ?__ |
| --------- |
| 1. Mermaid lets you create diagrams and visualizations using text and code. |
| 2. It is based on JavaScript and inspired from Markdown Text. |

| __NOTE:-__ |
| --------- |
| If users have familiarity or a working experience with Markdown, then understanding Mermaid Syntax comes easy. |

| __MERMAID FLOWCHART: POINTS TO NOTE:-__ |
| --------- |
| 1. Flowcharts are composed of nodes (geometric shapes) and edges (arrows or lines). |
| Possible FlowChart orientations are: a.) TB - __Top to bottom__; b.) TD - __Top-down/ same as top to bottom__; c.) BT - __Bottom to top__; d.) RL - __Right to left__; LR - __Left to right__. |  

| __USECASE #1:-__ |
| --------- |
| Create FlowChart. |

Below follows the code:-

```
flowchart BT
    B(Chief Cloud Officer) --> A(Chief Technology Officer)
    C(Cloud Architect) --> B
    D(Cloud Service Manager) --> B
    E(Cloud Application Lead) --> B
    C1(Devops Engineer) --> C
    C2(IaC Developer) --> C1
    C3(IaC Operations Engineer) --> C2
    F(Support Engineer) --> C3
    D1(Cloud Operations Manager) --> D
    D2(Cloud Operations Engineer) --> D1
    F(Support Engineer) --> D2
    E1(Cloud Developer) --> E
```

| __EXPLANATION OF USECASE #1 MERMAID FLOWCHART CODE:-__ |
| --------- |
| 1. `flowchart BT` - This Syntax indicates that the orientation of the FlowChart will be __Bottom to Top__. |
| 2. `B(Chief Cloud Officer)` - This Syntax indicates __a node with round edges__. |
| 3. `-->` - This Syntax indicates __a link with arrow head__. |

| __OUTPUT FOR USECASE #1:-__ |
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ig95ozgmdruyrhpq2gk7.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/siht6k0io394dfs1hsxs.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jo40axb1rfg092jgbtku.jpg) |

| __USECASE #2:-__ |
| --------- |
| Create FlowChart using Subgraph. |

Below follows the code:-

```
flowchart BT
    B(Chief Cloud Officer) --> A(Chief Technology Officer)
    C(Cloud Architect) --> B
    subgraph PLATFORM
    C1(Devops Engineer) --> C
    C2(IaC Developer) --> C1
    C3(IaC Operations Engineer) --> C2
    end
    D(Cloud Service Manager) --> B
    subgraph OPERATIONS
    D1(Cloud Operations Manager) --> D
    D2(Cloud Operations Engineer) --> D1
    end
    E(Cloud Application Lead) --> B
    subgraph APPLICATION
    E1(Cloud Developer) --> E    
    end
    subgraph SUPPORT
    F(Support Engineer) --> C3
    F(Support Engineer) --> D2
    end
```

| __EXPLANATION OF USECASE #2 MERMAID FLOWCHART CODE:-__ |
| --------- |
| 1. `flowchart BT` - This Syntax indicates that the orientation of the FlowChart will be __Bottom to Top__. |
| 2. `B(Chief Cloud Officer)` - This Syntax indicates __a node with round edges__. |
| 3. `-->` - This Syntax indicates __a link with arrow head__. |
| 4. `subgraph PLATFORM` or `subgraph OPERATIONS` or `subgraph SUPPORT` - This Syntax indicates __grouping of nodes in a grid and providing a title to it__. |

| __SYNTAX OF "SUBGRAPH":-__ |
| --------- |

```
subgraph one
    a1-->a2
    end
```
where, 
- "subgraph one" - __Title of the Grid__.
- "a1-->a2" - __a1 and a2 are nodes linked with arrow head__.
- "end" - __End of the Grid__. 

| __OUTPUT FOR USECASE #2:-__ |
| --------- |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xv5xy1l5c5sg7v89sxda.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vqaj93eahn4s493uhe0q.jpg) |
| ![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6y3d6rdji9jxzjtavp3m.jpg) |

__Hope You Enjoyed the Session!!!__

__Stay Safe | Keep Learning | Spread Knowledge__