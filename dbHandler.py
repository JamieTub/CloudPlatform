import boto3
from botocore.exceptions import ClientError

def create_table(name):
    #accessing the dynamoDB api here
    cloudFormation = boto3.client('cloudformation')

    template_url = "https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/DynamoDB_Table.template"

    try:
        res = cloudFormation.create_stack(
            StackName = name,
            TemplateURL = template_url,
            Parameters = [{
                'ParameterKey': 'HashKeyElementName',
                'ParameterValue': 'trackname'
            }]
        )

        print(name + ' was created.')
        return res

    except Exception as err:
        print("Database already exists.")