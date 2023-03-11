# Service bank

For debug use: ModHeader(extension in chrome) and Postman

#### Endpoints:
- api/account For create accounts*, viewing accounts and history of transactions

*Accounts can be presented in the form of bank cards

----

- api/customer/ For create info about user*

*User != account. User can have many accounts(cards)

---

- api/transaction For make transactions between different users accounts(cards) and between accounts(cards) of the same user

---

Default by djoser: </br>
/auth/token/login for get Token

