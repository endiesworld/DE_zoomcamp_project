# Data Overview
This dataset surfaces data from the Ethereum Goerli testnet blockchain and includes tables for blocks, transactions, logs, and more.

Ethereum is a decentralized open-source blockchain system that features its own cryptocurrency, Ether. A blockchain is an ever-growing tree of blocks. Each block contains a number of transactions.

The Goerli testnet is a testnet of the Ethereum network. It enables developers to deploy, test, and execute their dApps in the blockchain environment risk-free and at no cost.

For more information, see the Blockchain Analytics documentation .

This public dataset is hosted in Google BigQuery and is included in BigQuery's 1TB/mo of free tier processing. This means that each user receives 1TB of free BigQuery processing every month, which can be used to run queries on this public dataset. Watch this short video to learn how to get started quickly using BigQuery to access public datasets.


# Project Overview
1. Visualize the numbers of failed and successful transactions
2. Reveal the to 10 most active addresses
3. Show the monthly transction count

# Running this project

## Prerequisites
>> Install docker and docker-compose in your machine
>> An active google cloud service account
>> Create and download google cloud service account key to the main project directory


## Download and run the project
>> git clone https://github.com/endiesworld/DE_zoomcamp_project.git
>> sudo lsof -i :6789 <!-- This act is to confirm that port 6789 is free on the machine you intend to run this application on-->
>> docker stop $(docker ps -q) <!-- Only do this if another docker container is using port 6789 -->
>> docker compose build <!-- To build the project -->
>> Save the path to your google cloud service key as a value in the 'GOOGLE_SERVICE_ACC_KEY_FILEPATH:' in the file 'io_config.yml' in the 'magic-zoomcamp' dir.




