"""
==========================================================
PS1 : IDENTITY SPRAWL & PRIVILEGE ABUSE DETECTION
==========================================================
"""

# ---------------------------------------------------------
# WHAT IS IDENTITY?
# ---------------------------------------------------------

# Identity means a digital person/account inside company.

# Example:
# Piyush has:
# - Email Account
# - GitHub Account
# - AWS Account
# - Database Account

# All together represent your Identity.


"""
REAL LIFE EXAMPLE

When you join a company:

Role = Intern

You receive:
- Email Access
- Git Access
- Database Read Access

After promotion:

Role = Developer

New permissions are added.

Problem:
Old permissions are never removed.
"""


# ---------------------------------------------------------
# WHAT IS IDENTITY SPRAWL?
# ---------------------------------------------------------

# Identity Sprawl means same user exists in many systems.

# Example:

# Active Directory
# Azure AD
# AWS IAM
# Salesforce
# Database

# User account exists everywhere.

# Security team loses visibility.


# ---------------------------------------------------------
# WHAT IS PRIVILEGE?
# ---------------------------------------------------------

# Privilege = Permission

# Examples:

# Read Database
# Write Database
# Delete Database
# Create User
# Admin Access

# More privilege = More power


# ---------------------------------------------------------
# WHAT IS PRIVILEGE ABUSE?
# ---------------------------------------------------------

# Using permissions in dangerous way.

# Example:

# HR employee accesses Finance records.

# Developer deletes production database.

# Employee steals customer data.


# ---------------------------------------------------------
# PRINCIPLE OF LEAST PRIVILEGE (PoLP)
# ---------------------------------------------------------

"""
Golden Rule of Cybersecurity

Give users only minimum permissions required.
"""

# Example:

# Intern:
# Needs Read Access

# Intern DOES NOT NEED:
# Admin Access
# Delete Access

# Extra permissions = Security Risk


# ---------------------------------------------------------
# WHAT SHOULD TEAM BUILD?
# ---------------------------------------------------------

# Collect user identities.

user = {
    "name":"piyush",
    "role":"developer",
    "permissions":[
        "read_db",
        "write_db",
        "admin_server"
    ]
}

# Detect risky users.

# Example Rules:

# Admin Access
# +
# Inactive 60 Days
# =
# High Risk

# Generate Risk Score

# Risk = 90/100

# Suggest:
# Remove Admin Rights
# Disable Account


"""
Winning Output

Risk Score
Risk Level
Reason
Recommended Action
"""



"""
==========================================================
PS2 : SECURITY CONTROL DRIFT & MISCONFIGURATION DETECTION
==========================================================
"""

# ---------------------------------------------------------
# WHAT IS SECURITY CONTROL?
# ---------------------------------------------------------

# Security Control = Protection Mechanism

# Examples:

# Firewall
# Encryption
# Logging
# MFA
# Antivirus

# These protect company systems.


# ---------------------------------------------------------
# WHAT IS CONFIGURATION?
# ---------------------------------------------------------

# Configuration = Settings of system

# Example:

config = {
    "firewall":"enabled",
    "encryption":"enabled",
    "logging":"enabled"
}


# ---------------------------------------------------------
# WHAT IS MISCONFIGURATION?
# ---------------------------------------------------------

# Wrong security setting.

# Example:

config = {
    "firewall":"enabled",
    "encryption":"disabled"
}

# Encryption should be ON.

# It is OFF.

# This is Misconfiguration.


"""
Many cloud breaches happen because
of simple misconfigurations.
"""


# ---------------------------------------------------------
# WHAT IS CONFIGURATION DRIFT?
# ---------------------------------------------------------

"""
Expected Configuration

Encryption = ON

Current Configuration

Encryption = OFF

Difference between expected and current
configuration is called DRIFT.
"""

# Example Timeline

# May 1  -> ON
# May 5  -> OFF
# May 10 -> OFF

# Drift Detected


# ---------------------------------------------------------
# WHAT SHOULD TEAM BUILD?
# ---------------------------------------------------------

# Store ideal configuration

ideal = {
    "encryption":"enabled",
    "firewall":"enabled"
}

# Compare actual configuration

actual = {
    "encryption":"disabled",
    "firewall":"enabled"
}

# Find differences.

# Alert:

# Encryption Disabled
# Severity = HIGH


"""
Winning Output

Drift Timeline
Severity Level
Impact
Suggested Fix
"""



"""
==========================================================
PS3 : AUTOMATED COMPLIANCE EVIDENCE COLLECTION & AUDIT
==========================================================
"""

# ---------------------------------------------------------
# WHAT IS COMPLIANCE?
# ---------------------------------------------------------

# Compliance means following rules.

# Examples:

# NIST
# GDPR
# RBI Guidelines

# If company follows rules:
# Company is Compliant.


# ---------------------------------------------------------
# WHAT IS NIST?
# ---------------------------------------------------------

"""
National Institute of Standards and Technology

Cybersecurity framework.

Functions:

1. Identify
2. Protect
3. Detect
4. Respond
5. Recover
6. Govern

Think:
Cybersecurity Rule Book
"""


# ---------------------------------------------------------
# WHAT IS GDPR?
# ---------------------------------------------------------

"""
General Data Protection Regulation

European Privacy Law.

Protects user data.

Example:

User says:
Delete my data.

Company must comply.
"""


# ---------------------------------------------------------
# WHAT IS RBI GUIDELINE?
# ---------------------------------------------------------

"""
Rules issued by Reserve Bank of India.

Focus:
- Banking Security
- Digital Payments
- Customer Protection
"""


# ---------------------------------------------------------
# WHAT IS AUDIT?
# ---------------------------------------------------------

# Security Inspection

# Auditor asks:

# Show proof encryption enabled.
# Show proof backups exist.
# Show proof logs retained.


# ---------------------------------------------------------
# WHAT IS EVIDENCE?
# ---------------------------------------------------------

# Proof that security control exists.

# Example:

evidence = {
    "database":"customer_db",
    "encryption":"enabled"
}

# This proves encryption exists.


# ---------------------------------------------------------
# BIG PROBLEM
# ---------------------------------------------------------

"""
Evidence is scattered everywhere.

Emails
PDFs
Excel Files
Reports
Screenshots

Finding evidence takes days.
"""


# ---------------------------------------------------------
# WHAT SHOULD TEAM BUILD?
# ---------------------------------------------------------

# Read policy

policy = "All databases must be encrypted"

# Collect evidence

evidence = {
    "db":"customer_db",
    "encryption":"enabled"
}

# Match policy with evidence.

# Generate report.

"""
Requirement : Encryption

Status : PASS

Evidence :
Database Encryption Enabled
"""


# ---------------------------------------------------------
# AI OPPORTUNITY
# ---------------------------------------------------------

"""
LLM can:

Read Policy
Read Evidence
Decide PASS or FAIL

This is why judges may like PS3.
"""


"""
Winning Output

Compliance Status
PASS / FAIL
Evidence Link
Audit Report
Confidence Score
"""



"""
==========================================================
PS4 : DATA ACCESS AUDIT & INSIDER THREAT DETECTION
==========================================================
"""

# ---------------------------------------------------------
# WHAT IS DATA ACCESS?
# ---------------------------------------------------------

# Whenever user reads or downloads data.

# Examples:

# Open File
# Read Database
# Download Customer Records

# All are Data Access Events.


# ---------------------------------------------------------
# WHAT IS ACCESS LOG?
# ---------------------------------------------------------

# Activity record.

log = {
    "user":"rahul",
    "time":"02:30 AM",
    "action":"download",
    "files":5000
}

# Logs help track behavior.


# ---------------------------------------------------------
# WHAT IS INSIDER THREAT?
# ---------------------------------------------------------

"""
Threat coming from inside company.

Examples:

Employee steals data.

Employee copies files to USB.

Employee leaks customer information.

Stolen employee account used by hacker.
"""


# ---------------------------------------------------------
# WHAT IS NORMAL BEHAVIOR?
# ---------------------------------------------------------

# Example:

# Rahul downloads
# 50 files/day

# This becomes baseline.


# ---------------------------------------------------------
# WHAT IS ANOMALY?
# ---------------------------------------------------------

"""
Something unusual.

Normal = 50 files

Today = 5000 files

This is anomaly.
"""


# ---------------------------------------------------------
# WHAT IS ANOMALY DETECTION?
# ---------------------------------------------------------

# Finding unusual activities.

# Example:

# Download at 2 AM
# Massive file transfer
# Access from new location

# System flags as suspicious.


# ---------------------------------------------------------
# ISOLATION FOREST
# ---------------------------------------------------------

"""
Popular Machine Learning Algorithm.

Used for:
Anomaly Detection

Idea:

Unusual records get isolated quickly.

Those become suspicious.
"""


# ---------------------------------------------------------
# WHAT SHOULD TEAM BUILD?
# ---------------------------------------------------------

# Collect logs.

# Learn normal behavior.

# Detect anomalies.

# Assign Risk Score.

# Explain why alert happened.


"""
Example Alert

User : Rahul

Risk : HIGH

Reason:

Downloaded 5000 files

100x higher than normal

Occurred at 2 AM
"""


"""
Winning Output

Top Risky Users
Risk Score
Explanation
Recommended Action
Investigation Report
"""