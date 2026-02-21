# Smart Inventory & Billing System with Sales Analytics

A cloud-deployed retail inventory and sales analytics system built using Python, PostgreSQL, and Streamlit.
This project models real-world grocery store operations with structured data management and interactive revenue insights.

 1) Live Demo

🌐 Live App: https://smart-inventory-and-billing-system.onrender.com

💻 GitHub Repository: https://github.com/sahil15573/smart-inventory-and-billing-system

2) Problem Statement

Small and medium-sized retail stores often rely on manual or disconnected systems for managing inventory and tracking sales. This leads to stock inconsistencies, inefficient billing, and limited visibility into revenue trends.

This project addresses that problem by building a database-driven inventory and billing system integrated with real-time sales analytics to support accurate tracking and data-driven decision-making.

3) Project Overview

The system simulates a real-world grocery store environment where:

Customers are recorded and managed

Products are tracked with inventory quantities

Sales transactions are stored with relational integrity

Bills are generated automatically

Sales analytics are visualized through an interactive dashboard

4) System Architecture

Backend: Python

Database: PostgreSQL (Normalized relational schema)

Frontend: Streamlit dashboard

Deployment: Render (Cloud PostgreSQL Integration)

5) Database Design

The system uses a normalized relational schema with foreign key constraints:

Customers – Customer information

Products – Inventory details and stock levels

Sales – Transaction records

SaleItems – Line-item mapping between sales and products

This ensures data integrity and realistic retail modeling.

6) Sales Analytics Implemented

Total Revenue Calculation

Sales Summary Dashboard

Product Performance Tracking

Customer Purchase Analysis

Inventory Monitoring

SQL Aggregations using JOIN, GROUP BY, HAVING, SUM, COUNT

7) Key Features

Add and manage customers and products

Record and store sales transactions

Automated bill generation

Real-time sales summary dashboard

Low stock tracking

Cloud-based deployment with persistent database

8) Tech Stack

Python
PostgreSQL
SQL
Streamlit
Render (Cloud Deployment)

9) Future Improvements

Monthly revenue trend visualization
Top-selling product analytics
CSV export functionality
Authentication system
Inventory demand forecasting
The application is fully deployed on Render with a cloud PostgreSQL database, enabling real-time access.

