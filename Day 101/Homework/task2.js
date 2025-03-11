

const sportsClub = {
    clubName: "დინამო თბილისი",
    sportType: "ფეხბურთი",
    foundedYear: 1925,
    achievements: {
      title1: "საქართველოს ჩემპიონატი - 1990",
      title2: "საქართველოს თასი - 1992",
      title3: "საქართველოს სუპერთასი - 2005",
    },
  };
  

  console.log(Object.keys(sportsClub));
  

  console.log(Object.values(sportsClub));
  

  console.log(sportsClub.hasOwnProperty("sponsors")); 
  

  sportsClub.stadiumCapacity = 25000;
  
  
  Object.freeze(sportsClub);
  
  sportsClub.clubName = "ახალი სახელი"; 
  
  
  console.log(Object.isFrozen(sportsClub)); 
  