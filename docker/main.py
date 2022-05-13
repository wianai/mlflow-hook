import os
from mlflow.tracking import MlflowClient
from kubernetes import client, config

mlflow_client = MlflowClient()
# os.environ['MLFLOW_TRACKING_URI']='http://localhost:54890'
model_name=os.environ['MLFLOW_MODEL_NAME']
Stage=os.environ['MLFLOW_STAGE']
seldon_deploy_name=os.environ['MLFLOW_DEPLOY_NAME']
namespace=os.environ['DEPLOY_NAMESPACE']
mlflow_prod_uri=mlflow_client.get_latest_versions(name=model_name,stages=[Stage])[0].source
print(mlflow_prod_uri)
config.load_incluster_config()
v1 = client.CustomObjectsApi()
seldon_model_uri =v1.get_namespaced_custom_object(group="machinelearning.seldon.io",
        version="v1",
        plural="seldondeployments",
        name=seldon_deploy_name,
        namespace=namespace)['spec']['predictors'][0]['graph']['modelUri']
print(seldon_model_uri)
seldon_dep = v1.get_namespaced_custom_object(group="machinelearning.seldon.io",
        version="v1",
        plural="seldondeployments",
        name=seldon_deploy_name,
        namespace=namespace)
if mlflow_prod_uri != seldon_dep:
    seldon_dep['spec']['predictors'][0]['graph']['modelUri']=mlflow_prod_uri
    api_response = v1.patch_namespaced_custom_object(group="machinelearning.seldon.io",
            version="v1",
            plural="seldondeployments",
            name=seldon_deploy_name,namespace=namespace,body=seldon_dep )
    print(api_response)