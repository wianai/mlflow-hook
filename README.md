<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Hellomlops" />

  &#xa0;

  <!-- <a href="https://Hellomlops.netlify.app">Demo</a> -->
</div>

<h1 align="center">Hellomlops MlFlow Hook</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/Hellomlops?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Hellomlops 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

MlFlow Cron Helm Chart to track changes between Mlflow and Seldon Deployments

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Helm](https://helm.sh/docs/helm/helm_install/)

## :checkered_flag: Starting ##

```bash

$ helm repo add HelloMLOps https://HelloMLOps.github.io/helm-charts

$ helm install hello-mlflow HelloMLOps/mlflow-hook

```


## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config.MLFLOW_TRACKING_URI | string | `"http://mlflow-service.mlflow.svc.cluster.local:5000"` | Mlflow URI |
| config.MLFLOW_STAGE | string | `"Production"` | Stage To be Tracked From Mlflow  |
| config.DEPLOY_NAMESPACE | string | `"default"` | Model Namespace |
| config.MLFLOW_DEPLOY_NAME| string | `""` | Seldon Model Name |


## :airplane: To Deploy New Version With Mlflow ##

Transition The version of Model in Mlflow UI

<img width="1404" alt="Screenshot 2022-05-08 at 2 19 10 PM" src="https://user-images.githubusercontent.com/62284209/167296179-3411891e-19c1-46e1-9c80-643b8a52eccf.png">

---
Cron Job Picks up and Patches the Changes to Seldon Core

<img width="914" alt="Screenshot 2022-05-08 at 2 20 27 PM" src="https://user-images.githubusercontent.com/62284209/167296195-afbbf844-bb0d-43f5-a25e-30b4c514bfa6.png">

---

## :chains: How The flow Works

<img width="1169" alt="Screenshot 2022-05-08 at 2 24 45 PM" src="https://user-images.githubusercontent.com/62284209/167296234-28e754ed-b17e-4afd-9da2-f7c877860375.png">

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>

&#xa0;

<a href="#top">Back to top</a>
