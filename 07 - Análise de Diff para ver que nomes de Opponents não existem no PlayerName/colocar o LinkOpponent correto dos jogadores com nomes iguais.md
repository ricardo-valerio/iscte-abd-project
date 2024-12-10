# 1) Alberto Gonzalez:

"Location": contains "Panama" or "Venezuela"
"Opponent": "Alberto Gonzalez"

$set:
"LinkOpponent": "https://www.atptour.com/en/players/alberto-gonzalez/g975/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------


"Opponent": "Alberto Gonzalez"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/alberto-gonzalez/g419/player-activity?year=all&matchType=Singles"



```js
db.atpplayers.updateMany(
    // filter
    {
        "Location": {
            $in: ["Panama", "Venezuela"]
        },
        "Opponent": "Alberto Gonzalez"
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/alberto-gonzalez/g975/player-activity?year=all&matchType=Singles"
      }
    }
)



db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Alberto Gonzalez",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/alberto-gonzalez/g419/player-activity?year=all&matchType=Singles"
      }
    }
)



```



# 2) Alexey Nesterov:


"Location": contains "U.S.A." or "Russia"
"Opponent": "Alexey Nesterov"

$set:
"LinkOpponent": "https://www.atptour.com/en/players/alexey-nesterov/n0ax/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------


"Opponent": "Alexey Nesterov"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/alexey-nesterov/n645/player-activity?year=all&matchType=Singles"





```js
db.atpplayers.updateMany(
    // filter
    {
      $or: [
      { "Location": { $regex: "U.S.A." } },
      { "Location": { $regex: "Russia" } }
    ],
      "Opponent": "Alexey Nesterov"
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/alexey-nesterov/n0ax/player-activity?year=all&matchType=Singles"
      }
    }
)



db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Alexey Nesterov",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/alexey-nesterov/n645/player-activity?year=all&matchType=Singles"
      }
    }
)



```



# 3) Andreas Weber

"Tournament" and "Location" equal to:

		Tournament	Location
		U.S.A. F28	HI, U.S.A.
		Germany F9	Germany
		U.S.A. F29	HI, U.S.A.
		Germany F9	Germany
		U.S.A. F29	HI, U.S.A.
		Aschaffenburg	Aschaffenburg, Germany

"Opponent": "Andreas Weber"

$set:
"LinkOpponent": "https://www.atptour.com/en/players/andreas-weber/w449/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------

"Opponent": "Andreas Weber"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/andreas-weber/w237/player-activity?year=all&matchType=Singles"



```js
db.atpplayers.updateMany(
  {
    $or: [
      { Tournament: "U.S.A. F28", Location: "HI, U.S.A." },
      { Tournament: "Germany F9", Location: "Germany" },
      { Tournament: "U.S.A. F29", Location: "HI, U.S.A." },
      { Tournament: "Aschaffenburg", Location: "Aschaffenburg, Germany" }
    ],
    Opponent: "Andreas Weber"
  },
  {
    $set: {
      LinkOpponent: "https://www.atptour.com/en/players/andreas-weber/w449/player-activity?year=all&matchType=Singles"
    }
  }
)


db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Andreas Weber",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/andreas-weber/w237/player-activity?year=all&matchType=Singles"
      }
    }
)


```



# 4) Enrique Pena

"Tournament" and "Location" and "Date" equal to:

		Tournament	Location	Date
		Cali	Cali, Colombia	1992.09.28 - 1992.10.04
		Bogota	Bogota, Colombia	1992.09.21 - 1992.09.27

"Opponent": "Enrique Pena"

$set:
"LinkOpponent": "https://www.atptour.com/en/players/enrique-pena/p306/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------

"Opponent": "Enrique Pena"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/enrique-pena/p0iz/player-activity?year=all&matchType=Singles"

```js
db.atpplayers.updateMany(
  {
    $or: [
      { Tournament: "Cali", Location: "Cali, Colombia", Date: "1992.09.28 - 1992.10.04" },
      { Tournament: "Bogota", Location: "Bogota, Colombia", Date: "1992.09.21 - 1992.09.27" }
    ],
    Opponent: "Enrique Pena"
  },
  {
    $set: {
      LinkOpponent: "https://www.atptour.com/en/players/enrique-pena/p306/player-activity?year=all&matchType=Singles"
    }
  }
)


db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Enrique Pena",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/enrique-pena/p0iz/player-activity?year=all&matchType=Singles"
      }
    }
)


```



# 5) Mark Kovacs


"Location": contains "Romania" or "Hungary"
"Opponent": "Mark Kovacs"

$set:
"LinkOpponent": "https://www.atptour.com/en/players/mark-kovacs/kb22/player-activity?year=all&matchType=Singles"

---------------------------------------------------------------------------------------------------------------------------~---~-------------

"Opponent": "Mark Kovacs"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/mark-kovacs/k678/player-activity?year=all&matchType=Singles"



```js
db.atpplayers.updateMany(
    // filter
    {
      $or: [
      { "Location": { $regex: "Romania" } },
      { "Location": { $regex: "Hungary" } }
    ],
      "Opponent": "Mark Kovacs"
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/mark-kovacs/kb22/player-activity?year=all&matchType=Singles"
      }
    }
)



db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Mark Kovacs",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/mark-kovacs/k678/player-activity?year=all&matchType=Singles"
      }
    }
)



```




# 6) Martin Damm


"Tournament" and "Location" and "Date" equal to:

		Tournament	Location	Date
		ATP Masters 1000 Miami	Miami, FL, U.S.A.	2022.03.21 - 2022.04.03
		M25 Bakersfield, CA	Bakersfield, CA, U.S.A.	2022.03.14 - 2022.03.20
		M25 Bakersfield, CA	Bakersfield, CA, U.S.A.	2022.03.14 - 2022.03.20
		M25 Glasgow	Glasgow, Great Britain	2022.02.14 - 2022.02.20
		M25 Bakersfield, CA	Bakersfield, CA, U.S.A.	2022.03.14 - 2022.03.20
		M25 Shrewsbury	Shrewsbury, Great Britain	2022.02.07 - 2022.02.13
		M25 Loughborough	Loughborough, Great Britain	2022.01.24 - 2022.01.30
		M25 Loughborough	Loughborough, Great Britain	2022.01.24 - 2022.01.30
		M25 Columbus	Columbus, OH, U.S.A.	2021.11.15 - 2021.11.21
		M25 Columbus	Columbus, OH, U.S.A.	2021.11.15 - 2021.11.21
		M25 Glasgow	Glasgow, Great Britain	2022.02.14 - 2022.02.20
		Knoxville	Knoxville, TN, U.S.A.	2021.11.08 - 2021.11.14
		Charlottesville	Charlottesville, VA, U.S.A.	2021.11.01 - 2021.11.07
		M25 Toulouse	Toulouse, France	2021.10.18 - 2021.10.24
		M25+H Rodez	Rodez, France	2021.10.11 - 2021.10.17
		M25+H Rodez	Rodez, France	2021.10.11 - 2021.10.17
		M25+H Rodez	Rodez, France	2021.10.11 - 2021.10.17
		M25+H Rodez	Rodez, France	2021.10.11 - 2021.10.17
		M25 Nevers	Nevers, France	2021.10.04 - 2021.10.10
		M25 Nevers	Nevers, France	2021.10.04 - 2021.10.10
		M15 Fayetteville, AR	Fayetteville, AR, U.S.A.	2021.09.20 - 2021.09.26
		M15 Champaign, IL	Champaign, IL, U.S.A.	2021.09.13 - 2021.09.19
		M15 Champaign, IL	Champaign, IL, U.S.A.	2021.09.13 - 2021.09.19
		M15 Champaign, IL	Champaign, IL, U.S.A.	2021.09.13 - 2021.09.19
		M15 Champaign, IL	Champaign, IL, U.S.A.	2021.09.13 - 2021.09.19
		M15 Champaign, IL	Champaign, IL, U.S.A.	2021.09.13 - 2021.09.19
		M25 Champaign	Champaign, IL, U.S.A.	2021.07.26 - 2021.08.01
		M25 Klosters	Klosters, Switzerland	2021.06.21 - 2021.06.27
		M15 Edwardsville	Edwardsville, IL, U.S.A.	2021.07.19 - 2021.07.25
		M15 Skopje	Skopje, Macedonia	2021.06.07 - 2021.06.13
		M15 Skopje	Skopje, Macedonia	2021.06.07 - 2021.06.13
		M15 Skopje	Skopje, Macedonia	2021.06.07 - 2021.06.13
		M15 Skopje	Skopje, Macedonia	2021.05.31 - 2021.06.06
		M15 Skopje	Skopje, Macedonia	2021.05.31 - 2021.06.06
		M25 Most	Most, Czech Republic	2021.05.24 - 2021.05.30
		M15 Valldoreix	Valldoreix, Valldoreix	2021.05.10 - 2021.05.16
		M15 Valldoreix	Valldoreix, Valldoreix	2021.05.10 - 2021.05.16
		Tallahassee	Tallahassee, FL, U.S.A.	2021.04.19 - 2021.04.25
		Orlando	Orlando, FL, U.S.A.	2021.04.12 - 2021.04.18
		Orlando	Orlando, FL, U.S.A.	2021.04.12 - 2021.04.18
		Orlando	Orlando, FL, U.S.A.	2021.04.12 - 2021.04.18
		M15 Opatija	Opatija, Croatia	2021.03.22 - 2021.03.28
		M15 Opatija	Opatija, Croatia	2021.03.22 - 2021.03.28
		M15 Rovinj	Rovinj, Croatia	2021.03.15 - 2021.03.21
		M15 Rovinj	Rovinj, Croatia	2021.03.15 - 2021.03.21
		M15 Rovinj	Rovinj, Croatia	2021.03.15 - 2021.03.21
		M15 Rovinj	Rovinj, Croatia	2021.03.15 - 2021.03.21
		M15 Rovinj	Rovinj, Croatia	2021.03.15 - 2021.03.21
		M15 Porec	Porec, Croatia	2021.03.08 - 2021.03.14
		M15 Porec	Porec, Croatia	2021.03.08 - 2021.03.14
		M25 Naples	Naples, FL, U.S.A.	2021.02.22 - 2021.02.28
		M25 Naples	Naples, FL, U.S.A.	2021.02.22 - 2021.02.28
		M25 Naples	Naples, FL, U.S.A.	2021.02.15 - 2021.02.21
		M25 Naples	Naples, FL, U.S.A.	2021.02.22 - 2021.02.28
		M15 Santo Domingo	Santo Domingo, Dominican Republic	2020.12.07 - 2020.12.13
		M15 Santo Domingo	Santo Domingo, Dominican Republic	2020.11.30 - 2020.12.06
		M15 Santo Domingo	Santo Domingo, Dominican Republic	2020.11.30 - 2020.12.06
		Orlando	Orlando, FL, U.S.A.	2020.11.16 - 2020.11.22
		M15 Fayetteville	Fayetteville, AR, U.S.A.	2020.11.02 - 2020.11.08
		M15 Fayetteville	Fayetteville, AR, U.S.A.	2020.11.02 - 2020.11.08
		M15 Fayetteville	Fayetteville, AR, U.S.A.	2020.11.02 - 2020.11.08
		M15 Monastir	Monastir, Tunisia	2020.10.05 - 2020.10.11
		M15 Monastir	Monastir, Tunisia	2020.09.28 - 2020.10.04
		M15 Curtea de Arges	Curtea de Arges, Romania	2020.09.14 - 2020.09.20
		M15 Curtea de Arges	Curtea de Arges, Romania	2020.09.14 - 2020.09.20
		M15 Bucharest	Bucharest, Romania	2020.09.07 - 2020.09.13
		M15 Antalya	Antalya, Turkey	2020.03.09 - 2020.03.15
		M15 Antalya	Antalya, Turkey	2020.03.02 - 2020.03.08
		M15 Antalya	Antalya, Turkey	2020.03.02 - 2020.03.08
		M25 Naples	Naples, FL, U.S.A.	2019.11.18 - 2019.11.24
		M25 Naples	Naples, FL, U.S.A.	2020.02.10 - 2020.02.16
		M25 Naples	Naples, FL, U.S.A.	2019.11.18 - 2019.11.24
		M25 Naples	Naples, FL, U.S.A.	2019.11.18 - 2019.11.24
		M25 Naples	Naples, FL, U.S.A.	2019.11.18 - 2019.11.24
		M25 Orlando	Orlando, FL, U.S.A.	2019.11.11 - 2019.11.17
		M25 Naples	Naples, FL, U.S.A.	2019.11.18 - 2019.11.24
		Prague	Prague, Czech Republic	2019.07.22 - 2019.07.28
		M15 Prague	Prague, Czech Republic	2019.05.13 - 2019.05.19
		Prague	Prague, Czech Republic	2018.07.23 - 2018.07.29

"Opponent": Martin Damm
"LinkOpponent": "https://www.atptour.com/en/players/martin-damm/d0dt/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------

"Opponent": "Martin Damm"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/martin-damm/d214/player-activity?year=all&matchType=Singles"




```js

db.atpplayers.updateMany(
  {
    $or: [
      {Tournament: "ATP Masters 1000 Miami", Location: "Miami, FL, U.S.A.", Date: "2022.03.21 - 2022.04.03"},
      {Tournament: "M25 Bakersfield, CA", Location: "Bakersfield, CA, U.S.A.", Date: "2022.03.14 - 2022.03.20"},
      {Tournament: "M25 Glasgow", Location: "Glasgow, Great Britain", Date: "2022.02.14 - 2022.02.20"},
      {Tournament: "M25 Shrewsbury", Location: "Shrewsbury, Great Britain", Date: "2022.02.07 - 2022.02.13"},
      {Tournament: "M25 Loughborough", Location: "Loughborough, Great Britain", Date: "2022.01.24 - 2022.01.30"},
      {Tournament: "M25 Columbus", Location: "Columbus, OH, U.S.A.", Date: "2021.11.15 - 2021.11.21"},
      {Tournament: "Knoxville", Location: "Knoxville, TN, U.S.A.", Date: "2021.11.08 - 2021.11.14"},
      {Tournament: "Charlottesville", Location: "Charlottesville, VA, U.S.A.", Date: "2021.11.01 - 2021.11.07"},
      {Tournament: "M25 Toulouse", Location: "Toulouse, France", Date: "2021.10.18 - 2021.10.24"},
      {Tournament: "M25+H Rodez", Location: "Rodez, France", Date: "2021.10.11 - 2021.10.17"},
      {Tournament: "M25 Nevers", Location: "Nevers, France", Date: "2021.10.04 - 2021.10.10"},
      {Tournament: "M15 Fayetteville, AR", Location: "Fayetteville, AR, U.S.A.", Date: "2021.09.20 - 2021.09.26"},
      {Tournament: "M15 Champaign, IL", Location: "Champaign, IL, U.S.A.", Date: "2021.09.13 - 2021.09.19"},
      {Tournament: "M25 Champaign", Location: "Champaign, IL, U.S.A.", Date: "2021.07.26 - 2021.08.01"},
      {Tournament: "M25 Klosters", Location: "Klosters, Switzerland", Date: "2021.06.21 - 2021.06.27"},
      {Tournament: "M15 Edwardsville", Location: "Edwardsville, IL, U.S.A.", Date: "2021.07.19 - 2021.07.25"},
      {Tournament: "M15 Skopje", Location: "Skopje, Macedonia", Date: "2021.06.07 - 2021.06.13"},
      {Tournament: "M15 Skopje", Location: "Skopje, Macedonia", Date: "2021.05.31 - 2021.06.06"},
      {Tournament: "M25 Most", Location: "Most, Czech Republic", Date: "2021.05.24 - 2021.05.30"},
      {Tournament: "M15 Valldoreix", Location: "Valldoreix, Valldoreix", Date: "2021.05.10 - 2021.05.16"},
      {Tournament: "Tallahassee", Location: "Tallahassee, FL, U.S.A.", Date: "2021.04.19 - 2021.04.25"},
      {Tournament: "Orlando", Location: "Orlando, FL, U.S.A.", Date: "2021.04.12 - 2021.04.18"},
      {Tournament: "M15 Opatija", Location: "Opatija, Croatia", Date: "2021.03.22 - 2021.03.28"},
      {Tournament: "M15 Rovinj", Location: "Rovinj, Croatia", Date: "2021.03.15 - 2021.03.21"},
      {Tournament: "M15 Porec", Location: "Porec, Croatia", Date: "2021.03.08 - 2021.03.14"},
      {Tournament: "M25 Naples", Location: "Naples, FL, U.S.A.", Date: "2021.02.22 - 2021.02.28"},
      {Tournament: "M25 Naples", Location: "Naples, FL, U.S.A.", Date: "2021.02.15 - 2021.02.21"},
      {Tournament: "M15 Santo Domingo", Location: "Santo Domingo, Dominican Republic", Date: "2020.12.07 - 2020.12.13"},
      {Tournament: "M15 Santo Domingo", Location: "Santo Domingo, Dominican Republic", Date: "2020.11.30 - 2020.12.06"},
      {Tournament: "Orlando", Location: "Orlando, FL, U.S.A.", Date: "2020.11.16 - 2020.11.22"},
      {Tournament: "M15 Fayetteville", Location: "Fayetteville, AR, U.S.A.", Date: "2020.11.02 - 2020.11.08"},
      {Tournament: "M15 Monastir", Location: "Monastir, Tunisia", Date: "2020.10.05 - 2020.10.11"},
      {Tournament: "M15 Monastir", Location: "Monastir, Tunisia", Date: "2020.09.28 - 2020.10.04"},
      {Tournament: "M15 Curtea de Arges", Location: "Curtea de Arges, Romania", Date: "2020.09.14 - 2020.09.20"},
      {Tournament: "M15 Bucharest", Location: "Bucharest, Romania", Date: "2020.09.07 - 2020.09.13"},
      {Tournament: "M15 Antalya", Location: "Antalya, Turkey", Date: "2020.03.09 - 2020.03.15"},
      {Tournament: "M15 Antalya", Location: "Antalya, Turkey", Date: "2020.03.02 - 2020.03.08"},
      {Tournament: "M25 Naples", Location: "Naples, FL, U.S.A.", Date: "2019.11.18 - 2019.11.24"},
      {Tournament: "M25 Naples", Location: "Naples, FL, U.S.A.", Date: "2020.02.10 - 2020.02.16"},
      {Tournament: "M25 Orlando", Location: "Orlando, FL, U.S.A.", Date: "2019.11.11 - 2019.11.17"},
      {Tournament: "Prague", Location: "Prague, Czech Republic", Date: "2019.07.22 - 2019.07.28"},
      {Tournament: "M15 Prague", Location: "Prague, Czech Republic", Date: "2019.05.13 - 2019.05.19"},
      {Tournament: "Prague", Location: "Prague, Czech Republic", Date: "2018.07.23 - 2018.07.29"}
    ],
    Opponent: "Martin Damm"
  },
  {
    $set: {
      LinkOpponent: "https://www.atptour.com/en/players/martin-damm/d0dt/player-activity?year=all&matchType=Singles"
    }
  }
)



db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Martin Damm",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/martin-damm/d214/player-activity?year=all&matchType=Singles"
      }
    }
)


```




# 7) Robert Phillips

"Tournament" and "Location" and "Date" equal to:

		Tournament	Location	Date
		Australia F3	Melbourne, Australia	2003.11.03 - 2003.11.09
		Cherbourg	Cherbourg, France	1992.10.12 - 1992.10.18
		Istanbul	Istanbul, Turkey	1991.09.02 - 1991.09.08

"Opponent": "Robert Phillips"
"LinkOpponent": "https://www.atptour.com/en/players/robert-phillips/p239/player-activity?year=all&matchType=Singles"


---------------------------------------------------------------------------------------------------------------------------~---~-------------


"Opponent": "Robert Phillips"
"LinkOpponent": null

$set:
"LinkOpponent": "https://www.atptour.com/en/players/robert-phillips/pd13/player-activity?year=all&matchType=Singles"



```js

db.atpplayers.updateMany(
  {
    $or: [
      {Tournament: "Australia F3", Location: "Melbourne, Australia", Date: "2003.11.03 - 2003.11.09"},
      {Tournament: "Cherbourg", Location: "Cherbourg, France", Date: "1992.10.12 - 1992.10.18"},
      {Tournament: "Istanbul", Location: "Istanbul, Turkey", Date: "1991.09.02 - 1991.09.08"}
    ],
    Opponent: "Robert Phillips"
  },
  {
    $set: {
      LinkOpponent: "https://www.atptour.com/en/players/robert-phillips/p239/player-activity?year=all&matchType=Singles"
    }
  }
)



db.atpplayers.updateMany(
    // filter
    {
        "Opponent": "Robert Phillips",
        "LinkOpponent": null
    },

    // set command
    { "$set":
      {
        "LinkOpponent": "https://www.atptour.com/en/players/robert-phillips/pd13/player-activity?year=all&matchType=Singles"
      }
    }
)



```
