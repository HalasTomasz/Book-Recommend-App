export const json = {
    "elements": [
      {
        "type": "checkbox",
        "name": "books",
        "title": "Wybierz 3 ksiązki które byś przeczytał!",
        "isRequired": true,
        "colCount": 4,
        "validators": [
          {
              "type": "answercount",
              "text": "Wybierz 3 ksiązki",
              "minCount": 3,
              "maxCount": 3
          }
          ],
        "choices": [
          "Harry Potter and the Sorcerer`s Stone",
          "The Hunger Games",
          "Twilight",
          "To Kill a Mockingbird",
          "The Great Gatsby",
          "The Fault in Our Stars",
          "1984",
          "Pride and Prejudice",
          "Divergent",
          "The Hobbit, or There and Back Again",
          "Harry Potter and the Deathly Hallows",
          "Harry Potter and the Prisoner of Azkaban",
          "The Diary of a Young Girl",
          "Animal Farm",
          "The Catcher in the Rye",
          "Harry Potter and the Chamber of Secrets",
          "Angels & Demons",
          "The Girl with the Dragon Tattoo",
          "Harry Potter and the Goblet of Fire",
          "Catching Fire",
          "Harry Potter and the Order of the Phoenix",
          "Harry Potter and the Half-Blood Prince",
          "The Kite Runner",
          "The Fellowship of the Ring",
          "Mockingjay",
          "Gone Girl",
          "Lord of the Flies",
          "The Help",
          "The Lion, the Witch and the Wardrobe",
          "The Girl on the Train",
          "The Alchemist",
          "Romeo and Juliet",
          "The Lovely Bones",
          "A Game of Thrones",
          "The Lightning Thief",
          "Fifty Shades of Grey",
          "Of Mice and Men",
          "The Da Vinci Code",
          "The Book Thief",
          "The Giver",
          "Memoirs of a Geisha",
          "Little Women",
          "Fahrenheit 451",
          "Jane Eyre",
          "City of Bones",
          "The Time Traveler`s Wife",
          "Eat, Pray, Love",
          "New Moon",
          "The Handmaid`s Tale",
          "Brave New World"
        ]
      }, {
        "type": "comment",
        "name": "rating",
        "title": "Polecane gatunki",
        "readOnly": true,
        "visibleIf": "rowsWithValue({books}) == 3"
      },
      {
        "type": "rating",
        "name": "algo1",
        "title": "Jak oceniasz rekomedację algorytmu nr 1?",
        "rateMax": 10,
        "isRequired": true,
        "visibleIf": "rowsWithValue({books}) == 3"
      }, {
        "type": "comment",
        "name": "rating2",
        "title": "Polecane gatunki",
        "readOnly": true,
        "visibleIf": "rowsWithValue({books}) == 3"
      },
      {
        "type": "rating",
        "name": "algo2",
        "isRequired": true,
        "title": "Jak oceniasz rekomedację algorytmu nr 2?",
        "rateMax": 10,
        "visibleIf": "rowsWithValue({books}) == 3"
      }
    ],
    "triggers": [
        {
          "type": "runexpression",
          "expression": "{books} notempty",
          "runExpression": "setName('rating', {books})"
        },
        {
          "type": "runexpression",
          "expression": "{books} notempty",
          "runExpression": "setName2('rating2', {books})"
        }
      ]
  };