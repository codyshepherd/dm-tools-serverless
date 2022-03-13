# dm-tools Serverless Deployment Setup

## To Deploy:

* `cdk synth`
* `cdk --profile <your profile> --region <your region> deploy`

## Description

This repo contains the CDK config and application code required for deploying `dm-tools` as a trio of AWS Lambda
functions behind an API Gateway in AWS. 

### Additional Configuration Required

Additional once-per-deployment manual config will be necessary to correctly set up an alternate domain name to point
at this deployment:

* purchase and register a domain name
* in AWS Route 53, request a certificate
  * add the DNS validation CNAME record under the domain in your domain registrar
* In the API Gateway web console, create a "Custom Domain Name" with your (sub)domain of choice and map it to the API
  Gateway stage of your choice (`prod` by default).
* create a CNAME record for your (sub)domain of choice mapping the (sub)domain to the API Gateway endpoint
* create one or more API Keys to allow services to call this API and protect yourself from overages by malicious actors