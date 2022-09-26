import reports
import os
import emails

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48]]

reports.generate("report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "mpono000@gmail.com"
receiver = "mpono000@gmail.com"
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."
password = 'rstaccqtruorfkem'

message = emails.generate(sender, receiver, subject, body, "report.pdf")
emails.send(message, sender, password)
