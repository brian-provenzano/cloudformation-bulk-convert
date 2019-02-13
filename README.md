## Clouformation template conversion (json to yaml) 
Quick script to bulk convert json CFN templates to yaml.  Uses [AWSLabs cfnflip](https://github.com/awslabs/aws-cfn-template-flip)

## Usage
Drop script into parent directory that needs files to be converted to yaml and execute; it will recurse the dir and convert.
NOTE: Overwrites if files exists!!

## Thanks
- [AWSLabs cfnflip python library](https://github.com/awslabs/aws-cfn-template-flip)