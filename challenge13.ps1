# Script: Ops 301 Class 13 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/29/23
# Purpose: Write a Powershell script that adds the below person to AD
# Resources: chatgpt helped with creating the new user by explaining it line by line to me. 




# Set the variables for the new user
$givenName = "Franz"
$surname = "Ferdinand"
$displayName = "$givenName $surname"
$samAccountName = "ferdinandf"
$userPrincipalName = "ferdi@GlobeXpower.com"
$description = "TPS Reporting Lead at GlobeX USA in Springfield, OR office"
$department = "TPS Department"

# Create the new user
New-ADUser `
    -Name $displayName `
    -GivenName $givenName `
    -Surname $surname `
    -SamAccountName $samAccountName `
    -UserPrincipalName $userPrincipalName `
    -Description $description `
    -Department $department `
    -AccountPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) `
    -Enabled $true `
    -Path "OU=Users,DC=corp.globexpower,DC=com"