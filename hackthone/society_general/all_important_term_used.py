# ==========================================================
# HACKATHON CYBERSECURITY & COMPLIANCE GLOSSARY
# ==========================================================

# ----------------------------------------------------------
# 1. IAM (Identity and Access Management)
# ----------------------------------------------------------

# Meaning:
# System that manages WHO can access WHAT.

# Example:
# Piyush = Developer
# Access = GitHub + Database

# IAM decides:
# - Who are you?
# - What can you access?
# - What actions can you perform?

# Real Life:
# College ID card.
# Student can enter classroom.
# Teacher can enter staff room.
# Principal can enter everywhere.

# ----------------------------------------------------------
# 2. Identity Sprawl
# ----------------------------------------------------------

# Meaning:
# Same user has accounts in many systems.

# Example:
# Piyush account exists in:
# - Active Directory
# - AWS
# - GitHub
# - Salesforce
# - Database

# Risk:
# Security team loses track of permissions.

# ----------------------------------------------------------
# 3. Privilege
# ----------------------------------------------------------

# Meaning:
# Permission granted to a user.

# Example:
# Read File
# Write File
# Delete File
# Admin Access

# Higher privilege = More power.

# ----------------------------------------------------------
# 4. Privilege Abuse
# ----------------------------------------------------------

# Meaning:
# User misuses permissions.

# Example:
# HR employee accesses Finance records.

# Example:
# Developer deletes production database.

# ----------------------------------------------------------
# 5. Principle of Least Privilege (PoLP)
# ----------------------------------------------------------

# Golden Rule of Security

# Meaning:
# User should get only minimum permissions required.

# Example:
# Intern needs:
# - Read Access

# Intern should NOT get:
# - Admin Access
# - Delete Database Access

# ----------------------------------------------------------
# 6. Active Directory (AD)
# ----------------------------------------------------------

# Microsoft's identity management system.

# Stores:
# - Users
# - Passwords
# - Permissions

# Example:
# Company login account.

# ----------------------------------------------------------
# 7. Azure AD / Microsoft Entra ID
# ----------------------------------------------------------

# Cloud version of identity management.

# Example:
# Login to Office365 using company account.

# ----------------------------------------------------------
# 8. AWS IAM
# ----------------------------------------------------------

# Amazon's Identity and Access Management system.

# Controls:
# - Users
# - Roles
# - Permissions

# Example:
# Who can create EC2?
# Who can delete S3 bucket?

# ----------------------------------------------------------
# 9. Service Account
# ----------------------------------------------------------

# Non-human account.

# Used by applications.

# Example:
# Backend service connecting to database.

# Risk:
# Forgotten service accounts become attack targets.

# ----------------------------------------------------------
# 10. Inactive User
# ----------------------------------------------------------

# User not logged in for long time.

# Example:
# Employee left company 6 months ago.

# Risk:
# Account may be hacked.

# ----------------------------------------------------------
# 11. Risk Score
# ----------------------------------------------------------

# Numeric representation of danger.

# Example:

# Admin Access = +30
# Sensitive Data = +20
# Inactive User = +40

# Total Risk = 90/100

# Higher score = Higher danger

# ----------------------------------------------------------
# 12. Sensitive Data
# ----------------------------------------------------------

# Important confidential information.

# Examples:
# - Aadhaar
# - PAN
# - Customer Records
# - Bank Details
# - Credit Card Numbers

# ----------------------------------------------------------
# 13. Security Control
# ----------------------------------------------------------

# Protection mechanism.

# Examples:
# Firewall
# Encryption
# Antivirus
# Logging
# MFA

# ----------------------------------------------------------
# 14. Firewall
# ----------------------------------------------------------

# Security gate of network.

# Controls incoming/outgoing traffic.

# Example:
# Port 22 blocked.

# Prevents unauthorized access.

# ----------------------------------------------------------
# 15. Port
# ----------------------------------------------------------

# Communication endpoint.

# Examples:
# 80 = HTTP
# 443 = HTTPS
# 22 = SSH

# Hackers often target open ports.

# ----------------------------------------------------------
# 16. Configuration
# ----------------------------------------------------------

# Settings of a system.

# Example:
# Encryption = ON
# Firewall = Enabled

# ----------------------------------------------------------
# 17. Misconfiguration
# ----------------------------------------------------------

# Wrong security settings.

# Example:
# Database exposed publicly.

# One of the biggest causes of cloud breaches.

# ----------------------------------------------------------
# 18. Configuration Drift
# ----------------------------------------------------------

# Actual configuration differs from intended configuration.

# Example:

# Policy:
# Encryption = ON

# Current:
# Encryption = OFF

# This difference is called Drift.

# ----------------------------------------------------------
# 19. Encryption
# ----------------------------------------------------------

# Converts readable data into unreadable form.

# Example:

# Original:
# password123

# Encrypted:
# X8f9K@2Lm#

# Only authorized users can read it.

# ----------------------------------------------------------
# 20. Logging
# ----------------------------------------------------------

# Recording activities in system.

# Example:

# User Login
# File Download
# Password Change

# Logs help investigations.

# ----------------------------------------------------------
# 21. Audit
# ----------------------------------------------------------

# Inspection of security controls.

# Example:
# Auditor checks:
# - Encryption enabled?
# - Backups working?
# - Logs retained?

# ----------------------------------------------------------
# 22. Compliance
# ----------------------------------------------------------

# Following required rules and standards.

# Example:
# Company follows GDPR.

# Then company is compliant.

# ----------------------------------------------------------
# 23. NIST
# ----------------------------------------------------------

# National Institute of Standards and Technology

# US Cybersecurity Framework.

# Functions:
# - Identify
# - Protect
# - Detect
# - Respond
# - Recover
# - Govern

# Think:
# Cybersecurity Rule Book

# ----------------------------------------------------------
# 24. GDPR
# ----------------------------------------------------------

# General Data Protection Regulation

# European privacy law.

# Protects user personal data.

# Example:
# User can request:
# "Delete my data"

# Company must comply.

# ----------------------------------------------------------
# 25. RBI Guidelines
# ----------------------------------------------------------

# Rules issued by Reserve Bank of India.

# Focus:
# Banking Security
# Digital Payments
# Customer Protection

# ----------------------------------------------------------
# 26. Evidence
# ----------------------------------------------------------

# Proof that a control exists.

# Example:

# Policy:
# Database must be encrypted.

# Evidence:
# Screenshot showing encryption enabled.

# ----------------------------------------------------------
# 27. Audit Evidence Collection
# ----------------------------------------------------------

# Gathering proof automatically.

# Example:
# Fetch database encryption status.

# Store as evidence.

# ----------------------------------------------------------
# 28. Insider Threat
# ----------------------------------------------------------

# Threat coming from inside organization.

# Example:
# Employee steals customer data.

# Example:
# Disgruntled worker leaks confidential files.

# ----------------------------------------------------------
# 29. Access Log
# ----------------------------------------------------------

# Record of user activity.

# Example:

# User: Rahul
# Time: 2:00 AM
# Action: Download

# ----------------------------------------------------------
# 30. Anomaly Detection
# ----------------------------------------------------------

# Detect unusual behavior.

# Example:

# Normal:
# 50 downloads/day

# Today:
# 5000 downloads

# Anomaly Detected.

# ----------------------------------------------------------
# 31. Isolation Forest
# ----------------------------------------------------------

# Machine Learning algorithm.

# Used for anomaly detection.

# Idea:
# Unusual points are isolated faster.

# Example:
# User downloads 5000 files at 2 AM.

# Model marks as suspicious.

# ----------------------------------------------------------
# 32. SIEM
# ----------------------------------------------------------

# Security Information and Event Management

# Collects logs from multiple systems.

# Example:
# Splunk
# QRadar

# Purpose:
# Detect attacks.

# ----------------------------------------------------------
# 33. SOC
# ----------------------------------------------------------

# Security Operations Center

# Team responsible for monitoring security.

# They investigate alerts.

# ----------------------------------------------------------
# 34. MFA (Multi-Factor Authentication)
# ----------------------------------------------------------

# Multiple proofs of identity.

# Example:
# Password + OTP

# More secure than password alone.

# ----------------------------------------------------------
# 35. Zero Trust
# ----------------------------------------------------------

# Security philosophy:

# "Never Trust, Always Verify"

# Every user and device must be verified.

# Even inside company network.

# ==========================================================
# MOST IMPORTANT HACKATHON WORDS TO REMEMBER
# ==========================================================

# IAM
# Identity Sprawl
# Privilege
# Least Privilege
# Risk Score
# Service Account
# Compliance
# Audit
# Evidence
# Configuration Drift
# Misconfiguration
# Encryption
# Logging
# Insider Threat
# Anomaly Detection
# NIST
# GDPR
# RBI
# Zero Trust
# MFA
# Isolation Forest