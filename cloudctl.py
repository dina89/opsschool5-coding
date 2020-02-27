import click
import boto3
from tabulate import tabulate

client = boto3.client('ec2', region_name='us-east-1')


@click.group()
@click.pass_context
def cloudctl(ctx):
    """ Cloud Manager cli """


@cloudctl.group()
@click.pass_context
def get(ctx):
    """ get object """


@get.command()
@click.pass_context
def instances(ctx):
    instance_table = []
    """ get instances """
    response = client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_row = [instance["InstanceId"],instance["Monitoring"]["State"],instance["KeyName"]]
            instance_table.append(instance_row)       
    print(tabulate(instance_table, headers=['InstanceId', 'State', 'Name']))

def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()