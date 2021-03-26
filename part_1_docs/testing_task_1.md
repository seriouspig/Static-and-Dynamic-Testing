### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  # Should be comparing with == rather than assigning with =
      return True
    else                # Colon missing after else
      return False
   
  dif highest_card(self, card1 card2):  # def is misseplled (dif) , coma missing between card1 and card2
  if card1.value > card2.value:         # the whole if else block should be indented to the right
    return card                         # should be card1 not card
  else:
    return card2
  
def cards_total(self, cards):           # whole def block should be intented on the same level as other functions within the class
  total                                 # need to assign total=0
  for card in cards:
    total += card.value
    return "You have a total of" + total  # return should be at the same level of indentation as for card in cards
                                          # return f"You have a total of {total}"
  
```
