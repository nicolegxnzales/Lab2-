# lab 2
# KSU CCSE Hackathon Food Cost Calculator

## Description

This Python program calculates the food costs for the KSU CCSE hackathon. The hackathon provides two meal options: pizza and salad. The program asks for the number of people who ordered each option and calculates the total cost, including any applicable discounts and delivery fees.

## Features

- **Pizza Orders**: Each person who orders pizza is allocated three (3) slices. Each pizza costs $15.99 and has 12 slices. The program calculates the total number of pizzas needed.
- **Salad Orders**: Each salad costs $7.99 per person.
- **Discounts**: 
  - A 15% discount is applied to the pizza cost if more than 10 pizzas are ordered.
  - A 15% discount is applied to the salad cost if more than 10 salads are ordered.
- **Delivery Fee**: The delivery fee is calculated as 7% of the total order cost before discounts, with a minimum delivery fee of $20.

## Input

The program prompts the user to input:
1. The number of people who ordered pizza.
2. The number of people who ordered salad.

## Output

The program calculates and displays:
- The total number of pizzas needed.
- The cost of the pizzas (before discounts).
- The cost of the salads (before discounts).
- The total discount amount.
- The delivery fee.
- The total amount due.

### Example

**Input:**
```plaintext
Number of pizza orders: 43
Number of salad orders: 7
