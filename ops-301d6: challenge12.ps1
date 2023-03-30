<# Script: Ops 301 Class 13 Ops Challenges 12: PowerShell AD Automation
 Author: Alexander Echols 
 Date of Creation 29 Mar 2023 
 Date of last revision: 29 Mar 2023 
 purpose: This script will add a new person to an AD #>

# First we need to prompt the user for the info of the new employee
$fName = Read-Host "What is the First name?"
$lName = Read-Host "Now the last name?"
# Then we use that info to create a display name for the user 
$dName = "$fName $lName"
# Next we will display their new display name 
Write-Host "Display Name: $dName"
# get thier email 
$eMail = Read-Host "What is the email?"
# department 
$dPart = Read-Host "What department are they in?"
# thier role 
$tRole = Read-Host "What is their role?"
# thier State
$sName = Read-Host "What state do they live in?"
# now we put it all together and create the new user with the New-ADUser command
New-ADUser -Name $dName -GivenName $fName -Surname $lName -EmailAddress $eMail -Department $dPart -Company "GlobeX" -State $sName -Country "United States" -Title $tRole -AccountPassword (ConvertTo-SecureString "P@ssword123" -AsPlainText -Force) -Enabled $true