###############################################################################
# Existing resources
###############################################################################

data "azurerm_kubernetes_cluster" "aks" {
  name                = "aks-example"
  resource_group_name = "rg-aks-example"
}

data "azurerm_log_analytics_workspace" "sentinel" {
  name                = "law-sentinel"
  resource_group_name = "rg-sentinel"
}

# The Microsoft multi-tenancy onboarding template creates an ingestion DCE.
#
# If you are managing that DCE in Terraform already, reference the resource
# directly instead of using a data source.
data "azurerm_monitor_data_collection_endpoint" "aks_ingestion" {
  name                = "MSCI-ingestion-<generated-name>"
  resource_group_name = "rg-monitoring"
}


###############################################################################
# ContainerLogV2 multi-tenancy DCR
###############################################################################

resource "azurerm_monitor_data_collection_rule" "jfrog_container_logs" {
  name                = "dcr-aks-jfrog-sentinel"
  resource_group_name = "rg-monitoring"

  # Microsoft's ARM template places the DCR in the workspace region.
  location = data.azurerm_log_analytics_workspace.sentinel.location

  kind = "Linux"

  # Maps to:
  #
  # "dataCollectionEndpointId":
  #   "[variables('ingestionDataCollectionEndpointId')]"
  #
  data_collection_endpoint_id = data.azurerm_monitor_data_collection_endpoint.aks_ingestion.id


  ###########################################################################
  # destinations.logAnalytics
  ###########################################################################

  destinations {
    log_analytics {
      # ARM:
      #
      # "workspaceResourceId": "[parameters('workspaceResourceId')]"
      #
      workspace_resource_id = data.azurerm_log_analytics_workspace.sentinel.id

      # ARM:
      #
      # "name": "ciworkspace"
      #
      name = "ciworkspace"
    }
  }


  ###########################################################################
  # dataSources.extensions
  ###########################################################################

  data_sources {
    extension {
      # ARM:
      #
      # "name": "ContainerLogV2Extension"
      #
      name = "ContainerLogV2Extension"

      # ARM:
      #
      # "extensionName": "ContainerLogV2Extension"
      #
      extension_name = "ContainerLogV2Extension"

      # ARM:
      #
      # "streams": [
      #   "Microsoft-ContainerLogV2-HighScale"
      # ]
      #
      streams = [
        "Microsoft-ContainerLogV2-HighScale"
      ]

      # ARM:
      #
      # "extensionSettings": {
      #   "dataCollectionSettings": {
      #     "namespaces": [
      #       "artifactory"
      #     ]
      #   }
      # }
      #
      # AzureRM represents extensionSettings as extension_json.
      #
      extension_json = jsonencode({
        dataCollectionSettings = {
          namespaces = [
            "artifactory"
          ]
        }
      })
    }
  }


  ###########################################################################
  # dataFlows
  ###########################################################################

  data_flow {
    # ARM:
    #
    # "streams": [
    #   "Microsoft-ContainerLogV2-HighScale"
    # ]
    #
    streams = [
      "Microsoft-ContainerLogV2-HighScale"
    ]

    # Must match destinations.log_analytics.name.
    #
    # ARM:
    #
    # "destinations": [
    #   "ciworkspace"
    # ]
    #
    destinations = [
      "ciworkspace"
    ]

    # ARM:
    #
    # "transformKql": ...
    #
    # Start with source while validating the deployment.
    #
    transform_kql = "source"
  }
}


###############################################################################
# Associate the DCR with the AKS cluster
###############################################################################

resource "azurerm_monitor_data_collection_rule_association" "jfrog_container_logs" {
  # ARM generates:
  #
  # ContainerLogV2Extension-<unique workspace hash>
  #
  # Terraform doesn't need to reproduce the ARM uniqueString() naming.
  name = "ContainerLogV2Extension-jfrog-sentinel"

  # ARM resource:
  #
  # Microsoft.ContainerService/managedClusters/providers/
  # dataCollectionRuleAssociations
  #
  # target = AKS cluster resource ID
  #
  target_resource_id = data.azurerm_kubernetes_cluster.aks.id

  # ARM:
  #
  # "dataCollectionRuleId":
  #   "[variables('dataCollectionRuleId')]"
  #
  data_collection_rule_id = azurerm_monitor_data_collection_rule.jfrog_container_logs.id

  description = "Collect JFrog container logs from selected AKS namespaces into the Sentinel workspace."
}