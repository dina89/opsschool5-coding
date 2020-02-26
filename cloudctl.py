import click
import boto3

client = boto3.client('ec2', region_name='us-east-1')


@click.group()
@click.pass_context
def cloudctl(ctx):
    """ Cloud Manager cli """


@cloudctl.group()
@click.pass_context
def get(ctx):
    """ get object """
    print(ctx)


@get.group()
@click.pass_context
def instances(ctx):
    """ get instances """
    response = client.describe_instances()
    print(response)
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
             print(instance)
    print(ctx)


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()