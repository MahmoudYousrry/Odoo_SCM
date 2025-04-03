# Student Course Management (SCM) System - Odoo18 Module

## Overview:
This Odoo module provides a comprehensive Student Course Management (SCM) system with features for managing students, tracks, skills, courses, and their relationships. It includes custom security rules, reporting, and integration with the HR module.

## Features:

### Core Models:
- **Students**: Manage student information including personal details, academic status, and financials.
- **Tracks**: Organize students into different academic tracks with capacity management.
- **Skills**: Track student skills with many-to-many relationships.
- **Courses**: Manage course offerings and student grades.

### Key Functionality:
- **Student Lifecycle Management**: From application to interview stages (Applied, First Interview, Second Interview, Passed, Rejected).
- **Automatic Email Generation**: Based on student names during creation.
- **Financial Calculations**: Automatic tax and net salary computation.
- **Track Capacity Management**: Prevent over-enrollment in tracks.
- **Gender-based Rules**: Different salary defaults and track visibility based on gender.
- **Reporting**: PDF report generation for student data.

## Security:
- **Two-tier user groups**: (Normal User and Manager)
- **Custom access rules**:
  - Normal users can only see students they created.
  - Managers have full access.
- **Granular permissions** for each model.

## Integration:
- **Extends HR Employee module** to add military certificate field.
- **Inherits and extends standard HR views**.

## Installation:
1. Clone this repository into your Odoo addons directory.
2. Install the module through Odoo Apps or command line.

## Usage:
After installation:
- Navigate to the SCM menu.
- Use the Students submenu to manage student records.
- Managers can access the Tracks submenu to manage academic tracks.

## Technical Details:
- **Python models** for business logic.
- **XML views** for user interface.
- **QWeb templates** for PDF reporting.
- **Security rules and access controls**.
- **Inherited views** for HR module extension.

## Dependencies:
- Odoo HR module (for the extension features).

## License:
- This module is released under the MIT License.
