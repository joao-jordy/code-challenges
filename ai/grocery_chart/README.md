# Grocery Chart

### Challenge Description

Application Requirements
The application should take an input (via any preferred input method, UI or command prompt) of a list of purchases made by a customer which includes:
* The name of the item 
* The cost of the item 
The application should calculate the total of all the items and display it. 
The application should have a drop down allowing the user to choose their US State from a list of all US States. 
* If the customer selected any of the following states, then the application will apply an 8% sales tax to the total calculated in #1 : California, Texas, New York or Florida 
* If the customer selected any of the following states, then the application will apply an 5% sales tax to the total calculated in #1 : Washington, Oregon, Idaho, Utah, Montana, New Mexico, Arizona, Wyoming, Kansas, Arkansas, Georgia, Alabama or Louisiana.  
* The application should not apply a tax to the total for any other states 
The total should update automatically when the user makes their selection or make their purchase item entry.

---

### Proposed Solution

#### Assumptions
* <strike>Use any tool for recording my screen while coding.</strike>
* <strike>Publish the record to a video sharing platform.</strike>
* Publish the source-code to my own github repo.
* This is a very open scope by design.
* The implementation will follow a single page JavaScript app.
* Generative AI will be used as base tool.

#### Prompt (Google Gemini)

```
  I'm acting as a requester for a develop team and I have some Application Requirements:
  1. The application should present a select list filled with dozens of grocery products which includes the name of the item and the cost of the item.
  2. The application should allow to select a product in the list and input the amount to buy.
  3. Many products can be selected and the buying list should be represented in the screen, line by line, with product name, unit cost and total cost per product.
  4. The application should calculate the total of all the items and display it. 
  5. The application should have a drop down allowing the user to choose their US State from a list of all of 51 US States, even not having a tax.
  5.1 * If the customer selected any of the following states, then the application will apply an 8% sales tax to the total calculated in #1 : California, Texas, New York or Florida 
  5.2 * If the customer selected any of the following states, then the application will apply an 5% sales tax to the total calculated in #1 : Washington, Oregon, Idaho, Utah, Montana, New Mexico, Arizona, Wyoming, Kansas, Arkansas, Georgia, Alabama or Louisiana.  
  5.3 * The application should not apply a tax to the total for any other states 
  6. The total should update automatically when the user makes their selection or make their purchase item entry.
  7. This implementation should be made as a single page application in JavaScript as HTML single file, to be executed at client side (internet browsers).
  8. Apply to this a professional bootstrap theme for e-commerce.
  9. Make sure that the grocery list is properly loaded.
  10. Make sure that the grand total is showing the proper value.
  11. Minify the products into a map
  12. Change the state-select to be loaded by javascript, and then, Minify the states plus the taxes into a single structure containing the state name and the correspondent tax.
  13. Be as much economic as possible in the code length, keeping state data in one variable only.
  14. Should be possible to add, update and remove the product from the buying list.
```
