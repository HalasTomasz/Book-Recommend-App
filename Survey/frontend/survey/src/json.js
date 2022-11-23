export const json = {
    "elements": [
      {
        "type": "checkbox",
        "name": "books",
        "title": "Która ksiązke przcytałbys?",
        "isRequired": true,
        "colCount": 4,
        "choices": [
          "Ford",
          "Vauxhall",
          "Volkswagen",
          "Nissan",
          "Audi",
          "Mercedes-Benz",
          "BMW",
          "Peugeot",
          "Toyota",
          "Citroen",
          "Ford1",
          "Vauxhall1",
          "Volkswagen1",
          "Nissan1",
          "Audi2",
          "Mercedes-Benz3",
          "BMW4",
          "Peugeot5",
          "Toyota6",
          "Citroen7"
        ]
      }, {
        "type": "text",
        "name": "rating",
        "title": "Polecane gatunki",
        "readOnly": true,
        "visibleIf": "rowsWithValue({books}) == 3"
      },
      {
        "type": "rating",
        "name": "algo1",
        "title": "Jak oceniasz rekomedacje algorytmu nr 1",
        "rateMax": 10,
        "visibleIf": "rowsWithValue({books}) == 3"
      }
    ],
    "triggers": [
        {
          "type": "runexpression",
          "expression": "{books} notempty",
          "runExpression": "setName('rating', {books})"
        }
      ]
  };