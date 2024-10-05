/*Les clients ayant consenti à recevoir des communications marketing*/
SELECT *
FROM Client
WHERE Consentement_Marketing = 1;


/*Les commandes du client 5*/
SELECT *
FROM Commande
WHERE Client_ID = 5;

/*Le montant total des commandes du client avec ID n° 61 :*/
SELECT SUM(Montant_Commande) AS Montant_Total
FROM Commande
WHERE Client_ID = 61;


/* Les clients ayant passé des commandes de plus de 100 euros :*/
SELECT DISTINCT Client.*
FROM Client
JOIN Commande ON Client.Client_ID = Commande.Client_ID
WHERE Commande.Montant_Commande > 100;

/*Les clients ayant passé des commandes après le 01/01/2023 :*/
SELECT DISTINCT Client.*
FROM Client
JOIN Commande ON Client.Client_ID = Commande.Client_ID
WHERE Commande.Date_Commande > '2023-01-01';


